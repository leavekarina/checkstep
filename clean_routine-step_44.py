# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: CleanRoutine
import json
import os
from datetime import datetime

def backup_data_file(data_file_path: str, backup_dir: str = "backups") -> str:
    """Создаёт резервную копию файла данных в директории backups."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{timestamp}.json")
    with open(data_file_path, "r", encoding="utf-8") as src, open(backup_path, "w", encoding="utf-8") as dst:
        dst.write(src.read())
    return backup_path
