"""
Experiment 39: Play Video in Reverse Mode in Slow Motion
=========================================================
Write a Python function to play the given video in reverse mode
in slow motion.

This experiment reads video frames, stores them in memory, reverses their
order, and displays them with an increased frame-delay (e.g. 100 ms instead
of the standard ~33 ms) to achieve a smooth slow-motion effect while playing
backwards. It also writes the processed video to an output file.

Input : 220268_medium.mp4  (placed in the same folder as this script)
Output: Reverse slow-motion video playback and saved as exp39_output_slow_reverse.avi
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
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"Original Video: {width}x{height} @ {fps:.1f} FPS, Total Frames: {total_frames}")

# Capture frames (limit to 250 frames for interactive smoothness)
frames = []
max_frames = min(total_frames, 250)

print(f"Reading {max_frames} frames into buffer...")
for i in range(max_frames):
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()
print("Reversing frame sequence...")
reversed_frames = frames[::-1]

# Slow-motion target FPS (half or one-third of original FPS)
slow_fps = max(5.0, (fps / 2.5) if fps > 0 else 10.0)
slow_delay_ms = int(1000 / slow_fps)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exp39_output_slow_reverse.avi")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(out_path, fourcc, slow_fps, (width, height))

print(f"Playing in Reverse Slow Motion at {slow_fps:.1f} FPS (Delay: {slow_delay_ms} ms)...")
print("Press 'q' to stop playback early.")

for idx, frame in enumerate(reversed_frames):
    out.write(frame)

    display_frame = frame.copy()
    cv2.putText(display_frame, f"REVERSE SLOW MOTION: Frame {idx + 1}/{len(reversed_frames)}",
                (30, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 165, 255), 2)
    cv2.putText(display_frame, f"Speed: {slow_fps:.1f} FPS",
                (30, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Reverse Slow-Motion Playback", display_frame)

    if cv2.waitKey(slow_delay_ms) & 0xFF == ord('q'):
        print("Playback interrupted by user.")
        break

out.release()
cv2.destroyAllWindows()
print(f"Reversed slow-motion video saved to: {out_path}")

