# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: CleanRoutine
def export_state_to_json():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.now().isoformat(),
        "zones": zones,
        "tasks": tasks,
        "stats": stats
    }
    return json.dumps(state, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    print(export_state_to_json())
