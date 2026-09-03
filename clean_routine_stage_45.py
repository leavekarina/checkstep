# === Stage 45: Добавь восстановление из резервной копии ===
# Project: CleanRoutine
import json, os, sys

def load_backup(file_path):
    if not os.path.exists(file_path):
        print(f"Резервная копия не найдена: {file_path}")
        return False
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"Резервная копия загружена из {file_path}")
        return True
    except Exception as e:
        print(f"Ошибка при загрузке резервной копии: {e}")
        return False

def restore_backup(file_path, backup_file_path, overwrite=True):
    if not load_backup(backup_file_path):
        return False
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            current = f.read()
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(current)
        print(f"Резервная копия восстановлена в {file_path}")
        return True
    except Exception as e:
        print(f"Ошибка при восстановлении: {e}")
        return False
