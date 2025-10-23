"""
Abstraction layer to send gestures/states to a VR/engine client.
Replace send() with WebSocket/UDP/OSC as needed.
"""
from typing import Dict

def connect():
    print("[VR] connected (stub)." )

def send(state: Dict):
    print(f"[VR] {state}")

def close():
    print("[VR] closed (stub)." )
