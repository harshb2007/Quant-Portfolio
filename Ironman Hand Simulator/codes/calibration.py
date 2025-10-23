"""
Simple calibration: captures baseline sensor noise and normalizes 0..1.
"""
import numpy as np
from typing import Tuple

def compute_baseline(samples) -> Tuple[float, float]:
    """
    samples: iterable of raw sensor values
    returns (mean, std) to normalize incoming data.
    """
    arr = np.asarray(list(samples), dtype=float)
    mean = float(arr.mean()) if arr.size else 0.0
    std = float(arr.std()) if arr.size else 1.0
    std = std or 1.0
    return mean, std

def normalize(value: float, mean: float, std: float) -> float:
    """z-score then squash to 0..1 via sigmoid-ish clamp."""
    z = (value - mean) / (std or 1.0)
    x = 1 / (1 + np.exp(-z))
    return float(np.clip(x, 0.0, 1.0))
