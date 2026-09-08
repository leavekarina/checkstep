# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: CleanRoutine
def format_stats(stats):
    """Форматирует статистику уборки в читаемый вид."""
    lines = []
    lines.append("📊 Статистика уборки:")
    lines.append(f"  • Всего выполнено зон: {stats.get('completed_zones', 0)}")
    lines.append(f"  • Всего выполнено задач: {stats.get('completed_tasks', 0)}")
    lines.append(f"  • Всего пропущено задач: {stats.get('missed_tasks', 0)}")
    lines.append(f"  • Средняя частота уборки: {stats.get('avg_frequency', 0)} раз")
    return "\n".join(lines)
