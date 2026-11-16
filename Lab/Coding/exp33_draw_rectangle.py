"""
Experiment 33: Create White Image and Draw Rectangle
=====================================================
Write a Python function to create a white image size entered by the user
and then create a shape of Rectangle using OpenCV.

Input : User enters image size (height, width)
Output: Image containing drawn rectangle displayed and saved as exp33_output.jpg
"""

import cv2
import numpy as np
import os
import sys

def draw_rectangle_on_white_image(height=500, width=600):
    """
    Creates a white canvas of specified size and draws a centered rectangle.
    """
    # Create pure white image (3 channels BGR)
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Define rectangle coordinates (centered with margin)
    start_point = (int(width * 0.2), int(height * 0.25))
    end_point   = (int(width * 0.8), int(height * 0.75))

    color = (0, 0, 255)       # Red color in BGR
    thickness = 3             # Boundary line thickness (use -1 to fill)

    # Draw the rectangle
    cv2.rectangle(image, start_point, end_point, color, thickness)

    # Add label
    cv2.putText(image, "Rectangle Shape", (start_point[0], start_point[1] - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    print(f"Canvas Size: {width} x {height}")
    print(f"Rectangle from {start_point} to {end_point}")
    return image

# Prompt user for dimensions
height, width = 500, 600
try:
    h_in = input("Enter image height (default 500): ").strip()
    if h_in:
        height = max(100, int(h_in))
    w_in = input("Enter image width  (default 600): ").strip()
    if w_in:
        width = max(100, int(w_in))
except (ValueError, EOFError):
    print(f"Using default dimensions: {width} x {height}")

result = draw_rectangle_on_white_image(height, width)

cv2.imshow("Rectangle on White Image", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp33_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")

