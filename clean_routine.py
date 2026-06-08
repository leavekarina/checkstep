# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: CleanRoutine
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class Zone:
    def __init__(self, name: str, frequency_days: int):
        self.name = name
        self.frequency_days = frequency_days
        self.last_cleaned: Optional[datetime] = None
        self.checklist: List[str] = []

    def is_due(self) -> bool:
        if not self.last_cleaned:
            return True
        next_date = self.last_cleaned + timedelta(days=self.frequency_days)
        return datetime.now() >= next_date

class CleanRoutineApp:
    def __init__(self):
        self.zones: Dict[str, Zone] = {}
        self.stats: Dict[str, int] = {}

    def add_zone(self, name: str, frequency_days: int, checklist: List[str]):
        zone = Zone(name, frequency_days)
        zone.checklist = checklist
        self.zones[name] = zone
        self.stats[name] = 0

    def mark_cleaned(self, zone_name: str):
        if zone_name in self.zones:
            self.zones[zone_name].last_cleaned = datetime.now()
            self.stats[zone_name] += 1

    def get_due_zones(self) -> List[str]:
        return [name for name, zone in self.zones.items() if zone.is_due()]

# --- Демонстрационные данные и точка входа ---
if __name__ == "__main__":
    app = CleanRoutineApp()
    
    # Добавляем зоны с чек-листами
    app.add_zone("Кухня", 3, ["Помыть посуду", "Протереть стол", "Вынести мусор"])
    app.add_zone("Ванная", 2, ["Убрать волосы", "Протереть зеркало", "Помыть ванну"])
    app.add_zone("Гостиная", 7, ["Подмести пол", "Пропылесосить диван"])
    
    # Демонстрация: вывод зон, которые нужно убирать сегодня
    due_zones = app.get_due_zones()
    print(f"Зон для уборки сегодня: {', '.join(due_zones) if due_zones else 'Нет'}")
