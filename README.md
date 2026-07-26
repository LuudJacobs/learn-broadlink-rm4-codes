# broadlink-code-learner 1.0.1

Small scripts to reliably learn IR/RF codes with a Broadlink RM4 Pro. The
learned hex codes can be pasted directly wherever your automation setup
expects a raw code (e.g. in the config of a Homebridge accessory).

## Requirements

- Python 3
- A Broadlink RM4 Pro reachable on the same network

## Installation

```
pip3 install -r requirements.txt --break-system-packages
```

All scripts are interactive and will ask for the RM's IP address (and, for
RF, the frequency) when run - no need to edit any file first.

## Usage

Run a script directly, e.g.:

```
python3 learn_ir_codes.py
```

Each script walks you through the same basic loop:

1. Answer the setup questions (IP address, and for RF the frequency in MHz;
   `learn_rf_dim_levels.py` also asks for the number of dim levels first).
2. For `learn_ir_codes.py` and `learn_rf_codes.py`, enter a name for the
   button you're about to learn (`learn_rf_dim_levels.py` generates level
   names for you, see below).
3. Watch the 3-2-1 countdown, then press the button on the remote (or
   release the dimmer slider in its app) when prompted.
4. On success, press Enter to learn the next one, or `q` to quit and save.
   On failure, press Enter to retry the same button, or `q` to quit and save.

Output is written once, when you quit, to the JSON file named below.

### Scripts

#### learn_ir_codes.py

Interactively learns IR codes one button at a time and saves them to
`ir_codes.json`.

#### learn_rf_codes.py

Same interactive flow as `learn_ir_codes.py`, but for RF codes. Also prompts
for the frequency in MHz (e.g. 433.92) after the IP address, and saves
results to `rf_codes.json`.

#### learn_rf_dim_levels.py

Same interactive flow, for a dimmer's RF dim levels. First asks for the
number of dim levels (e.g. 16), then the IP address and frequency. Button
names are generated automatically as rounded percentages, e.g. `level-0`,
`level-7`, ... `level-100`. Control the dimmer during learning via its
companion app or hub instead of a physical remote. Saves results to
`rf_dim-level_codes.json`.

## Links

[License](https://github.com/LuudJacobs/learn-broadlink-rm4-codes/blob/main/LICENSE) · [Changelog](https://github.com/LuudJacobs/learn-broadlink-rm4-codes/blob/main/CHANGELOG.md)
