"""
Global configuration for Ironman Hand Simulator.
Edit thresholds/ports once and import everywhere.
"""
from dataclasses import dataclass

@dataclass
class SerialConfig:
    port: str = "COM3"          # e.g., "COM3" on Windows or "/dev/ttyUSB0" on Linux
    baudrate: int = 115200
    timeout: float = 0.1

@dataclass
class GestureThresholds:
    fist: float = 0.75          # 0..1 flex value
    open_hand: float = 0.20
    pinch_gap_mm: float = 20.0  # distance threshold in mm

@dataclass
class VisualConfig:
    show_landmarks: bool = True
    window_title: str = "IronMan Hand – Live View"

SERIAL = SerialConfig()
GESTURE = GestureThresholds()
VIS = VisualConfig()
