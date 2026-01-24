import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np

st.title("🍎🍌🍊 Fruit Object Detection")

# Load model
model = YOLO("fruit.pt")  # ensure best.pt is in same folder

# Confidence slider
conf_threshold = st.slider("Confidence Threshold", 0.1, 1.0, 0.5, 0.05)

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")

    # Run inference
    results = model(img, conf=conf_threshold)

    # Plot detections
    annotated = results[0].plot()
    annotated = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    st.image(annotated, caption="Detected Fruits", use_column_width=True)

    # Collect detected classes
    detected_info = []
    for box, cls, conf in zip(
        results[0].boxes.xyxy,
        results[0].boxes.cls,
        results[0].boxes.conf
    ):
        detected_info.append(f"{model.names[int(cls)]}: {conf:.2f}")

    # Display results
    if detected_info:
        st.subheader("Detected Fruits:")
        for item in detected_info:
            st.write(item)
    else:
        st.write("No fruits detected. Try lowering the confidence threshold.")