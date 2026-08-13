# Raven

Raven is a desktop app for password and hash cracking, built with Python and Tkinter. It wraps around Hashcat and adds AI-assisted candidate generation to make wordlist-based attacks smarter.

⚠️ **For authorized use only** — password auditing on systems and data you own or have explicit permission to test (CTFs, your own lab, authorized pentests).

## Status

Early development. The home screen and navigation between screens are working. Core cracking logic (Hashcat integration, AI candidate generation) is still in progress.

## Features (planned)

- Load a hash or file to crack
- Choose an attack mode: dictionary, AI-generated candidates, or mask attack
- Run Hashcat under the hood with live progress
- View and export cracked results
- Simple, dark-themed GUI

## Tech stack

- **Python 3.14** + **Tkinter** (GUI)
- **Hashcat** (cracking engine)
- AI candidate generation model (PassGAN-style, trained separately)

## Project structure

```
Raven/
├── main.py              # Entry point
├── config.py             # Paths and constants
├── gui/
│   ├── homeSC.py          # Home screen
│   ├── crackSC.py         # Attack setup + progress
│   └── resultsSC.py       # Results screen
├── core/                 # Hashcat wrapper, AI candidate generation
├── data/
│   ├── wordlists/
│   └── models/            # Trained model weights
└── assets/                # Icons and images
```

## Running it

```bash
python3 main.py
```

Make sure Hashcat is installed and the path to it is set correctly in `config.py`.

## Disclaimer

This tool is for educational and authorized security testing purposes only. Using it against systems or data without permission is illegal. The author takes no responsibility for misuse.
