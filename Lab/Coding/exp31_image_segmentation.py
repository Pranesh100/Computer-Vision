"""
Experiment 31: Image Segmentation based on Thresholding
=========================================================
Implement a Segmentation algorithm using OpenCV to segment the given
input image based on the given threshold values.

Image thresholding converts a grayscale image into a binary image,
separating the foreground (objects of interest) from the background.
This script demonstrates:
1. Binary Thresholding
2. Inverse Binary Thresholding
3. Truncated Thresholding
4. To-Zero Thresholding
5. Otsu's Optimal Bimodal Thresholding

Input : image 1.jpg  (placed in the same folder as this script)
Output: Segmented thresholded images displayed; saved as exp31_output.jpg
"""

import cv2
import sys
import os

image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image 1.jpg")

if not os.path.exists(image_path):
    print(f"[ERROR] Image not found: {image_path}")
    print("Please place 'image 1.jpg' in the same folder as this script.")
    sys.exit(1)

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Prompt user for threshold value with a safe default
thresh_val = 127
try:
    user_input = input("Enter threshold value (0-255, default 127): ").strip()
    if user_input:
        thresh_val = int(user_input)
        thresh_val = max(0, min(255, thresh_val))
except (ValueError, EOFError):
    print(f"Using default threshold value: {thresh_val}")

print(f"Applying segmentation with threshold = {thresh_val}...")

# 1. Binary Thresholding
_, thresh_binary = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)

# 2. Binary Inverse
_, thresh_binary_inv = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY_INV)

# 3. Truncate
_, thresh_trunc = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_TRUNC)

# 4. To Zero
_, thresh_tozero = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_TOZERO)

# 5. Otsu's Thresholding (automatic optimal threshold)
otsu_thresh, thresh_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(f"Otsu's calculated optimal threshold: {otsu_thresh:.2f}")

cv2.imshow("Original Grayscale", gray)
cv2.imshow(f"Binary Threshold ({thresh_val})", thresh_binary)
cv2.imshow("Binary Inverse", thresh_binary_inv)
cv2.imshow("Truncate", thresh_trunc)
cv2.imshow(f"Otsu Threshold ({otsu_thresh:.1f})", thresh_otsu)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp31_output.jpg")
cv2.imwrite(out, thresh_otsu)
print(f"Saved Otsu segmented image to: {out}")

