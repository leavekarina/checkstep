# === Stage 17: Добавь группировку записей по категориям ===
# Project: CleanRoutine
from collections import defaultdict

def group_by_category(records):
    grouped = defaultdict(list)
    for record in records:
        cat = record.get('category', 'other')
        grouped[cat].append(record)
    return dict(sorted(grouped.items()))
