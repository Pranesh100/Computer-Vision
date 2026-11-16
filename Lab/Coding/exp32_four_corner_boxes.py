"""
Experiment 32: Create White Image with 4 Colored Corner Boxes
==============================================================
Write a Python function to create a white image size entered by the user
and then create 4 boxes of Black, Blue, Green and Red respectively on each
corner of the image. The size of the colored boxes should be 1/10th the
size of the image. (HINT: the arrays of ones and zeros can be in more
than 2 dimensions).

Corner Layout:
- Top-Left     : Black [0, 0, 0]
- Top-Right    : Blue  [255, 0, 0]  (OpenCV BGR format)
- Bottom-Left  : Green [0, 255, 0]
- Bottom-Right : Red   [0, 0, 255]

Input : User enters height and width (e.g., 500 500)
Output: Generated image with corner boxes displayed and saved as exp32_output.jpg
"""

import cv2
import numpy as np
import os
import sys

def create_four_corner_boxes(height=500, width=500):
    """
    Creates a white canvas and paints 4 colored boxes of size 1/10th the
    dimensions at each corner using NumPy array slicing.
    """
    # Create white canvas (3-dimensional array: height x width x 3 channels)
    # Using np.ones in 3 dimensions and scaling to 255
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Compute box dimensions (1/10th of the image dimensions)
    box_h = max(1, int(height / 10))
    box_w = max(1, int(width / 10))

    print(f"Image dimensions : {width} x {height}")
    print(f"Corner box size  : {box_w} x {box_h} (1/10th)")

    # 1. Top-Left: Black [0, 0, 0]
    image[0:box_h, 0:box_w] = [0, 0, 0]

    # 2. Top-Right: Blue [255, 0, 0] (BGR order)
    image[0:box_h, width - box_w:width] = [255, 0, 0]

    # 3. Bottom-Left: Green [0, 255, 0]
    image[height - box_h:height, 0:box_w] = [0, 255, 0]

    # 4. Bottom-Right: Red [0, 0, 255]
    image[height - box_h:height, width - box_w:width] = [0, 0, 255]

    return image

# Prompt user for image size
height, width = 500, 500
try:
    h_in = input("Enter image height (default 500): ").strip()
    if h_in:
        height = max(50, int(h_in))
    w_in = input("Enter image width  (default 500): ").strip()
    if w_in:
        width = max(50, int(w_in))
except (ValueError, EOFError):
    print(f"Using default size: {width}x{height}")

result = create_four_corner_boxes(height, width)

cv2.imshow("White Image with 4 Colored Corner Boxes", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp32_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")

