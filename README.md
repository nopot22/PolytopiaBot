# PolytopiaBot

A Python-based bot for image processing and object detection in the context of Polytopia, utilizing YOLOv8 models for inference.

## Description

This project demonstrates how to perform object detection on images using a pre-trained YOLOv8 model. It loads an image, runs inference, annotates detected objects with bounding boxes and labels, and displays the result.

## Installation

1. Clone or download the repository.
2. Create a virtual environment(Python <3.13, >=3.9):
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install the required dependencies:
   ```
   pip install inference supervision opencv-python
   ```

## Usage

1. Place your image file (e.g., `IMG_0153.PNG`) in the project directory.
2. Update the `image_file` variable in `test.py` if necessary.
3. Run the script:
   ```
   python test.py
   ```
4. The annotated image will be displayed.

## Dependencies

- `inference`: For loading and running the YOLOv8 model.
- `supervision`: For handling detections and annotations.
- `opencv-python`: For image processing.

## Model

The script uses a custom model identified as "polybot/2". Ensure you have access to this model via the inference library.

## License

[Specify your license here, e.g., MIT]
