"""
Experiment 22: Closing Morphological Operation
================================================
Implement the Closing technique as a Morphological operation to dilate
the foreground regions based on OpenCV.

Closing is a Dilation followed by an Erosion. It is useful for closing
small dark holes, filling gaps in object contours, and connecting nearby
components without significantly changing their size.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Closed images with different kernel sizes displayed; saved as exp22_output.jpg
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

# Define structuring elements (kernels)
kernel_3 = np.ones((3, 3), np.uint8)
kernel_5 = np.ones((5, 5), np.uint8)
kernel_7 = np.ones((7, 7), np.uint8)

print("Applying Closing morphological operations...")
# Closing = Dilation followed by Erosion
closed_3 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_3)
closed_5 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_5)
closed_7 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_7)

print("Closing complete.")
print(f"Original size: {image.shape}")

cv2.imshow("Original Image", image)
cv2.imshow("Closing (Kernel 3x3)", closed_3)
cv2.imshow("Closing (Kernel 5x5)", closed_5)
cv2.imshow("Closing (Kernel 7x7)", closed_7)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp22_output.jpg")
cv2.imwrite(out, closed_5)
print(f"Saved: {out}")

