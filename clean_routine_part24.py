# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: CleanRoutine
def print_record(record):
    """Компактный вывод одной записи с деталями."""
    if record is None:
        return
    print(f"📋 {record['status']} | Зона: {record.get('zone', '—')}")
    print(f"   Чек-лист: {'✅ '.join(record.get('completed_items', []))} "
          f"{', ❌ '.join(record.get('pending_items', []))}")
    if record.get('notes'):
        print(f"   📝 {record['notes']}")
