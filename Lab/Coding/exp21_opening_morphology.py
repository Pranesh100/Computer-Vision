"""
Experiment 21: Opening Morphological Operation
================================================
Implement the Opening technique as a Morphological operation to dilate
the foreground regions based on OpenCV.

Opening is an Erosion followed by a Dilation. It is useful for removing
noise, small bright spots, and isolated foreground pixels without
significantly altering the size or shape of larger objects.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Opened images with different kernel sizes displayed; saved as exp21_output.jpg
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

# Define structuring elements (kernels) of different sizes
kernel_3 = np.ones((3, 3), np.uint8)
kernel_5 = np.ones((5, 5), np.uint8)
kernel_7 = np.ones((7, 7), np.uint8)

print("Applying Opening morphological operations...")
# Opening = Erosion followed by Dilation
opened_3 = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel_3)
opened_5 = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel_5)
opened_7 = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel_7)

print("Opening complete.")
print(f"Original size: {image.shape}")

cv2.imshow("Original Image", image)
cv2.imshow("Opening (Kernel 3x3)", opened_3)
cv2.imshow("Opening (Kernel 5x5)", opened_5)
cv2.imshow("Opening (Kernel 7x7)", opened_7)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp21_output.jpg")
cv2.imwrite(out, opened_5)
print(f"Saved: {out}")

