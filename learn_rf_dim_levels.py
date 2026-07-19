"""Interactively learn RF dim levels of a dimmer (via its companion app/hub)
and save them to rf_dim-level_codes.json."""

import json
import time

from broadlink_helpers import connect, learn_rf

OUTPUT_FILE = "rf_dim-level_codes.json"


def prompt_level_count():
    while True:
        raw = input("Number of dim levels: ").strip()
        if not raw:
            print("Number of dim levels is required.")
            continue
        try:
            count = int(raw)
        except ValueError:
            print("Enter a whole number, e.g. 16.")
            continue
        if count < 2:
            print("Need at least 2 dim levels.")
            continue
        return count


def prompt_ip():
    ip = input("Broadlink RM IP address: ").strip()
    while not ip:
        ip = input("IP address is required. Broadlink RM IP address: ").strip()
    return ip


def prompt_frequency():
    while True:
        raw = input("Frequency in MHz (e.g. 433.92): ").strip()
        if not raw:
            print("Frequency is required.")
            continue
        try:
            return float(raw)
        except ValueError:
            print("Enter a number, e.g. 433.92.")


def countdown():
    for n in (3, 2, 1):
        print(n)
        time.sleep(1)


def learn_level(dev, frequency, name, pct):
    while True:
        countdown()
        print(f"Listening now - set the slider in the app to {pct}% and release it...")
        code = learn_rf(dev, frequency=frequency)

        if code:
            print(f"✓ Learned '{name}': {code}")
            return code

        print(f"✗ Nothing captured for '{name}'.")
        choice = input("Press Enter to try again, or 'q' to quit and save... ").strip().lower()
        if choice == "q":
            return None


def main():
    level_count = prompt_level_count()
    ip = prompt_ip()
    frequency = prompt_frequency()
    dev = connect(ip)
    results = {}

    for level in range(level_count):
        pct = round(level * 100 / (level_count - 1))
        name = f"level-{pct}"

        code = learn_level(dev, frequency, name, pct)
        if code is None:
            break
        results[name] = code

        if level < level_count - 1:
            choice = input("Press Enter to continue to the next level, or 'q' to quit and save... ").strip().lower()
            if choice == "q":
                break

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nSaved {len(results)} code(s) to {OUTPUT_FILE}:")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
