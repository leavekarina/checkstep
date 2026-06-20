# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: CleanRoutine
import json, os, uuid, datetime as dt

INITIAL_DATA = '''
{
  "zones": [
    {
      "id": "living-room",
      "name": "Гостиная",
      "tasks": [
        {"id": "dust-furniture", "text": "Протереть мебель", "frequency_days": 7},
        {"id": "vacuum-floor", "text": "Пылесосить пол", "frequency_days": 2}
      ]
    },
    {
      "id": "kitchen",
      "name": "Кухня",
      "tasks": [
        {"id": "clean-oven", "text": "Вымыть духовку", "frequency_days": 14},
        {"id": "wipe-counters", "text": "Протереть столешницы", "frequency_days": 2}
      ]
    }
  ],
  "history": [],
  "settings": {
    "default_timezone": "Europe/Moscow"
  }
}'''

def load_initial_data():
    try:
        data = json.loads(INITIAL_DATA)
        if not isinstance(data, dict):
            raise ValueError("Invalid JSON structure")
        
        # Validate zones and tasks
        for zone in data.get("zones", []):
            if "id" not in zone or "name" not in zone:
                raise ValueError(f"Zone missing required fields: {zone}")
            for task in zone.get("tasks", []):
                if "id" not in task or "text" not in task or "frequency_days" not in task:
                    raise ValueError(f"Task missing required fields: {task}")
        
        # Validate history format
        for entry in data.get("history", []):
            if not isinstance(entry, dict) or "zone_id" not in entry or "completed_at" not in entry:
                raise ValueError("Invalid history entry")
        
        return data
        
    except json.JSONDecodeError as e:
        print(f"[CleanRoutine] Failed to parse initial JSON: {e}")
        return None

def ensure_timezone(data):
    tz = data.get("settings", {}).get("default_timezone", "UTC")
    # In a real app, we would use pytz or zoneinfo here. 
    # Since no external libs allowed, we store the string and handle conversion later if needed.
    return data

def merge_data(existing: dict | None, new: dict) -> dict:
    merged = {k: v for k, v in (existing or {}).items() if k not in new}
    merged.update(new)
    
    # Merge zones by ID to avoid duplicates
    existing_zones = {z["id"]: z for z in merged.get("zones", [])}
    new_zones = {z["id"]: z for z in new.get("zones", [])}
    
    all_zone_ids = set(existing_zones.keys()) | set(new_zones.keys())
    merged["zones"] = []
    for zone_id in sorted(all_zone_ids):
        ez = existing_zones.get(zone_id, {})
        nz = new_zones.get(zone_id, {})
        
        # Prefer new
