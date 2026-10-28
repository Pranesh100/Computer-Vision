"""
Experiment 15: Harris Corner Detection
========================================
Read an image and detect corners using the Harris Corner Detection function.

The Harris Corner Detector identifies corners by examining how pixel
intensity changes in different directions using a sliding window.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Image with detected corners highlighted in red, saved as exp15_output.jpg
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

image  = cv2.imread(image_path)
gray   = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_f = np.float32(gray)

# Harris Corner Detection
# blockSize : size of the neighbourhood considered for corner detection
# ksize     : aperture parameter for the Sobel operator
# k         : Harris detector free parameter (0.04 - 0.06)
dst = cv2.cornerHarris(gray_f, blockSize=2, ksize=3, k=0.04)

# Dilate to make corners more visible
dst = cv2.dilate(dst, None)

# Threshold: mark strong corners in red on a copy of the original
result = image.copy()
result[dst > 0.01 * dst.max()] = [0, 0, 255]   # Red pixels

print("Harris Corner Detection complete.")
print(f"Number of corner pixels detected: {(dst > 0.01 * dst.max()).sum()}")

cv2.imshow("Original Image", image)
cv2.imshow("Harris Corner Detection", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp15_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")
