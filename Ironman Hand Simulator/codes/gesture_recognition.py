"""
Rule-based gesture recognition for fist / open-hand / pinch.
Plug in your data source to classify frames into discrete gestures.
"""
from dataclasses import dataclass
from typing import Literal, Dict
from config import GESTURE

Gesture = Literal["FIST", "OPEN_HAND", "PINCH", "UNKNOWN"]

@dataclass
class FrameFeatures:
    flex_avg: float           # 0..1 (higher = more closed)
    pinch_distance_mm: float  # distance between thumb & index tips

def classify(features: FrameFeatures) -> Gesture:
    if features.flex_avg >= GESTURE.fist:
        return "FIST"
    if features.flex_avg <= GESTURE.open_hand:
        return "OPEN_HAND"
    if features.pinch_distance_mm <= GESTURE.pinch_gap_mm:
        return "PINCH"
    return "UNKNOWN"

def one_hot(gesture: Gesture) -> Dict[str, int]:
    keys = ["FIST", "OPEN_HAND", "PINCH", "UNKNOWN"]
    return {k: int(k == gesture) for k in keys}
