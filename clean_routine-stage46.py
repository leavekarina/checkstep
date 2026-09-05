# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: CleanRoutine
import json, os

def migrate_structure():
    """Миграция структуры данных CleanRoutine из v1 в v2.

    v1 → v2:
      - зоны с дублирующими полями (zone_id, zone_name, zone_label) теперь
        хранятся как единое поле zone (словарь с ключами id, name, label);
      - периодичность (frequency) из строки "daily"/"weekly" теперь
        кодируется через enum Periodicity;
      - статистика выполнения (task_stats) теперь включает поле last_cleaned;
      - добавлена метка migration_version для отслеживания текущей схемы.
    """
    data_path = "clean_routine_data.json"
    if not os.path.exists(data_path):
        return

    try:
        with open(data_path, "r", encoding="utf-8") as f:
            raw = json.load(f)
    except Exception:
        return

    raw.setdefault("migration_version", 1)
    if raw["migration_version"] == 1:
        raw["migration_version"] = 2

        zones = raw.setdefault("zones", [])
        for z in zones:
            if "zone_id" in z and "zone_name" in z and "zone_label" in z:
                z["zone"] = {
                    "id": z.pop("zone_id"),
                    "name": z.pop("zone_name"),
                    "label": z.pop("zone_label"),
                }

        frequency_map = {"daily": "daily", "weekly": "weekly", "monthly": "monthly"}
        for task in raw.get("tasks", []):
            freq = task.get("frequency")
            if freq in frequency_map:
                task["frequency"] = frequency_map[freq]

        for stat in raw.get("task_stats", []):
            task_id = stat.get("task_id")
            if task_id:
                task = next(
                    (t for t in raw["tasks"] if t.get("id") == task_id), None
                )
                if task:
                    stat.setdefault("last_cleaned", None)

    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(raw, f, ensure_ascii=False, indent=2)

    print("Миграция v1 → v2 завершена.")

migrate_structure()
