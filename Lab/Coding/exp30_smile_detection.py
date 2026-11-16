"""
Experiment 30: Smile Detection using OpenCV
============================================
Implement a Smile detection algorithm using OpenCV to detect and locate
human smile in the images.

This experiment combines face detection with smile detection using Haar
Cascade Classifiers. The algorithm locates the face, extracts the lower
region of interest (mouth/smile area), and determines if a smile is present.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Image with detected smile marked and labeled, saved as exp30_output.jpg
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

face_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

if face_cascade.empty() or smile_cascade.empty():
    print("[ERROR] Failed to load Haar cascades.")
    sys.exit(1)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
result = image.copy()
smiles_found = 0

print(f"Detected {len(faces)} face(s). Now searching for smile in lower face region...")

for (fx, fy, fw, fh) in faces:
    # Draw face boundary
    cv2.rectangle(result, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 2)
    cv2.putText(result, "Face", (fx, fy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Smile is in the lower half of the face
    roi_gray  = gray[fy + int(fh * 0.5):fy + fh, fx:fx + fw]
    roi_color = result[fy + int(fh * 0.5):fy + fh, fx:fx + fw]

    # Detect smiles
    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20, minSize=(25, 25))
    for (sx, sy, sw, sh) in smiles:
        smiles_found += 1
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
        cv2.putText(result, "Smiling :-)", (fx, fy + fh + 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

if smiles_found == 0:
    print("No smile detected in the face(s).")
    cv2.putText(result, "Neutral / No Smile Detected", (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
else:
    print(f"Total smile detections: {smiles_found}")

cv2.imshow("Original Image", image)
cv2.imshow("Smile Detection Result", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp30_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")

