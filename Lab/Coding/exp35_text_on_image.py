"""
Experiment 35: Put User-Entered Text on Image
==============================================
Write a Python function to create a text string entered by the user
that must be appeared on the given image using OpenCV.

Input : Text string entered by the user, and image 1.jpg
Output: Image with formatted text overlay displayed and saved as exp35_output.jpg
"""

import cv2
import numpy as np
import os
import sys

image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image 1.jpg")

if os.path.exists(image_path):
    image = cv2.imread(image_path)
else:
    print("[INFO] 'image 1.jpg' not found. Creating a solid background canvas.")
    image = np.ones((500, 800, 3), dtype=np.uint8) * 240

# Get text string from user
user_text = "Computer Vision Lab Experiment 35"
try:
    text_in = input("Enter text string to overlay on image: ").strip()
    if text_in:
        user_text = text_in
except (EOFError, KeyboardInterrupt):
    pass

result = image.copy()
h, w = result.shape[:2]

# Text configuration
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.0
thickness = 2
text_color = (0, 255, 255)   # Yellow in BGR
outline_color = (0, 0, 0)    # Black outline for crisp readability

# Calculate text size and position (centered near bottom)
(text_w, text_h), baseline = cv2.getTextSize(user_text, font, font_scale, thickness)
text_x = max(20, int((w - text_w) / 2))
text_y = int(h * 0.85)

# Draw dark background banner behind text
cv2.rectangle(result, (text_x - 15, text_y - text_h - 15),
              (text_x + text_w + 15, text_y + baseline + 10), (40, 40, 40), -1)

# Draw outline and then text
cv2.putText(result, user_text, (text_x, text_y), font, font_scale, outline_color, thickness + 2, cv2.LINE_AA)
cv2.putText(result, user_text, (text_x, text_y), font, font_scale, text_color, thickness, cv2.LINE_AA)

print(f"Overlaying text: '{user_text}' at ({text_x}, {text_y})")

cv2.imshow("Original Image", image)
cv2.imshow("Text on Image Result", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp35_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")

