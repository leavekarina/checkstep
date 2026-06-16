# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: CleanRoutine
def filter_tasks(tasks, filters=None):
    if not filters: return tasks
    result = []
    for task in tasks:
        match_status = (not filters.get('status')) or task['status'] == filters['status']
        match_category = (not filters.get('category')) or task.get('category') == filters['category']
        match_tags = True
        if 'tags' in filters and task.get('tags'):
            match_tags = not set(filters['tags']).isdisjoint(task['tags'])
        if match_status and match_category and match_tags: result.append(task)
    return result

# Пример использования:
# filtered = filter_tasks(all_tasks, {'status': 'pending', 'category': 'kitchen'})
