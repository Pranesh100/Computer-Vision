"""
Experiment 11: 180-Degree Clockwise Rotation
=============================================
Perform a 180-degree rotation clockwise along the y-axis for the given image.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Rotated image displayed on screen and saved as exp11_output.jpg
"""

import cv2
import sys
import os

image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image 1.jpg")

if not os.path.exists(image_path):
    print(f"[ERROR] Image not found: {image_path}")
    print("Please place 'image 1.jpg' in the same folder as this script.")
    sys.exit(1)

image   = cv2.imread(image_path)
rotated = cv2.rotate(image, cv2.ROTATE_180)

print("Original size :", image.shape)
print("Rotated  size :", rotated.shape)

cv2.imshow("Original Image", image)
cv2.imshow("180 Degree Clockwise Rotation", rotated)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp11_output.jpg")
cv2.imwrite(out, rotated)
print(f"Saved: {out}")
