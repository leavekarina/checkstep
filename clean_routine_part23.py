# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: CleanRoutine
def print_task_table(tasks):
    if not tasks:
        print("Нет задач для отображения")
        return
    headers = ["Зона", "Периодичность", "Статус", "Последнее выполнение"]
    widths = [len(h) for h in headers]
    for t in tasks:
        row = [t["zone"], str(t["period"]), t.get("status", ""), str(t.get("last_done", ""))]
        for i, cell in enumerate(row):
            if len(cell) > widths[i]:
                widths[i] = len(cell)
    print(f"{'Зона':<{widths[0]}} {'Периодичность':<{widths[1]}} {'Статус':<{widths[2]}} {'Последнее выполнение':<{widths[3]}}")
    for t in tasks:
        row = [t["zone"], str(t["period"]), t.get("status", ""), str(t.get("last_done", ""))]
        print(f"{row[0]:<{widths[0]}} {row[1]:<{widths[1]}} {row[2]:<{widths[2]}} {row[3]:<{widths[3]}}")
