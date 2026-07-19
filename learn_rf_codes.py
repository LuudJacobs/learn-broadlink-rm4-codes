"""Interactively learn RF codes button-by-button and save them to rf_codes.json."""

import json
import re
import time

from broadlink_helpers import connect, learn_rf

OUTPUT_FILE = "rf_codes.json"
NAME_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")


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


def prompt_button_name(existing):
    while True:
        name = input("\nName of the button to learn: ").strip()
        if not name:
            print("Name can't be empty.")
        elif not NAME_PATTERN.match(name):
            print("Use only letters, digits, underscores and dashes.")
        elif name in existing:
            print(f"'{name}' has already been learned, choose a different name.")
        else:
            return name


def countdown():
    for n in (3, 2, 1):
        print(n)
        time.sleep(1)


def learn_button(dev, frequency, name):
    while True:
        countdown()
        print(f"Listening now - press '{name}' on the remote...")
        code = learn_rf(dev, frequency=frequency)

        if code:
            print(f"✓ Learned '{name}': {code}")
            return code

        print(f"✗ Nothing captured for '{name}'.")
        choice = input("Press Enter to try again, or 'q' to quit and save... ").strip().lower()
        if choice == "q":
            return None


def main():
    ip = prompt_ip()
    frequency = prompt_frequency()
    dev = connect(ip)
    results = {}

    while True:
        name = prompt_button_name(results)
        code = learn_button(dev, frequency, name)

        if code is None:
            break
        results[name] = code

        choice = input("Press Enter to add another button, or 'q' to quit and save... ").strip().lower()
        if choice == "q":
            break

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nSaved {len(results)} code(s) to {OUTPUT_FILE}:")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
