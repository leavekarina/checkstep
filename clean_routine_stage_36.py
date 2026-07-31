# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: CleanRoutine
def validate_and_fix(self):
        """Проверка целостности данных и автоматический ремонт простых проблем."""
        issues = []
        # Проверка: все зоны имеют хотя бы одну задачу
        for zone in self.zones.values():
            if not zone.tasks:
                issues.append(f"Зона '{zone.name}' пуста, добавлена задача 'Обзор'")
                zone.add_task("Обзор", "1 раз в месяц", 2)
        # Проверка: все задачи имеют хотя бы один чек-лист
        for task in self.tasks.values():
            if not task.checklists:
                issues.append(f"Задача '{task.name}' без чек-листа, добавлен базовый")
                task.add_checklist("Базовая проверка", ["Выполнено?"])
        # Проверка: все пользователи имеют хотя бы один профиль
        for user in self.users.values():
            if not user.profiles:
                issues.append(f"Пользователь '{user.username}' без профиля, создан дефолтный")
                user.add_profile("Дефолт", {"score": 0})
        # Проверка: статистика не пустая после добавления задач/профилей
        if not self.statistics.completed_tasks and self.tasks.values():
            issues.append("Статистика пуста, инициализирована")
            self.statistics.reset()
        return issues
