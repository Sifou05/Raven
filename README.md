# Raven

Raven is a desktop app for password and hash cracking, built with Python and Tkinter (customtkinter). It wraps around Hashcat and adds AI-assisted candidate generation to make wordlist-based attacks smarter.

⚠️ **For authorized use only** — password auditing on systems and data you own or have explicit permission to test (CTFs, your own lab, authorized pentests).

## Status

Early development. Home screen, navigation between screens, and the crack screen's file browser are working. First-run setup (choosing your Hashcat install) is in progress. Core cracking logic (Hashcat integration, AI candidate generation) is still to come.

## Features (planned)

- First-run setup to locate your Hashcat installation
- Load a hash or file to crack
- Choose an attack mode: dictionary, AI-generated candidates, or mask attack
- Run Hashcat under the hood with live progress
- View and export cracked results
- Simple, dark-themed GUI

## Tech stack

- **Python 3.10+**
- **customtkinter** (GUI)
- **Hashcat** (cracking engine, installed separately)
- AI candidate generation model (PassGAN-style, trained separately)

## Project structure

```
Raven/
├── main.py                # Entry point
├── config.py               # Paths and constants
├── gui/
│   ├── homeSC.py            # Home screen
│   ├── crackSC.py           # Attack setup + progress
│   ├── setupSC.py           # First-run Hashcat setup screen
│   └── resultsSC.py         # Results screen
├── core/
│   ├── settings.py          # Save/load user settings (e.g. Hashcat path)
│   ├── hashcat_wrapper.py   # Hashcat subprocess integration
│   └── candidate_gen.py     # AI candidate generation
├── data/
│   ├── wordlists/
│   └── models/               # Trained model weights
├── assets/                  # Icons and images
├── requirements.txt
└── venv/                    # Virtual environment (not committed)
```

## Setup

### 1. Prerequisites

- **Python 3.10+**
- **Tkinter.** On Linux this often needs installing separately:
  ```bash
  sudo apt install python3-tk        # Debian/Ubuntu/Parrot
  ```
- **Hashcat**, installed and available somewhere on disk:
  ```bash
  sudo apt install hashcat           # Debian/Ubuntu/Parrot
  ```
  or download it from the [official site](https://hashcat.net/hashcat/) for a specific version.

### 2. Get the project and install dependencies

```bash
git clone <this-repo-url>
cd Raven/Raven
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run it

```bash
python3 main.py
```

## Disclaimer

This tool is for educational and authorized security testing purposes only. Using it against systems or data without permission is illegal. The author takes no responsibility for misuse.
