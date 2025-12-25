import cv2
from ultralytics import YOLO
import numpy as np
from deep_sort_realtime.deepsort_tracker import DeepSort

# py -3.10 -m venv ai_env
# ai_env\Scripts\activate
# pip install opencv-python ultralytics numpy
# pip install deep-sort-realtime
# python main.py

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Initialize Deep SORT
tracker = DeepSort(
    max_age=30,
    n_init=3,
    max_iou_distance=0.7
)

# Track ID → Label mapping
track_labels = {}

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO Detection
    results = model(frame, conf=0.3)
    detections = []

    if results and results[0].boxes is not None:
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            detections.append(
                ([x1, y1, x2 - x1, y2 - y1], conf, label)
            )

    # Deep SORT Tracking
    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        l, t, w, h = map(int, track.to_ltrb())

        # Save label for each track_id
        if track_id not in track_labels:
            if track.det_class is not None:
                track_labels[track_id] = track.det_class

        label = track_labels.get(track_id, "Object")

        cv2.rectangle(frame, (l, t), (l + w, t + h),
                      (0, 255, 0), 2)

        cv2.putText(
            frame,
            f"{label} ID:{track_id}",
            (l, t - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    cv2.imshow("YOLO + Deep SORT Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
