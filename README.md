# Photo Editor Application

This **Photo Editor Application** is a Python-based project designed to provide users with an intuitive interface for editing and applying various filters to their images. The application is built using **PyQt5** for the graphical user interface (GUI) and **OpenCV** for image processing.

---

## Features

### 1. **Image Upload and Display**
- Select images using a file dialog for editing and processing.
- Preview uploaded images within the application.

### 2. **Image Editing Tools**
- **Brightness Adjustment**: Modify brightness levels using a slider.
- **Contrast Adjustment**: Fine-tune contrast for better visuals.
- **Sepia Effect**: Apply a sepia filter to give images a vintage look.
- **Blur Effect**: Smooth images by adding Gaussian blur.
- **Edge Detection**: Highlight edges using the Canny edge detection algorithm.
- **Rotation**: Rotate the image to any angle using a slider.
- **Grayscale Conversion**: Convert the image to grayscale for a monochromatic effect.
- **Flip Image**: Flip the image horizontally or vertically.

### 3. **Undo/Redo Functionality**
- Allows users to revert or redo changes made to the image.

### 4. **Reset and Save**
- Reset: Revert the image back to its original state.
- Save: Save edited images in various formats such as PNG, JPG, and BMP.

---

## Technologies and Tools Used

### Programming Language
- **Python**

### Libraries/Frameworks
1. **OpenCV**:
   - Image processing and transformations.
2. **NumPy**:
   - Mathematical and array operations.
3. **PyQt5**:
   - GUI design and sliders for user input.

### Tools/Platforms
- **Python IDLE**
- **VS Code** (Optional for editing)
- **OpenCV** for advanced image manipulation.

---

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repository/photo-editor.git
   ```

2. **Install Dependencies**
   ```bash
   pip install opencv-python-headless numpy PyQt5
   ```

3. **Run the Application**
   ```bash
   python photo_editor.py
   ```

---

## How to Use

1. Launch the application.
2. Click **Load Image** to upload an image from your file system.
3. Use the sliders to adjust brightness, contrast, sepia effect, blur, edge detection, and rotation.
4. Apply additional effects like **Grayscale** and **Flip Image** using their respective buttons.
5. Undo or redo changes using the **Undo** and **Redo** buttons.
6. Click **Reset** to restore the image to its original state.
7. Save the edited image by clicking **Save Image** and specifying the desired format.

---

## Feature Details

### 1. Brightness Adjustment
- Adjusts image brightness by modifying pixel values using OpenCV's `convertScaleAbs()`.

### 2. Contrast Adjustment
- Enhances image contrast using scaling factors applied with OpenCV.

### 3. Sepia Effect
- Applies a predefined kernel matrix to generate a sepia tone.

### 4. Blur Effect
- Smooths the image using Gaussian blur with a customizable kernel size.

### 5. Edge Detection
- Highlights edges using OpenCV's Canny edge detection algorithm.

### 6. Rotation
- Rotates the image based on the specified angle using transformation matrices.

### 7. Grayscale Conversion
- Converts the image to grayscale using OpenCV's `cvtColor()` function.

### 8. Flip Image
- Flips the image horizontally or vertically based on user selection.

### 9. Undo/Redo
- Maintains a stack of changes, enabling users to revert and reapply modifications.

---

## Acknowledgments
- **OpenCV** for providing powerful image processing tools.
- **PyQt5** for enabling GUI-based interactions.

---

## Contact
For any issues or feature requests, please open an issue in the repository or reach out via email at **coderboy396@gmail.com** or **meghajbhat@gmail.com**.
