"""
Experiment 27: Face Detection using OpenCV
============================================
Implement a face detection algorithm using OpenCV to detect and locate
human faces in the images.

This experiment uses Haar Feature-based Cascade Classifiers proposed by
Paul Viola and Michael Jones. The classifier is trained on thousands of
positive (faces) and negative (non-faces) images to detect faces in real-time.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Image with detected faces enclosed in bounding boxes, saved as exp27_output.jpg
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

# Load OpenCV's pre-trained Haar Cascade for frontal face detection
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print(f"[ERROR] Failed to load Haar Cascade from: {cascade_path}")
    sys.exit(1)

# Detect faces in the grayscale image
# scaleFactor : compensates for faces being closer/further from camera
# minNeighbors: specifies how many neighbors each candidate rectangle should have
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"Total faces detected: {len(faces)}")

result = image.copy()
for i, (x, y, w, h) in enumerate(faces):
    # Draw green bounding box around each face
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
    label = f"Face {i + 1}"
    cv2.putText(result, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    print(f"Face {i + 1} located at: x={x}, y={y}, width={w}, height={h}")

if len(faces) == 0:
    print("No faces detected in the input image. (Try using an image with clear visible human faces)")
    cv2.putText(result, "No Face Detected", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

cv2.imshow("Original Image", image)
cv2.imshow("Face Detection Result", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp27_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")

