# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: CleanRoutine
def suggest_next_action(user, zones, stats):
    """Recommend the next cleaning step based on current state."""
    pending = [z for z in zones if not z.completed]
    if not pending:
        return "Все зоны убраны! Отличная работа. Хотите начать заново?"

    # Sort by frequency (higher freq first), then alphabetically
    pending.sort(key=lambda z: (-z.frequency, z.name))

    # If user has a streak goal and is close to it, suggest that zone type
    if stats and stats.get("streak_goal"):
        current_streak = sum(1 for d in stats["history"] 
                            if any(d.get(f"last_clean_{z.name}") > 0 for z in zones))
        if current_streak >= stats["streak_goal"] - 1:
            return (f"Отлично! Вы почти достигли streak в {stats['streak_goal']} дней. "
                    f"Давайте завершим сейчас — начнём с зоны «{pending[0].name}»?")

    # Pick the most frequent pending zone and its first incomplete task
    top_zone = pending[0]
    tasks = [t for t in top_zone.tasks if not t.done]
    if tasks:
        return (f"Следующее действие: {tasks[0].description} "
                f"(зона «{top_zone.name}\", периодичность: каждые {top_zone.frequency} дней)")

    # Fallback — just any pending zone's first task
    for z in pending:
        tasks = [t for t in z.tasks if not t.done]
        if tasks:
            return (f"Следующее действие: {tasks[0].description} "
                    f"(зона «{z.name}\", периодичность: каждые {z.frequency} дней)")

    return "Нет конкретных задач. Хотите добавить новую в зону?"
