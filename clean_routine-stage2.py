# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: CleanRoutine
class CleaningZone:
    def __init__(self, name, frequency_days):
        self.name = name
        self.frequency_days = frequency_days

class Task:
    def __init__(self, zone_name, description, estimated_minutes):
        self.zone_name = zone_name
        self.description = description
        self.estimated_minutes = estimated_minutes

def validate_input(zone_name, frequency_days, task_description, estimated_minutes):
    if not zone_name or not isinstance(zone_name, str):
        raise ValueError("Имя зоны должно быть непустой строкой.")
    if not (1 <= frequency_days <= 365):
        raise ValueError("Периодичность должна быть от 1 до 365 дней.")
    if not task_description or not isinstance(task_description, str):
        raise ValueError("Описание задачи должно быть непустой строкой.")
    if not (0 < estimated_minutes <= 480):
        raise ValueError("Время выполнения должно быть от 1 до 480 минут.")
    return True
