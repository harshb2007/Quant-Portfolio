"""
Minimal live dashboard using cv2 (text overlay).
Shows current gesture + bars.
"""
import cv2
import numpy as np

def render(frame: np.ndarray, gesture: str, flex_avg: float):
    h, w = frame.shape[:2]
    bar_w = int(max(1, w * 0.3))
    bar_h = 16
    x, y = 20, 20

    cv2.rectangle(frame, (x, y), (x + bar_w, y + bar_h), (60, 60, 60), -1)
    fill_w = int(bar_w * np.clip(flex_avg, 0, 1))
    cv2.rectangle(frame, (x, y), (x + fill_w, y + bar_h), (0, 200, 255), -1)

    cv2.putText(frame, f"Gesture: {gesture}", (x, y + 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
    return frame
