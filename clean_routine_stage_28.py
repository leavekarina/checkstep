# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: CleanRoutine
def report_metrics(stats):
    """Компактный отчёт по ключевым метрикам проекта."""
    total_tasks = sum(len(z["tasks"]) for z in stats.values())
    completed = sum(1 for z in stats.values() for t in z["tasks"] if t.get("done"))
    overdue = {z: [t for t in z["tasks"] if t.get("overdue")] for z in stats.values()}
    overdue_areas = {k: v for k, v in overdue.items() if v}
    print(f"Всего задач: {total_tasks}")
    print(f"Выполнено: {completed} / {total_tasks}")
    print(f"Отставание от графика:")
    for area, tasks in sorted(overdue_areas.items()):
        count = len(tasks)
        if count == 1:
            print(f"  - {area}: {count} задача")
        else:
            print(f"  - {area}: {count} задачи")
