"""
Experiment 34: Create White Image and Draw Circle
==================================================
Write a Python function to create a white image size entered by the user
and then create a shape of Circle using OpenCV.

Input : User enters image size (height, width)
Output: Image containing drawn circle displayed and saved as exp34_output.jpg
"""

import cv2
import numpy as np
import os
import sys

def draw_circle_on_white_image(height=500, width=600):
    """
    Creates a white canvas of specified size and draws a centered circle.
    """
    # Create pure white image (3 channels BGR)
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Center of circle and radius
    center = (int(width / 2), int(height / 2))
    radius = int(min(height, width) * 0.3)

    color = (255, 0, 0)       # Blue color in BGR
    thickness = 3             # Boundary line thickness (use -1 for solid fill)

    # Draw the circle
    cv2.circle(image, center, radius, color, thickness)
    # Draw center dot
    cv2.circle(image, center, 4, (0, 0, 255), -1)

    # Add label
    cv2.putText(image, f"Circle (Center={center}, Radius={radius})",
                (int(width * 0.1), 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    print(f"Canvas Size: {width} x {height}")
    print(f"Circle drawn at Center {center} with Radius {radius}")
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

result = draw_circle_on_white_image(height, width)

cv2.imshow("Circle on White Image", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp34_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")

