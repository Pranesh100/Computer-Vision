"""
Experiment 18: Image Cropping, Copying and Pasting (ROI)
==========================================================
Implement image cropping, copying and pasting to select a Region of
Interest (ROI) from the source image using OpenCV.

The user is prompted to enter ROI coordinates interactively.

Input : image 1.jpg  (placed in the same folder as this script)
Output: Cropped ROI and image with pasted ROI displayed; saved as exp18_output.jpg
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
h, w  = image.shape[:2]
print(f"Image size: width={w}, height={h}")
print()

# Get ROI coordinates from user
try:
    print("Enter the Region of Interest (ROI) coordinates:")
    y1 = int(input(f"  Start row  (0 to {h-1}): "))
    y2 = int(input(f"  End   row  ({y1+1} to {h}): "))
    x1 = int(input(f"  Start col  (0 to {w-1}): "))
    x2 = int(input(f"  End   col  ({x1+1} to {w}): "))
except ValueError:
    print("[ERROR] Please enter integer values.")
    sys.exit(1)

# Clamp to image bounds
y1, y2 = max(0, y1), min(h, y2)
x1, x2 = max(0, x1), min(w, x2)

if y2 <= y1 or x2 <= x1:
    print("[ERROR] Invalid ROI: end must be greater than start.")
    sys.exit(1)

# Crop the ROI
roi = image[y1:y2, x1:x2].copy()
print(f"ROI cropped: rows {y1}-{y2}, cols {x1}-{x2}");
print(f"ROI size: {roi.shape}");

# Paste ROI at a different location (offset by 30 pixels)
roi_h = y2 - y1;
roi_w = x2 - x1;
result = image.copy();

dst_y1 = min(y1 + 30, h - roi_h);
dst_x1 = min(x1 + 30, w - roi_w);
dst_y2 = dst_y1 + roi_h;
dst_x2 = dst_x1 + roi_w;

result[dst_y1:dst_y2, dst_x1:dst_x2] = roi;
print(f"ROI pasted at: rows {dst_y1}-{dst_y2}, cols {dst_x1}-{dst_x2}");

cv2.imshow("Original Image", image);
cv2.imshow("Cropped ROI", roi);
cv2.imshow("Image with Pasted ROI", result);
print("Press any key to close windows...");
cv2.waitKey(0);
cv2.destroyAllWindows();
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp18_output.jpg");
cv2.imwrite(out, result);
print(f"Saved: {out}"); 
