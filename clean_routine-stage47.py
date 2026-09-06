# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: CleanRoutine
def demo():
    """Демонстрация основного сценария использования CleanRoutine."""
    zones = [
        Zone("Кухня", "ежедневно", ["мыть посуду", "вытирать стол", "проветрить"]),
        Zone("Спальня", "недельно", ["сделать постель", "убрать одежду", "пропылесосить"]),
        Zone("Гостиная", "ежедневно", ["протереть пыль", "вынести мусор"]),
    ]
    routine = Routine("Мой план уборки", zones)
    routine.add_checklist("Понедельник", ["Кухня", "Спальня"])
    routine.add_checklist("Вторник", ["Гостиная"])
    routine.add_checklist("Среда", ["Кухня", "Гостиная"])
    routine.add_checklist("Четверг", ["Спальня"])
    routine.add_checklist("Пятница", ["Кухня", "Гостиная", "Спальня"])
    print("Добро пожаловать в CleanRoutine!")
    print(f"Всего зон: {len(routine.zones)}")
    print(f"Планов на неделю: {len(routine.checklists)}")
    routine.track_progress()
