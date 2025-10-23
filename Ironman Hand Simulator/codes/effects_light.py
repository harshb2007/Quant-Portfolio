"""
LED / light patterns for IronMan visuals.
Replace stubs with your microcontroller or LED strip API calls.
"""
import time

def repulsor_charge(duration_s: float = 1.0):
    """Ramp brightness up (charging effect)."""
    steps = 20
    for i in range(steps + 1):
        level = i / steps
        _set_brightness(level)
        time.sleep(duration_s / steps)
    _set_brightness(1.0)

def repulsor_blast(pulses: int = 3):
    """Short bright pulses."""
    for _ in range(pulses):
        _set_brightness(1.0)
        time.sleep(0.08)
        _set_brightness(0.15)
        time.sleep(0.08)

def steady_idle(level: float = 0.2):
    _set_brightness(level)

# ---- hardware binding (stub) ----
def _set_brightness(level: float):
    # TODO: connect to LED driver or microcontroller (e.g., via serial/i2c)
    print(f"[LIGHT] brightness={level:.2f}")
