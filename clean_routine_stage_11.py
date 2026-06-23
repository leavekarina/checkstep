# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: CleanRoutine
import json, os

DATA_FILE = "clean_routine_data.json"

def save_to_json(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def get_data_store():
    store = load_from_json()
    if not store.get('zones'):
        store['zones'] = []
    if not store.get('tasks'):
        store['tasks'] = []
    if not store.get('stats'):
        store['stats'] = {}
    save_to_json(store)
    return store
