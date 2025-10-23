"""
End-to-end demo that ties everything together.
Simulates sensor values; swap simulation with real feed later.
"""
import time
import random
import numpy as np
import cv2

from calibration import compute_baseline, normalize
from gesture_recognition import FrameFeatures, classify
from effects_light import repulsor_charge, repulsor_blast, steady_idle
from effects_audio import beep, voice_cue
from data_logging import SessionLogger
from ui_dashboard import render
import vr_interface

def simulate_sensor_stream(n=120):
    """yield fake (flex, pinch_mm) pairs"""
    for _ in range(n):
        flex = random.uniform(0.0, 1.0)
        pinch = random.uniform(10.0, 40.0)
        yield flex, pinch
        time.sleep(0.03)

def main():
    baseline_samples = [random.uniform(0.35, 0.45) for _ in range(60)]
    mean, std = compute_baseline(baseline_samples)

    logger = SessionLogger()
    vr_interface.connect()
    voice_cue("Iron Man hand online.")

    cap = cv2.VideoCapture(0)  # try webcam for overlay (optional)

    try:
        steady_idle(0.2)
        for flex_raw, pinch_mm in simulate_sensor_stream(300):
            flex_norm = normalize(flex_raw, mean, std)
            features = FrameFeatures(flex_avg=flex_norm, pinch_distance_mm=pinch_mm)
            g = classify(features)

            if g == "FIST":
                repulsor_charge(0.25); beep(1)
            elif g == "PINCH":
                repulsor_blast(2); beep(2)
            else:
                steady_idle(0.15)

            vr_interface.send({"gesture": g, "flex": round(flex_norm, 3), "pinch_mm": round(pinch_mm,1)})
            logger.log(g, flex_norm, pinch_mm)

            ret, frame = cap.read()
            if not ret:
                frame = np.zeros((360, 640, 3), dtype=np.uint8)
            frame = render(frame, g, flex_norm)
            cv2.imshow("IronMan Hand – Live View", frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
                break

    finally:
        logger.close()
        vr_interface.close()
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
