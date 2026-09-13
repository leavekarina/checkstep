# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: CleanRoutine
class ChangeLog:
    def __init__(self):
        self.entries = []

    def log(self, category, description, data=None):
        entry = {
            "time": datetime.now().isoformat(),
            "category": category,
            "description": description,
            "data": data or {}
        }
        self.entries.append(entry)
        return entry

    def get_recent(self, count=10):
        return self.entries[-count:]
