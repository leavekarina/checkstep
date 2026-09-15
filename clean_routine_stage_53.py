# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: CleanRoutine
import json, csv, os

def export_to_csv(records, filepath):
    if not records:
        return
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['zone', 'task', 'due', 'done', 'completed_at'])
        for r in records:
            w.writerow([r['zone'], r['task'], r['due'], r['done'], r.get('completed_at', '')])

def export_to_json(records, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    sample = [
        {'zone': 'kitchen', 'task': 'wipe counter', 'due': '2025-01-01', 'done': True, 'completed_at': '2025-01-01 10:00'},
        {'zone': 'bathroom', 'task': 'clean sink', 'due': '2025-01-02', 'done': False, 'completed_at': ''},
    ]
    export_to_csv(sample, 'cleanroutine_export.csv')
    export_to_json(sample, 'cleanroutine_export.json')
    print('Exported reports saved.')
