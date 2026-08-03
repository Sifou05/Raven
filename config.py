from pathlib import Path

HASHCAT_PATH = r"G:\hashcat-6.2.6\hashcat-6.2.6\hashcat.exe"

BASE_DIR = Path(__file__).resolve().parent
WORDLIST_DIR = BASE_DIR/ "data" / "wordlists"

MODELS_DIR = ""
MODELS_DIR = BASE_DIR / "data" / "models"
