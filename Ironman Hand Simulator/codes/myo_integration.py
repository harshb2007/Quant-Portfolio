# Myo Integration Stub
# Replace this with your Myo SDK event loop.
# Expose two callbacks: on_charge_start() and on_fire().

def on_charge_start():
    # e.g., hand open detected
    pass

def on_fire():
    # e.g., quick wrist flick detected
    pass

# Wire these into repulsor_game by sending synthetic
# MOUSEBUTTONDOWN/UP events or by setting shared flags.
