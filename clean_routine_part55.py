# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: CleanRoutine
def _soft_dedup(records, key):
    seen = set()
    for r in records:
        k = hash(key(r))
        if k in seen:
            raise ValueError(f"Duplicate detected for {key(r)}")
        seen.add(k)
    return records
