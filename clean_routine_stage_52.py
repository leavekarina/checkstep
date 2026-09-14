# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: CleanRoutine
def export_report(stats: dict, zones: list, today: str = None) -> str:
    """Export a compact text report of cleaning routine."""
    lines = []
    if today:
        lines.append(f"📅 Report for {today}")
    else:
        lines.append("📅 Report")
    lines.append("=" * 30)
    total = sum(stats.values())
    lines.append(f"Total tasks done: {total}")
    for zone, count in stats.items():
        lines.append(f"  {zone}: {count}")
    lines.append("=" * 30)
    lines.append("Zones:")
    for z in zones:
        lines.append(f"  - {z['name']} (period: {z['period']})")
    lines.append("=" * 30)
    return "\n".join(lines)
