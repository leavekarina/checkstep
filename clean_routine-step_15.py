# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: CleanRoutine
def calculate_weekly_stats(stats_history):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1)
    
    weekly_data = {d.strftime('%Y-%m-%d'): {'completed': 0, 'total_items': 0} for d in range(week_start, week_end)}
    
    for entry in stats_history:
        task_date = date.fromisoformat(entry['date'])
        if not (week_start <= task_date < week_end):
            continue
        
        weekly_data[task_date.strftime('%Y-%m-%d')]['completed'] += 1
        weekly_data[task_date.strftime('%Y-%m-%d')]['total_items'] += len(entry.get('items', []))
    
    return weekly_data
