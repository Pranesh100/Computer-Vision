"""
Experiment 36: Background Subtraction based on Color Levels
============================================================
Write a Python function to subtract the background of the given input
image based on color levels using OpenCV.

This experiment converts the image to the HSV (Hue, Saturation, Value)
color space, determines color ranges corresponding to the background
(e.g., green screen or dominant background hue), creates a binary mask
using cv2.inRange, and isolates the foreground object by removing the
background.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Background mask and extracted foreground displayed; saved as exp36_output.jpg
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
hsv   = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Sample background color from corners to automatically set background range
corner_pixels = np.vstack([
    hsv[0:10, 0:10].reshape(-1, 3),
    hsv[0:10, -10:].reshape(-1, 3),
    hsv[-10:, 0:10].reshape(-1, 3),
    hsv[-10:, -10:].reshape(-1, 3)
])
bg_mean = np.mean(corner_pixels, axis=0)
bg_std  = np.std(corner_pixels, axis=0)

# Set lower and upper HSV color bounds for background
tolerance = 40
lower_bg = np.array([max(0, int(bg_mean[0] - tolerance)),
                     max(0, int(bg_mean[1] - tolerance)),
                     max(0, int(bg_mean[2] - tolerance))])
upper_bg = np.array([min(180, int(bg_mean[0] + tolerance)),
                     min(255, int(bg_mean[1] + tolerance)),
                     min(255, int(bg_mean[2] + tolerance))])

print(f"Estimated Background HSV range:")
print(f"  Lower: {lower_bg}")
print(f"  Upper: {upper_bg}")

# Create background mask
bg_mask = cv2.inRange(hsv, lower_bg, upper_bg)

# Invert mask to get foreground mask (where background is removed)
fg_mask = cv2.bitwise_not(bg_mask)

# Clean mask with morphological operations
kernel = np.ones((5, 5), np.uint8)
fg_mask_clean = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
fg_mask_clean = cv2.morphologyEx(fg_mask_clean, cv2.MORPH_DILATE, kernel)

# Apply mask to extract foreground (background becomes black)
foreground_only = cv2.bitwise_and(image, image, mask=fg_mask_clean)

# Also create a version with clean white background
white_bg = np.ones_like(image) * 255
white_bg_result = np.where(fg_mask_clean[:, :, None] == 255, image, white_bg)

cv2.imshow("Original Image", image)
cv2.imshow("Background Mask (White = Background)", bg_mask)
cv2.imshow("Foreground Mask (White = Keep)", fg_mask_clean)
cv2.imshow("Foreground Extracted (Black BG)", foreground_only)
cv2.imshow("Foreground on White BG", white_bg_result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp36_output.jpg")
cv2.imwrite(out, foreground_only)
print(f"Saved: {out}")

