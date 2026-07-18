# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: CleanRoutine
def reset_demo_data():
    """Сброс демо-данных в начале каждого зоны."""
    global current_zone, current_task_index, task_status
    current_zone = 0
    current_task_index = 0
    task_status = {"status": "pending", "completed_at": None}

def reset_all_data():
    """Полный сброс: демо-данные + история статистики."""
    reset_demo_data()
    history = []
    return history
