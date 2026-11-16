"""
Experiment 37: Foreground Subtraction based on Color Levels
============================================================
Write a Python function to subtract the foreground of the given input
image based on color levels using OpenCV.

This experiment identifies and segments foreground objects based on their
color intensity levels in the HSV color space, creating a foreground mask.
The foreground is then subtracted (removed) from the scene, preserving
only the background or replacing the foreground with background color.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Foreground subtracted image displayed and saved as exp37_output.jpg
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

# Compute central region color characteristics to isolate central foreground
h, w = image.shape[:2]
center_patch = hsv[int(h * 0.3):int(h * 0.7), int(w * 0.3):int(w * 0.7)]
fg_mean = np.mean(center_patch.reshape(-1, 3), axis=0)

# Define color range for the foreground object
tolerance = 45
lower_fg = np.array([max(0, int(fg_mean[0] - tolerance)),
                     max(0, int(fg_mean[1] - tolerance)),
                     max(0, int(fg_mean[2] - tolerance))])
upper_fg = np.array([min(180, int(fg_mean[0] + tolerance)),
                     min(255, int(fg_mean[1] + tolerance)),
                     min(255, int(fg_mean[2] + tolerance))])

# Create binary foreground mask
fg_mask = cv2.inRange(hsv, lower_fg, upper_fg)

# Clean mask with morphological operations
kernel = np.ones((5, 5), np.uint8)
fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_CLOSE, kernel)
fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

# Invert mask to retain only background pixels
bg_mask = cv2.bitwise_not(fg_mask)

# Method 1: Foreground removed with black fill
bg_only = cv2.bitwise_and(image, image, mask=bg_mask)

# Method 2: Foreground subtracted using inpainting to seamlessly fill background
inpaint_result = cv2.inpaint(image, fg_mask, inpaintRadius=5, flags=cv2.INPAINT_TELEA)

print("Foreground Subtraction complete.")
print(f"Foreground pixels removed: {np.count_nonzero(fg_mask)}")

cv2.imshow("Original Image", image)
cv2.imshow("Foreground Mask (Object to Subtract)", fg_mask)
cv2.imshow("Foreground Subtracted (Masked)", bg_only)
cv2.imshow("Foreground Subtracted (Inpainted)", inpaint_result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp37_output.jpg")
cv2.imwrite(out, bg_only)
print(f"Saved: {out}")

