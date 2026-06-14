# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: CleanRoutine
def delete_task(task_id: int) -> bool:
    try:
        tasks = load_tasks()
        if not tasks:
            return False
        new_tasks = [t for t in tasks if t['id'] != task_id]
        save_tasks(new_tasks)
        print(f"Задача #{task_id} удалена.")
        return True
    except FileNotFoundError:
        print("Файл задач не найден или пуст.")
        return False
    except Exception as e:
        print(f"Ошибка при удалении задачи: {e}")
        return False

def delete_zone(zone_name: str) -> bool:
    try:
        tasks = load_tasks()
        if not tasks:
            return False
        new_tasks = [t for t in tasks if t['zone'] != zone_name]
        save_tasks(new_tasks)
        print(f"Зона '{zone_name}' и все её задачи удалены.")
        return True
    except FileNotFoundError:
        print("Файл задач не найден или пуст.")
        return False
    except Exception as e:
        print(f"Ошибка при удалении зоны: {e}")
        return False
