# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: CleanRoutine
def check_overdue_reminders(reminders):
    overdue = []
    now = datetime.now()
    for r in reminders:
        if r['date'] < now and 'done' not in r:
            overdue.append(r)
    return overdue
