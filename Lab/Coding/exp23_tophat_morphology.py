"""
Experiment 23: Top Hat Morphological Operation
================================================
Implement the Top hat technique as a Morphological operation to dilate
the foreground regions based on OpenCV.

Top Hat (White Top Hat) is the difference between the input image and its
Opening (Image - Opening(Image)). It isolates and enhances elements, fine
details, or bright structures that are smaller than the structuring element
against a dark or uneven background.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Top Hat filtered images displayed; saved as exp23_output.jpg
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

# Define structuring elements (rectangular or elliptical)
kernel_5 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_9 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
kernel_15 = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

print("Applying Top Hat morphological operations...")
# Top Hat = Input Image - Opening(Image)
tophat_5  = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel_5)
tophat_9  = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel_9)
tophat_15 = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel_15)

print("Top Hat operation complete.")
print(f"Original size: {image.shape}")

cv2.imshow("Original Image", image)
cv2.imshow("Top Hat (Kernel 5x5)", tophat_5)
cv2.imshow("Top Hat (Kernel 9x9)", tophat_9)
cv2.imshow("Top Hat (Kernel 15x15)", tophat_15)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp23_output.jpg")
cv2.imwrite(out, tophat_9)
print(f"Saved: {out}")

