🍎🍌 Fruit Object Detection using YOLO & Streamlit
📌 Project Overview

This project is a Fruit Object Detection web application built using YOLO (Ultralytics) and Streamlit.
Users can upload an image, and the model will detect fruits present in the image with bounding boxes and confidence scores.

🚀 Features

Detects multiple fruits in a single image

Uses a trained YOLO model (fruit.pt)

Adjustable confidence threshold

Simple and interactive Streamlit web interface

🛠️ Tech Stack

Python 3

YOLO (Ultralytics)

Streamlit

OpenCV

Pillow

NumPy

PyTorch

📂 Project Structure
Fruit_Object_Detection/
│
├── Fruit_object.py      # Streamlit application
├── fruit.pt             # Trained YOLO model
├── README.md            # Project documentation

⚙️ Installation & Setup
1️⃣ Clone or Upload Project Files

Upload the following files to your working directory:

Fruit_object.py

fruit.pt

2️⃣ Install Dependencies

Run the following command:

pip install ultralytics streamlit opencv-python pillow torch torchvision

3️⃣ Run the Application
streamlit run Fruit_object.py --server.address 0.0.0.0

4️⃣ Open in Browser

Open your browser and go to:

http://<YOUR_PUBLIC_IP>:8501

🧠 How It Works

User uploads an image through the Streamlit UI

The YOLO model loads the trained weights (fruit.pt)

The model detects fruits in the image

Bounding boxes and confidence scores are displayed

📸 Input & Output

Input:

JPG / JPEG / PNG image

Output:

Image with detected fruits highlighted

Confidence score for each detection

📊 Model Details

Model: YOLO (Ultralytics)

Weights file: fruit.pt

Task: Object Detection

Classes: Fruits (as trained in the dataset)

⚠️ Notes

Ensure fruit.pt is in the same folder as Fruit_object.py

CloudShell is not recommended due to storage limits

Best run on EC2 / local machine

📌 Future Improvements

Add webcam/live detection

Deploy using Docker

Improve accuracy with more training data

Add fruit count feature

👩‍💻 Author

Sangavi Annadhurai
Fruit Object Detection Project
