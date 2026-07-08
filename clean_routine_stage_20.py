# === Stage 20: Добавь восстановление записей из архива ===
# Project: CleanRoutine
def restore_from_archive(archive_path):
    """Восстанавливает записи из JSON-архива, если файл существует."""
    import json
    if not os.path.exists(archive_path):
        print(f"Архив не найден: {archive_path}")
        return False
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        records = data.get('records', [])
        if not records:
            print("Архив пуст.")
            return False
        for rec in records:
            record_id = rec['id']
            if record_id not in database:
                database[record_id] = rec
            else:
                print(f"Запись {record_id} уже существует в БД, пропуск.")
        print(f"Восстановлено {len(records)} записей из архива.")
        return True
    except Exception as e:
        print(f"Ошибка при восстановлении: {e}")
        return False


def export_to_archive(archive_path):
    """Экспортирует все текущие записи в JSON-архив."""
    records = list(database.values())
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump({'records': records}, f, ensure_ascii=False, indent=2)
    print(f"Архив сохранён: {len(records)} записей.")


if __name__ == "__main__":
    archive_path = os.path.join(os.path.dirname(__file__), 'archive.json')
    print("=== CleanRoutine v20. Архив и восстановление ===")
    export_to_archive(archive_path)
    import time; time.sleep(1)
    restore_from_archive(archive_path)
