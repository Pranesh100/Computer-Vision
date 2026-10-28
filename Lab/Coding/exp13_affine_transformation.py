"""
Experiment 13: Affine Transformation
======================================
Perform Affine Transformation on the given image using Python and OpenCV.

An affine transformation preserves lines and parallelism.
Three source points are mapped to three destination points to compute
the 2x3 transformation matrix.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Transformed image displayed and saved as exp13_output.jpg
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

# Three source points
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Three destination points (where source points map to)
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Compute the Affine Transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply the transformation
dst = cv2.warpAffine(image, M, (cols, rows))

print("Affine Transformation Matrix:")
print(M)

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformation", dst)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp13_output.jpg")
cv2.imwrite(out, dst)
print(f"Saved: {out}")
