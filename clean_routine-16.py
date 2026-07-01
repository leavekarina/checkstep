# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: CleanRoutine
def calculate_monthly_stats(stats: dict, current_date: datetime) -> None:
    year = current_date.year
    month = current_date.month
    if stats.get(year, {}).get(month):
        return
    stats[year][month] = {
        "total_tasks": 0,
        "completed_tasks": 0,
        "zones_covered": set(),
        "tasks_by_zone": defaultdict(int),
    }

def run_monthly_report(stats: dict) -> None:
    if not stats:
        print("Нет данных для отчёта.")
        return
    for year in sorted(stats.keys()):
        for month in range(1, 13):
            data = stats[year].get(month)
            if not data:
                continue
            total = data["total_tasks"]
            completed = data["completed_tasks"]
            coverage = len(data["zones_covered"]) / max(len(all_zones), 1) * 100
            print(f"{year}-{month:02d}: выполнено {completed}/{total} задач, охвачено зон {coverage:.1f}%")
