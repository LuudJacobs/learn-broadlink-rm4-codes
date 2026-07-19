"""Small shared helpers for learning IR/RF codes with a Broadlink RM4 Pro."""

import time

import broadlink


def connect(ip: str):
    """Connect directly to a known IP address (no discovery needed)."""
    dev = broadlink.hello(ip)
    dev.auth()
    return dev


def wait_for_data(dev, attempts: int = 20, delay: float = 0.5):
    """Poll check_data() until a packet arrives, or return None."""
    for _ in range(attempts):
        try:
            packet = dev.check_data()
            return packet.hex()
        except Exception:
            time.sleep(delay)
    return None


def learn_ir(dev, attempts: int = 20, delay: float = 0.5):
    """Learn an IR code (single step: just press the button right away)."""
    dev.enter_learning()
    return wait_for_data(dev, attempts, delay)


def learn_rf(dev, frequency: float = 433.92, attempts: int = 20, delay: float = 0.5):
    """Learn an RF code. Frequency is known in advance, so no sweep phase is needed."""
    dev.find_rf_packet(frequency=frequency)
    return wait_for_data(dev, attempts, delay)
