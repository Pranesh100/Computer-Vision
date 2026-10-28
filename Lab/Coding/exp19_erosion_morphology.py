"""
Experiment 19: Erosion Morphological Operation
================================================
Implement the Erosion Morphological operations technique using OpenCV in Python.

Erosion shrinks the white (foreground) regions by eroding boundaries,
useful for removing small white noise and separating connected objects.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Eroded images with 1/2/3 iterations displayed; saved as exp19_output.jpg
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

# Define the structuring element (kernel)
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)
print(f"Structuring element: {kernel_size}x{kernel_size} rectangular kernel")

# Apply Erosion with increasing iterations
eroded_1 = cv2.erode(image, kernel, iterations=1)
eroded_2 = cv2.erode(image, kernel, iterations=2)
eroded_3 = cv2.erode(image, kernel, iterations=3)

cv2.imshow("Original Image", image)
cv2.imshow("Eroded 1 Iteration", eroded_1)
cv2.imshow("Eroded 2 Iterations", eroded_2)
cv2.imshow("Eroded 3 Iterations", eroded_3)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp19_output.jpg")
cv2.imwrite(out, eroded_1)
print(f"Saved: {out}")
