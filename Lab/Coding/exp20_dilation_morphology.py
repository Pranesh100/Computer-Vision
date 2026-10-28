"""
Experiment 20: Dilation Morphological Operation
=================================================
Implement the Dilation technique as a Morphological operation to dilate
the foreground regions based on OpenCV.

Dilation expands the white (foreground) regions, useful for joining broken
parts and filling small holes in objects.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Dilated images with 1/2/3 iterations displayed; saved as exp20_output.jpg
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

# Apply Dilation with increasing iterations
dilated_1 = cv2.dilate(image, kernel, iterations=1)
dilated_2 = cv2.dilate(image, kernel, iterations=2)
dilated_3 = cv2.dilate(image, kernel, iterations=3)

cv2.imshow("Original Image", image)
cv2.imshow("Dilated 1 Iteration", dilated_1)
cv2.imshow("Dilated 2 Iterations", dilated_2)
cv2.imshow("Dilated 3 Iterations", dilated_3)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp20_output.jpg")
cv2.imwrite(out, dilated_1)
print(f"Saved: {out}")
