"""
Simple audio feedback (beeps / cues). Cross-platform friendly.
"""
import sys
import time

def beep(times: int = 1):
    for _ in range(times):
        _beep_once()
        time.sleep(0.1)

def voice_cue(text: str):
    """Optional TTS via pyttsx3 if available."""
    try:
        import pyttsx3
        tts = pyttsx3.init()
        tts.say(text)
        tts.runAndWait()
    except Exception:
        print(f"[AUDIO] {text}")

def _beep_once():
    if sys.platform.startswith("win"):
        try:
            import winsound
            winsound.Beep(1200, 120)
        except Exception:
            print("\a", end="")
    else:
        print("\a", end="")
