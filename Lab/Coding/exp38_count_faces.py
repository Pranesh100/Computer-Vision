"""
Experiment 38: Count the Number of Faces in an Image
=====================================================
Write a Python function to Count the number of faces for the given
input image using OpenCV.

This experiment uses a pre-trained Haar Cascade Classifier to detect all
human faces present in the input image, counts the total number of
occurrences, tags each face with an index (Face 1, Face 2, ...), and displays
a summary badge with the final face count.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Image with numbered faces and total count displayed; saved as exp38_output.jpg
"""

import cv2
import sys
import os

def count_faces_in_image(image_path):
    if not os.path.exists(image_path):
        print(f"[ERROR] Image not found: {image_path}")
        print("Please place 'image 1.jpg' in the same folder as this script.")
        sys.exit(1)

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar cascade classifier
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)

    if face_cascade.empty():
        print(f"[ERROR] Could not load Haar cascade classifier: {cascade_path}")
        sys.exit(1)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    total_faces = len(faces)
    print("=" * 45)
    print(f" TOTAL FACES DETECTED: {total_faces}")
    print("=" * 45)

    result = image.copy()

    for idx, (x, y, w, h) in enumerate(faces):
        # Draw bounding rectangle
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Face label
        label = f"#{idx + 1}"
        cv2.putText(result, label, (x + 5, y + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        print(f"Face #{idx + 1}: x={x}, y={y}, width={w}, height={h}")

    # Top banner showing total face count
    banner_text = f"Total Faces Detected: {total_faces}"
    cv2.rectangle(result, (10, 10), (380, 55), (0, 0, 0), -1)
    cv2.putText(result, banner_text, (20, 42),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    return image, result, total_faces

# Run detection
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image 1.jpg")
orig, result, count = count_faces_in_image(path)

cv2.imshow("Original Image", orig)
cv2.imshow("Count Faces Result", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp38_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")

