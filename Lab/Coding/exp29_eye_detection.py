"""
Experiment 29: Eye Detection using OpenCV
==========================================
Implement an Eye detection algorithm using OpenCV to detect and locate
human eyes in the images.

This experiment uses Haar Cascade Classifiers. To maximize accuracy and avoid
false detections, it first identifies the face region, and then searches for
eyes within the upper portion of each detected face region of interest (ROI).

Input : image 1.jpg  (placed in the same folder as this script)
Output: Image with detected eyes enclosed in bounding boxes, saved as exp29_output.jpg
"""

import cv2
import sys
import os

image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image 1.jpg")

if not os.path.exists(image_path):
    print(f"[ERROR] Image not found: {image_path}")
    print("Please place 'image 1.jpg' in the same folder as this script.")
    sys.exit(1)

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Haar cascades for face and eye
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

if face_cascade.empty() or eye_cascade.empty():
    print("[ERROR] Failed to load Haar cascades.")
    sys.exit(1)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
result = image.copy()
total_eyes = 0

print(f"Detected {len(faces)} face(s). Now searching for eyes within face regions...")

for (fx, fy, fw, fh) in faces:
    # Draw face boundary (blue)
    cv2.rectangle(result, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 2)
    cv2.putText(result, "Face", (fx, fy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Eyes are typically located in the upper half of the face
    roi_gray  = gray[fy:fy + int(fh * 0.65), fx:fx + fw]
    roi_color = result[fy:fy + int(fh * 0.65), fx:fx + fw]

    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))
    for (ex, ey, ew, eh) in eyes:
        total_eyes += 1
        # Draw eye boundary (green)
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        cv2.putText(roi_color, "Eye", (ex, ey - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

# If no faces were detected, attempt global eye detection as fallback
if len(faces) == 0:
    print("No faces detected; running direct global eye detection...")
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))
    for (ex, ey, ew, eh) in eyes:
        total_eyes += 1
        cv2.rectangle(result, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        cv2.putText(result, "Eye", (ex, ey - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

print(f"Total eyes detected: {total_eyes}")

cv2.imshow("Original Image", image)
cv2.imshow("Eye Detection Result", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp29_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")

