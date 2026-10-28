"""
Experiment 14: Perspective Transformation
==========================================
Perform Perspective Transformation on the given image using Python and OpenCV.

A perspective transformation maps 4 source points to 4 destination points,
simulating a viewpoint change (useful for correcting skewed documents etc.).

Input : image 1.jpg  (placed in the same folder as this script)
Output: Transformed image displayed and saved as exp14_output.jpg
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
rows, cols, _ = image.shape

# Four source points (corners of the region to warp)
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])

# Four destination points (where source corners should map to)
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# Compute the Perspective Transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the transformation
dst = cv2.warpPerspective(image, M, (300, 300))

print("Perspective Transformation Matrix:")
print(M)

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", dst)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp14_output.jpg")
cv2.imwrite(out, dst)
print(f"Saved: {out}")
