"""
Experiment 40: Extract Text from Videos
========================================
Write a Python function to extract the text from videos.

This experiment extracts text regions and textual content appearing in
video frames. It samples frames at intervals, applies preprocessing
(grayscale conversion, adaptive thresholding, and morphological dilation),
detects text candidate bounding boxes, and performs OCR extraction using
Tesseract (via pytesseract) if available, with a native OpenCV bounding-box
text region detector fallback.

Input : 220268_medium.mp4  (placed in the same folder as this script)
Output: Annotated video frames with detected text bounding boxes and extracted text log
"""

import cv2
import numpy as np
import sys
import os

video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "220268_medium.mp4")

if not os.path.exists(video_path):
    print(f"[ERROR] Video file not found: {video_path}")
    print("Please place '220268_medium.mp4' in the same folder as this script.")
    sys.exit(1)

# Check if pytesseract is available
try:
    import pytesseract
    has_tesseract = True
    print("[INFO] pytesseract library found.")
except ImportError:
    has_tesseract = False
    print("[INFO] pytesseract not installed. Using native OpenCV text region localization.")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("[ERROR] Cannot open video file.")
    sys.exit(1)

fps = cap.get(cv2.CAP_PROP_FPS)
fps = fps if fps > 0 else 25.0
sample_interval = int(fps * 2)   # Sample 1 frame every 2 seconds

frame_idx = 0
extracted_results = []
keyframe_saved = None

print("Processing video frames for text detection... (Press 'q' to stop)")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_idx += 1

    # Process only sampled frames
    if frame_idx % sample_interval == 0:
        timestamp_sec = frame_idx / fps
        display_frame = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Preprocessing: morphological gradient to highlight text edges
        morph_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        grad = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, morph_kernel)

        # Binarize with Otsu
        _, binary = cv2.threshold(grad, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Connect text characters horizontally
        text_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
        connected = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, text_kernel)

        contours, _ = cv2.findContours(connected, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        frame_texts = []
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            aspect_ratio = w / float(h)

            # Filter candidate text bounding boxes (typical text line proportions)
            if w > 25 and h > 10 and aspect_ratio > 1.2 and w < frame.shape[1] * 0.9:
                roi = gray[y:y + h, x:x + w]
                text_content = ""

                if has_tesseract:
                    try:
                        text_content = pytesseract.image_to_string(
                            roi, config='--psm 7 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
                        ).strip()
                    except Exception:
                        pass

                # Draw bounding box
                cv2.rectangle(display_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if text_content:
                    frame_texts.append(text_content)
                    cv2.putText(display_frame, text_content, (x, y - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

        info = f"Time: {timestamp_sec:.1f}s | Boxes: {len(contours)}"
        cv2.putText(display_frame, info, (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if frame_texts:
            print(f"[{timestamp_sec:.1f}s] Extracted text: {', '.join(frame_texts)}")
            extracted_results.extend(frame_texts)
        else:
            print(f"[{timestamp_sec:.1f}s] Detected {len(contours)} potential text candidate regions.")

        if keyframe_saved is None:
            keyframe_saved = display_frame.copy()

        cv2.imshow("Video Text Extraction", display_frame)
        if cv2.waitKey(200) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

if keyframe_saved is not None:
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp40_output.jpg")
    cv2.imwrite(out, keyframe_saved)
    print(f"Keyframe saved: {out}")

print("\n" + "=" * 50)
print(f"Total Text Elements Extracted from Video: {len(extracted_results)}")
if extracted_results:
    for idx, t in enumerate(extracted_results, 1):
        print(f"  {idx}. {t}")
print("=" * 50)

