"""
CSV logger for sessions. Each row = timestamp, gesture, features...
"""
import csv
import time
from typing import Optional, Dict

class SessionLogger:
    def __init__(self, path: str = "session_log.csv"):
        self.path = path
        self.fp = open(self.path, "a", newline="", encoding="utf-8")
        self.writer = csv.writer(self.fp)
        self._wrote_header = False
        self._write_header()

    def _write_header(self):
        if not self._wrote_header:
            self.writer.writerow(["ts", "gesture", "flex_avg", "pinch_mm"])
            self._wrote_header = True

    def log(self, gesture: str, flex_avg: float, pinch_mm: float, extra: Optional[Dict]=None):
        ts = f"{time.time():.3f}"
        self.writer.writerow([ts, gesture, f"{flex_avg:.3f}", f"{pinch_mm:.1f}"])
        if extra:
            pass

    def close(self):
        try:
            self.fp.close()
        except Exception:
            pass
