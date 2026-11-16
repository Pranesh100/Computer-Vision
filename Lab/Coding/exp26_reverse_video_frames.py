"""
Experiment 26: Reverse Frames of Video
========================================
Implement a function to reverse the frames of the video to create
a video in reverse mode using OpenCV.

This experiment reads all frames from an input video, reverses their order,
plays the reversed video in a window, and saves the reversed video file.

Input : 220268_medium.mp4  (placed in the same folder as this script)
Output: Video played in reverse and saved as exp26_reversed_video.avi
"""

import cv2
import sys
import os

video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "220268_medium.mp4")

if not os.path.exists(video_path):
    print(f"[ERROR] Video file not found: {video_path}")
    print("Please place '220268_medium.mp4' in the same folder as this script.")
    sys.exit(1)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("[ERROR] Cannot open video file.")
    sys.exit(1)

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"Reading video: {width}x{height} @ {fps:.2f} FPS | Total frames: {total_frames}")

# Read and store frames (limit to 300 frames if video is long to conserve memory)
max_frames = min(total_frames, 300)
frames = []

for i in range(max_frames):
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()
print(f"Captured {len(frames)} frames. Reversing frame sequence...")

# Reverse the list of frames
reversed_frames = frames[::-1]

# Setup VideoWriter to save reversed video
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp26_reversed_video.avi")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(out_path, fourcc, fps if fps > 0 else 24.0, (width, height))

print("Playing and saving reversed video... (Press 'q' to stop)")
for idx, frame in enumerate(reversed_frames):
    out.write(frame)
    
    # Display frame counter on screen
    display_frame = frame.copy()
    cv2.putText(display_frame, f"Reversed Frame: {idx+1}/{len(reversed_frames)}", (30, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    
    cv2.imshow("Reverse Video Mode", display_frame)
    if cv2.waitKey(int(1000 / (fps if fps > 0 else 24))) & 0xFF == ord('q'):
        print("Playback stopped by user.")
        break

out.release()
cv2.destroyAllWindows()
print(f"Reversed video successfully saved to: {out_path}")

