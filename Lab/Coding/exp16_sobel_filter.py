"""
Experiment 16: Sobel Edge Detection Filter
============================================
Implement a Sobel algorithm using OpenCV to filter the input image.

The Sobel operator computes an approximation of the image gradient,
detecting edges by finding rapid intensity changes.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Sobel filtered images (X, Y, combined) saved as exp16_output.jpg
"""

import cv2
import numpy as np
import sys
import os

image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image 1.jpg")

if not os.path.exists(image_path):
    print(f"[ERROR] Image not found: {image_path}")
    print("Please place 'image 1.jpg' in the same folder as this script.")
    sys.exit(1)

image = cv2.imread(image_path)
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sobel in X direction  - detects vertical edges
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)

# Sobel in Y direction - detects horizontal edges
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combined Sobel - both directions equally weighted
sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

print("Sobel Filter applied successfully.")
print(f"Image size: {image.shape}")

cv2.imshow("Original Image", image)
cv2.imshow("Sobel X - Vertical Edges", sobel_x)
cv2.imshow("Sobel Y - Horizontal Edges", sobel_y)
cv2.imshow("Sobel Combined", sobel_combined)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp16_output.jpg")
cv2.imwrite(out, sobel_combined)
print(f"Saved: {out}")
