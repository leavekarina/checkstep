# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: CleanRoutine
import pickle, os, uuid
from datetime import date

PROFILES_DIR = "profiles"
PROFILE_FILE = "current_profile.pkl"

def _ensure_profiles_dir():
    if not os.path.isdir(PROFILES_DIR):
        os.makedirs(PROFILES_DIR)

def save_profile(profile_name: str, user_data: dict):
    _ensure_profiles_dir()
    path = os.path.join(PROFILES_DIR, f"{profile_name}.pkl")
    with open(path, "wb") as f:
        pickle.dump(user_data, f)
    return profile_name

def load_profile(name: str) -> dict | None:
    _ensure_profiles_dir()
    path = os.path.join(PROFILES_DIR, f"{name}.pkl")
    if not os.path.isfile(path):
        return None
    with open(path, "rb") as f:
        return pickle.load(f)

def get_current_profile():
    if os.path.isfile(PROFILE_FILE):
        try:
            with open(PROFILE_FILE, "rb") as f:
                return pickle.load(f)
        except Exception:
            pass
    return load_profile("default") or {}

def set_current_profile(name: str):
    if not name or not os.path.isfile(os.path.join(PROFILES_DIR, f"{name}.pkl")):
        print(f"Профиль '{name}' не найден.")
        return None
    data = load_profile(name)
    with open(PROFILE_FILE, "wb") as f:
        pickle.dump(data, f)
    return data

def list_profiles():
    _ensure_profiles_dir()
    profiles = [f.rsplit(".", 1)[0] for f in os.listdir(PROFILES_DIR) if f.endswith(".pkl")]
    return sorted(profiles)

def add_default_profile(name: str = "default"):
    save_profile(name, {
        "name": name,
        "active_zones": ["кухня", "ванна"],
        "frequency": {"кухня": 1, "ванна": 7},
        "stats": {},
        "last_cleaned": None
    })
