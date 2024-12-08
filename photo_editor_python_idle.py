import sys
import cv2
import numpy as np
import os
from PyQt5.QtWidgets import (
    QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QWidget, QMainWindow, QMessageBox, QSlider, QGridLayout, QSplitter
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

# Global variables for image manipulation and undo/redo functionality
image = None
original_image = None
file_path = None
undo_stack = []
redo_stack = []

# Function to load an image from the file system
def load_image():
    global image, original_image, file_path, undo_stack, redo_stack
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getOpenFileName(None, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
    if file_path:
        image = cv2.imread(file_path)  # Read image using OpenCV
        original_image = image.copy()  # Store the original image for resets
        undo_stack.clear()  # Clear the undo stack when a new image is loaded
        redo_stack.clear()  # Clear the redo stack
        undo_stack.append(image.copy())  # Add the initial image to the undo stack
        display_image()  # Display the image on the GUI
        
        # Enable buttons and sliders after an image is loaded
        save_button.setEnabled(True)
        reset_button.setEnabled(True)
        undo_button.setEnabled(True)
        redo_button.setEnabled(True)
        brightness_slider.setEnabled(True)
        contrast_slider.setEnabled(True)
        sepia_slider.setEnabled(True)
        blur_slider.setEnabled(True)
        edge_slider.setEnabled(True)
        rotate_slider.setEnabled(True)

# Function to save the current image to a file
def save_image():
    global image
    if image is not None:
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            None, 
            "Save Image File", 
            "", 
            "PNG (*.png);;JPEG (*.jpg *.jpeg);;BMP (*.bmp);;All Files (*)", 
            options=options
        )
        
        if file_path:
            try:
                file_extension = os.path.splitext(file_path)[1].lower()  # Get file extension
                
                # Default to .png if no extension is provided
                if not file_extension:
                    file_path += '.png'
                
                # Save the image based on its format
                if len(image.shape) == 2:
                    cv2.imwrite(file_path, image)  # Save grayscale image
                else:
                    if image.shape[2] == 3:
                        cv2.imwrite(file_path, image)  # Save BGR image
                    elif image.shape[2] == 4:
                        image_bgr = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)  # Convert to BGR if image has alpha channel
                        cv2.imwrite(file_path, image_bgr)
                    else:
                        raise ValueError("Unsupported image format")
                
                QMessageBox.information(None, "Save Successful", f"Image saved to {file_path}")
            
            except Exception as e:
                QMessageBox.warning(None, "Save Error", f"Could not save image: {str(e)}")
    else:
        QMessageBox.warning(None, "No Image", "Please load an image before saving.")

# Function to reset the image to its original state
def reset_image():
    global image, original_image, undo_stack, redo_stack
    if original_image is not None:
        image = original_image.copy()  # Reset image to the original
        undo_stack.clear()  # Clear undo stack
        redo_stack.clear()  # Clear redo stack
        undo_stack.append(image.copy())  # Add reset image to the undo stack
        display_image()  # Display the reset image
    else:
        QMessageBox.warning(None, "No Image", "Please load an image before resetting.")

# Function to display the image in the GUI
def display_image():
    if image is not None:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for display
        height, width, channels = rgb_image.shape
        bytes_per_line = channels * width
        q_image = QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)  # Create QImage from the OpenCV image
        pixmap = QPixmap.fromImage(q_image)  # Convert QImage to QPixmap for display in QLabel
        image_label.setPixmap(pixmap.scaled(image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))  # Scale the pixmap to fit label

# Push current image state to undo stack
def push_to_undo():
    global undo_stack
    if image is not None:
        undo_stack.append(image.copy())  # Add the current image to the undo stack
        if len(undo_stack) > 20:  # Keep stack size manageable by removing oldest state
            undo_stack.pop(0)

# Function to undo the last change
def undo():
    global image, undo_stack, redo_stack
    if len(undo_stack) > 1:  # Check if there's something to undo
        redo_stack.append(undo_stack.pop())  # Move current state to redo stack
        image = undo_stack[-1].copy()  # Set image to the last undo state
        display_image()  # Display the undone image
    else:
        QMessageBox.information(None, "Undo", "Nothing to undo.")

# Function to redo the last undone change
def redo():
    global image, redo_stack
    if redo_stack:
        push_to_undo()  # Save current state to undo stack before redoing
        image = redo_stack.pop()  # Pop from redo stack and apply image
        display_image()  # Display the redone image
    else:
        QMessageBox.information(None, "Redo", "Nothing to redo.")

# Function to adjust brightness of the image
def adjust_brightness(value):
    global image
    if original_image is not None:
        alpha = 1.0 + (value / 100)  # Adjust brightness scaling factor
        beta = 50 * (value / 100)  # Adjust brightness offset
        image = cv2.convertScaleAbs(original_image, alpha=alpha, beta=beta)  # Apply brightness change
        display_image()

# Function to adjust contrast of the image
def adjust_contrast(value):
    global image
    if original_image is not None:
        alpha = 1.0 + (value / 100)  # Adjust contrast scaling factor
        image = cv2.convertScaleAbs(original_image, alpha=alpha, beta=0)  # Apply contrast change
        display_image()

# Function to apply sepia effect to the image
def adjust_sepia(value):
    global image
    if original_image is not None:
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])  # Sepia filter matrix
        sepia_img = cv2.transform(original_image, kernel)  # Apply sepia filter
        image = cv2.addWeighted(original_image, 1 - value / 100, sepia_img, value / 100, 0)  # Blend sepia filter with original image
        display_image()

# Function to apply blur effect to the image
def adjust_blur(value):
    global image
    if original_image is not None:
        kernel_size = max(1, value // 10 * 2 + 1)  # Calculate kernel size for blur
        image = cv2.GaussianBlur(original_image, (kernel_size, kernel_size), 0)  # Apply Gaussian blur
        display_image()

# Function to apply edge detection to the image
def adjust_edge(value):
    global image
    if original_image is not None:
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale
        edges = cv2.Canny(gray_image, value, value * 2)  # Apply Canny edge detection
        image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)  # Convert edge image back to BGR
        display_image()

# Function to rotate the image by a given angle
def rotate_image(value):
    global image
    if original_image is not None:
        (h, w) = original_image.shape[:2]  # Get image dimensions
        center = (w // 2, h // 2)  # Set the rotation center
        matrix = cv2.getRotationMatrix2D(center, value, 1.0)  # Generate rotation matrix
        image = cv2.warpAffine(original_image, matrix, (w, h))  # Apply rotation transformation
        display_image()

# PyQt5 GUI setup
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Photo Editor")
window.resize(1200, 800)

central_widget = QWidget()
window.setCentralWidget(central_widget)

splitter = QSplitter(Qt.Vertical)

# QLabel to display the image
image_label = QLabel()
image_label.setMinimumSize(400, 300)
image_label.setAlignment(Qt.AlignCenter)
image_label.setStyleSheet("border: 2px solid black; background-color: #f0f0f0;")

# Layout for controls and buttons
controls_widget = QWidget()
controls_layout = QVBoxLayout()

# Layout for buttons
button_layout = QHBoxLayout()
load_button = QPushButton("Load Image")
save_button = QPushButton("Save Image")
reset_button = QPushButton("Reset Image")
undo_button = QPushButton("Undo")
redo_button = QPushButton("Redo")

save_button.setEnabled(False)
reset_button.setEnabled(False)
undo_button.setEnabled(False)
redo_button.setEnabled(False)

button_layout.addWidget(load_button)
button_layout.addWidget(save_button)
button_layout.addWidget(reset_button)
button_layout.addWidget(undo_button)
button_layout.addWidget(redo_button)

# Layout for sliders (brightness, contrast, etc.)
slider_layout = QGridLayout()

brightness_slider = QSlider(Qt.Horizontal)
brightness_slider.setRange(-100, 100)
brightness_slider.setValue(0)
brightness_slider.valueChanged.connect(adjust_brightness)
brightness_slider.setEnabled(False)

contrast_slider = QSlider(Qt.Horizontal)
contrast_slider.setRange(-100, 100)
contrast_slider.setValue(0)
contrast_slider.valueChanged.connect(adjust_contrast)
contrast_slider.setEnabled(False)

sepia_slider = QSlider(Qt.Horizontal)
sepia_slider.setRange(0, 100)
sepia_slider.setValue(0)
sepia_slider.valueChanged.connect(adjust_sepia)
sepia_slider.setEnabled(False)

blur_slider = QSlider(Qt.Horizontal)
blur_slider.setRange(0, 100)
blur_slider.setValue(0)
blur_slider.valueChanged.connect(adjust_blur)
blur_slider.setEnabled(False)

edge_slider = QSlider(Qt.Horizontal)
edge_slider.setRange(0, 100)
edge_slider.setValue(0)
edge_slider.valueChanged.connect(adjust_edge)
edge_slider.setEnabled(False)

rotate_slider = QSlider(Qt.Horizontal)
rotate_slider.setRange(0, 360)
rotate_slider.setValue(0)
rotate_slider.valueChanged.connect(rotate_image)
rotate_slider.setEnabled(False)

slider_layout.addWidget(QLabel("Brightness"), 0, 0)
slider_layout.addWidget(brightness_slider, 0, 1)
slider_layout.addWidget(QLabel("Contrast"), 1, 0)
slider_layout.addWidget(contrast_slider, 1, 1)
slider_layout.addWidget(QLabel("Sepia"), 2, 0)
slider_layout.addWidget(sepia_slider, 2, 1)
slider_layout.addWidget(QLabel("Blur"), 3, 0)
slider_layout.addWidget(blur_slider, 3, 1)
slider_layout.addWidget(QLabel("Edge Detection"), 4, 0)
slider_layout.addWidget(edge_slider, 4, 1)
slider_layout.addWidget(QLabel("Rotate"), 5, 0)
slider_layout.addWidget(rotate_slider, 5, 1)

controls_layout.addLayout(button_layout)
controls_layout.addLayout(slider_layout)
controls_widget.setLayout(controls_layout)

# Add controls and image display to the main layout
splitter.addWidget(image_label)
splitter.addWidget(controls_widget)

splitter.setSizes([700, 300])

main_layout = QVBoxLayout()
main_layout.addWidget(splitter)
central_widget.setLayout(main_layout)

# Connect buttons to their respective functions
load_button.clicked.connect(load_image)
save_button.clicked.connect(save_image)
reset_button.clicked.connect(reset_image)
undo_button.clicked.connect(undo)
redo_button.clicked.connect(redo)

window.show()

# Start the PyQt5 application event loop
sys.exit(app.exec_())
