"""
Experiment 17: Image Watermarking
===================================
Design and implement a watermarking technique to insert a watermark
into the original image effectively using OpenCV.

A semi-transparent text watermark is overlaid on the image using
cv2.putText with alpha blending via cv2.addWeighted.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Watermarked image displayed and saved as exp17_output.jpg
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
h, w  = image.shape[:2]

# Watermark settings
text       = "WATERMARK"
font       = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
thickness  = 5
color      = (0, 255, 255)   # Yellow (BGR)
alpha      = 0.4             # Watermark opacity (0=invisible, 1=fully opaque)

# Get text dimensions to centre it on the image
(text_w, text_h), _ = cv2.getTextSize(text, font, font_scale, thickness)
x = (w - text_w) // 2
y = (h + text_h) // 2

# Draw text on a copy, then blend with original
overlay = image.copy()
cv2.putText(overlay, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)
result = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)

print(f"Watermark '{text}' added at position ({x}, {y})")

cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp17_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")
