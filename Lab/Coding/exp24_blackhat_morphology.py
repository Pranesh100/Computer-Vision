"""
Experiment 24: Black Hat Morphological Operation
=================================================
Implement the Black hat technique as a Morphological operation to dilate
the foreground regions based on OpenCV.

Black Hat is the difference between the Closing of the input image and
the input image itself (Closing(Image) - Image). It isolates and highlights
dark structures and details that are smaller than the structuring element
against bright or lighter surroundings.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Black Hat filtered images displayed; saved as exp24_output.jpg
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

# Define structuring elements
kernel_5  = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_9  = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
kernel_15 = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

print("Applying Black Hat morphological operations...")
# Black Hat = Closing(Image) - Input Image
blackhat_5  = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel_5)
blackhat_9  = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel_9)
blackhat_15 = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel_15)

print("Black Hat operation complete.")
print(f"Original size: {image.shape}")

cv2.imshow("Original Image", image)
cv2.imshow("Black Hat (Kernel 5x5)", blackhat_5)
cv2.imshow("Black Hat (Kernel 9x9)", blackhat_9)
cv2.imshow("Black Hat (Kernel 15x15)", blackhat_15)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp24_output.jpg")
cv2.imwrite(out, blackhat_9)
print(f"Saved: {out}")

