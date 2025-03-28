import os
import subprocess

# Check if libGL.so.1 exists and install it if missing
if not os.path.exists('/usr/lib/x86_64-linux-gnu/libGL.so.1'):
    subprocess.run(['sudo', 'apt-get', 'update'])
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'libgl1'])






import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO

# Cache the model loading to improve performance
@st.cache_resource
def load_model(model_path):
    return YOLO(model_path)

def main():
    st.title("MRI Detection with YOLO11")
    
    # Sidebar controls
    st.sidebar.header("Settings")
    conf_threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.5, 0.01)
    model_path = "best.pt"  # Update this path if needed

    # File uploader
    uploaded_file = st.file_uploader("Upload an MRI image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load image with PIL and convert to OpenCV format
        pil_image = Image.open(uploaded_file)
        img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
        
        # Load YOLO model
        model = load_model(model_path)
        
        # Perform detection
        results = model.predict(img, conf=conf_threshold)
        
        # Check if any objects were detected
        if len(results[0].boxes) == 0:
            st.warning("No MRI regions detected!")
            return
            
        # Create two columns for display
        col1, col2 = st.columns(2)
        
        # Original image with bounding boxes
        plotted_image = results[0].plot()  # Draws bounding boxes on the image
        plotted_image_rgb = cv2.cvtColor(plotted_image, cv2.COLOR_BGR2RGB)
        
        with col1:
            st.subheader("Detected MRI Regions")
            st.image(plotted_image_rgb, use_column_width=True)
        
        # Cropped regions
        with col2:
            st.subheader("Extracted Regions")
            boxes = results[0].boxes.xyxy.cpu().numpy()
            for i, box in enumerate(boxes):
                x1, y1, x2, y2 = map(int, box[:4])
                # Ensure coordinates are within image boundaries
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(img.shape[1], x2), min(img.shape[0], y2)
                
                # Extract and convert ROI
                roi = img[y1:y2, x1:x2]
                roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
                
                st.image(roi_rgb, caption=f"Region {i+1}", use_column_width=True)

if __name__ == "__main__":
    main()
