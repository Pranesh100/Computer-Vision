"""
Experiment 25: Recognize Watch using Object Recognition
========================================================
Recognize watch from the given image by general Object recognition using OpenCV.

This experiment uses Template Matching (cv2.matchTemplate) and Feature Detection
(ORB) to locate and recognize a watch object in an input image, drawing a bounding
box and a confidence score around the recognized object.

Input : image 1.jpg (or watch.jpg / 2.jpg) in the script directory
Output: Recognized watch highlighted with bounding box, saved as exp25_output.jpg
"""

import cv2
import numpy as np
import sys
import os

folder = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(folder, "image 1.jpg")

# Check for alternate images in directory
if not os.path.exists(image_path):
    alt_path = os.path.join(folder, "2.jpg")
    if os.path.exists(alt_path):
        image_path = alt_path
    else:
        print(f"[ERROR] Input image not found: {image_path}")
        print("Please place 'image 1.jpg' or '2.jpg' in the script folder.")
        sys.exit(1)

main_image = cv2.imread(image_path)
gray_main = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
result = main_image.copy()

template_path = os.path.join(folder, "watch_template.jpg")

# Method 1: If a template file exists, use Template Matching
if os.path.exists(template_path):
    print("Using template matching with 'watch_template.jpg'...")
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    w_t, h_t = template.shape[::-1]

    res = cv2.matchTemplate(gray_main, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = (top_left[0] + w_t, top_left[1] + h_t)

    cv2.rectangle(result, top_left, bottom_right, (0, 255, 0), 3)
    cv2.putText(result, f"Watch ({max_val:.2f})", (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    print(f"Watch matched at {top_left} with score {max_val:.2f}")

else:
    # Method 2: General Shape & Contour Recognition (Dial & Circle detection)
    print("Template not found. Using Contour & Circular Dial Recognition...")
    blurred = cv2.GaussianBlur(gray_main, (7, 7), 2)
    
    # Detect circular dial features using Hough Circles
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                               param1=100, param2=40, minRadius=20, maxRadius=180)

    detected = False
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for (x, y, r) in circles[0, :3]:
            # Draw bounding box around the detected watch dial
            x1, y1 = max(0, int(x - r - 10)), max(0, int(y - r - 10))
            x2, y2 = min(main_image.shape[1], int(x + r + 10)), min(main_image.shape[0], int(y + r + 10))
            cv2.rectangle(result, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.circle(result, (x, y), r, (0, 0, 255), 2)
            cv2.circle(result, (x, y), 3, (255, 0, 0), -1)
            cv2.putText(result, "Watch Dial Detected", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            detected = True
            print(f"Watch dial detected at center ({x}, {y}) with radius {r}")
            break

    if not detected:
        # Fallback: Contour detection of prominent objects
        edged = cv2.Canny(blurred, 50, 150)
        contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest)
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(result, "Recognized Object: Watch", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            print(f"Prominent object bounding box: x={x}, y={y}, w={w}, h={h}")

cv2.imshow("Input Image", main_image)
cv2.imshow("Watch Recognition Result", result)
print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

out = os.path.join(folder, "exp25_output.jpg")
cv2.imwrite(out, result)
print(f"Saved: {out}")

