CodeAlpha_tasks
Structure:

Object Detection and Tracking using YOLOv8 & Deep SORT
📌 Description
This project implements a real-time object detection and tracking system using a webcam. YOLOv8 is used for detecting objects in each video frame, while Deep SORT is applied to track detected objects and assign unique tracking IDs along with class labels in real time.

🚀 Features
Real-time video input using webcam
Object detection using pre-trained YOLOv8 model
Object tracking using Deep SORT algorithm
Bounding boxes with object name and unique tracking ID
Real-time display using OpenCV

🛠️ Tech Stack
Python 3.10
OpenCV
YOLOv8 (Ultralytics)
Deep SORT
NumPy

2.Create a virtual environment:
py -3.10 -m venv ai_env

3.Activate the virtual environment: 
ai_env\Scripts\activate

4.Install required libraries:
pip install opencv-python ultralytics numpy deep-sort-realtime

5.How to Run 
python main.py

6.Output
The system displays bounding boxes around detected objects with:
Object class name Unique tracking ID in real time on the video stream.

7.Conclusion
This project demonstrates the practical implementation of computer vision techniques for object detection and tracking. The integration of YOLOv8 and Deep SORT enables accurate real-time tracking, making it suitable for surveillance, traffic monitoring, and smart vision applications.
