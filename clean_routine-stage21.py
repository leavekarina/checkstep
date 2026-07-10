# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: CleanRoutine
class Reminder:
    def __init__(self, task_name, due_date):
        self.task_name = task_name
        self.due_date = due_date

    def is_due(self):
        return datetime.date.today() >= self.due_date and self.due_date <= datetime.date.today().replace(hour=23)


class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, task_name, due_date):
        reminder = Reminder(task_name, due_date)
        self.reminders.append(reminder)

    def check_due_reminders(self):
        due = [r for r in self.reminders if r.is_due()]
        return due
