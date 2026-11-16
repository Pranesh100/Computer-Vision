"""
Experiment 28: Vehicle Detection in Video
==========================================
Implement a vehicle detection algorithm using OpenCV to detect and locate
vehicles in each frame of the video.

This experiment uses Background Subtraction (MOG2) combined with morphological
filtering and contour analysis to locate moving vehicles on roads across
video frames, bounding each detected vehicle with a green rectangle.

Input : 220268_medium.mp4  (placed in the same folder as this script)
Output: Real-time detection display and keyframe saved as exp28_output.jpg
"""

import cv2
import numpy as np
import sys
import os

video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "220268_medium.mp4")

if not os.path.exists(video_path):
    print(f"[ERROR] Video not found: {video_path}")
    print("Please place '220268_medium.mp4' in the same folder as this script.")
    sys.exit(1)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("[ERROR] Cannot open video.")
    sys.exit(1)

# Initialize Background Subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

saved_sample = None
frame_count = 0

print("Processing video for vehicle detection... Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    # Resize frame for efficient display if needed
    h, w = frame.shape[:2]
    if w > 960:
        scale = 960 / w
        frame = cv2.resize(frame, (int(w * scale), int(h * scale)))

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(frame)

    # Threshold to remove shadows (shadow pixels are gray ~127)
    _, thresh = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY)

    # Morphological operations to remove noise and fill holes in vehicles
    dilated = cv2.dilate(thresh, kernel, iterations=2)
    closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find contours representing moving vehicles
    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    vehicle_count = 0
    display_frame = frame.copy()

    for cnt in contours:
        area = cv2.contourArea(cnt)
        # Filter small noise contours
        if area > 1200:
            x, y, cw, ch = cv2.boundingRect(cnt)
            # Aspect ratio and size check for vehicles
            if cw > 30 and ch > 30:
                vehicle_count += 1
                cv2.rectangle(display_frame, (x, y), (x + cw, y + ch), (0, 255, 0), 2)
                cv2.putText(display_frame, "Vehicle", (x, y - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display vehicle count on top of frame
    cv2.putText(display_frame, f"Frame: {frame_count} | Vehicles: {vehicle_count}",
                (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Vehicle Detection", display_frame)
    cv2.imshow("Foreground Mask", closing)

    # Save a keyframe that has detected vehicles
    if vehicle_count > 0 and saved_sample is None:
        saved_sample = display_frame.copy()

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if saved_sample is None:
    saved_sample = display_frame

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp28_output.jpg")
cv2.imwrite(out, saved_sample)
print(f"Sample detection keyframe saved to: {out}")

