# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: CleanRoutine
def generate_summary(tasks, completed_tasks):
    total = len(tasks)
    done = len(completed_tasks)
    progress = (done / total * 100) if total else 0
    print(f"Сводка: выполнено {done}/{total} задач ({progress:.1f}%).")
    for task in tasks:
        status = "✓" if task['id'] in completed_tasks else "○"
        print(f"{status} [{task['periodicity']}] {task['zone']} - {task['checklist'][0]}")
