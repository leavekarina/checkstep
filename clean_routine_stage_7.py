# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: CleanRoutine
def sort_tasks(tasks, key='date'):
    if not tasks: return []
    order = {'daily': 0, 'weekly': 1, 'monthly': 2}
    def _sort_key(t):
        date_val = t.get('last_run') or datetime.min.replace(year=9999)
        priority_val = -t.get('priority', 3)
        return (order.get(key, 0), date_val, priority_val, t.get('name', ''))
    return sorted(tasks, key=_sort_key)
