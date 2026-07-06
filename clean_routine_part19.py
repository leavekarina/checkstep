# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: CleanRoutine
def archive_records(records, cutoff_days=30):
    """Archive records older than `cutoff_days` days."""
    import datetime
    now = datetime.datetime.now()
    archived = []
    for rec in records:
        if isinstance(rec, dict) and "date" in rec:
            try:
                age = (now - datetime.date.fromisoformat(rec["date"])).days
                if age > cutoff_days:
                    archived.append(rec.copy())
            except Exception:
                pass
    return archived
