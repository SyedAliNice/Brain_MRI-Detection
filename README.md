# Brain_MRI-Detection

This project is a Streamlit-based application that uses a YOLO11 model to detect MRI regions in medical images. Users can upload MRI images, and the model will identify and highlight relevant regions.

## Features
- Upload MRI images in JPG, JPEG, or PNG formats
- Perform object detection using a YOLO11 model
- Display detected MRI regions with bounding boxes
- Extract and show cropped MRI regions separately
- Adjustable confidence threshold for predictions

## Requirements
Make sure you have the following dependencies installed:

        ```streamlit
        opencv-python
        ultralytics
        numpy
        pillow```

## Installation and Setup

Follow these steps to set up and run the project on your system:

1. Clone the Repository
    ``` git clone <repository_url>
        cd <repository_folder>```
2. Create a Virtual Environment (Optional but Recommended)
    ``` python -m venv venv
        source venv/bin/activate  # On macOS/Linux
        venv\Scripts\activate    # On Windows ```
3. Install Dependencies
    ``` pip install -r requirements.txt ```

4. Place the Model File

    Ensure that the `best.pt` YOLO model file is placed in the project directory.

5. Run the Application

    `streamlit run app.py`
    This will start the Streamlit web application, and you can access it in your browse

## How It Works

- Upload an MRI image.

- Adjust the confidence threshold using the sidebar.

- The YOLO11 model will analyze the image and detect regions.

- The detected regions will be highlighted and displayed separately.


## File Structure

    ``` 📂 project_folder
        ├── app.py              # Main Streamlit application
        ├── requirements.txt    # List of dependencies
        ├── best.pt             # YOLO model file (must be placed manually) ```

## Notes

- The best.pt model file should be trained and placed in the project directory before running the application.

- Make sure all dependencies are installed correctly to avoid errors.


## Author

Developed by Syed Ali Hassan
  
