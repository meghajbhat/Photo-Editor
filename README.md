# Photo Editor Application

This **Photo Editor Application** is a Python-based project that provides users with an intuitive interface to edit and apply various filters to their images. The application is built using **Tkinter** for the graphical user interface (GUI) and **OpenCV** for image processing.

## Features

1. **Image Upload**:
   - Select images using a file dialog for editing and processing.
   - Preview uploaded images in the application.

2. **Filters and Transformations**:
   - **Black and White**: Converts the image to grayscale.
   - **Pencil Sketch**: Applies a pencil sketch effect.
   - **Sepia**: Adds a sepia tone to the image.
   - **Crop**: Crops a predefined area from the image.
   - **Sharpen**: Enhances image sharpness using a sharpening kernel.
   - **Contrast**: Adjusts the image's contrast and brightness.
   - **X-ray**: Creates an inverted version of the image for an X-ray-like effect.
   - **Brighten**: Increases the brightness of the image.

3. **Graphical User Interface**:
   - Built with **Tkinter** for an intuitive and interactive layout.
   - Buttons for each filter with clear labels.
   - Organized design with frames to manage button layout and functionality.

## Technologies and Tools Used

### Programming Language
- **Python**

### Libraries/Frameworks
1. **OpenCV**:
   - For image processing and transformations (e.g., grayscale conversion, kernel operations).
2. **NumPy**:
   - To handle image data and perform kernel matrix operations.
3. **Tkinter**:
   - For GUI design and file dialog integration.

### Tools/Platforms
- **Python IDLE**
- **VS Code** (Optional for editing)
- **OpenCV** for advanced image manipulation.

## How to Use

1. Clone the repository or download the `photo_editor_python_idle.py` file.
2. Install the required dependencies using:
   ```bash
   pip install opencv-python-headless numpy
3. Run the script:
   ```bash
   python photo_editor_python_idle.py
4. Use the "GO" button in the main window to launch the photo editor.
5. Upload an image using the "ADD IMAGE" button.
6. Apply filters using the feature-specific buttons:
7. Black and White, Pencil Sketch, Sepia, etc.
8. Preview the modified image in the popup window.

## Features

### 1. Black and White
- Converts the image to grayscale using OpenCV's `cv2.cvtColor`.

### 2. Pencil Sketch
- Applies a pencil sketch effect by combining grayscale conversion and morphological transformations.

### 3. Sepia
- Applies a sepia tone using a predefined kernel matrix.

### 4. Crop
- Crops the image to a predefined rectangular area.

### 5. Sharpen
- Enhances edges using a sharpening kernel filter.

### 6. Contrast
- Adjusts contrast and brightness with `cv2.convertScaleAbs`.

### 7. X-ray
- Inverts the image colors to create an X-ray-like effect.

### 8. Brighten
- Increases brightness using an alpha and beta scaling approach.

## Possible Enhancements
- **Dynamic Crop Selection**: Allow users to interactively select crop areas with the mouse.
- **Save Edited Image**: Add a feature to save the modified images.
- **Support for More File Formats**: Expand support for formats like PNG, TIFF, and BMP.
- **Real-Time Filter Preview**: Show filter previews before applying changes.
- **Undo/Redo**: Add undo/redo functionality for enhanced usability.
