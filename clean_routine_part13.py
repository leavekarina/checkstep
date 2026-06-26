# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: CleanRoutine
def search_tasks(query, tasks):
    query_lower = query.lower().strip()
    if not query_lower:
        return []
    
    def match(text):
        text_lower = (text or "").lower()
        return query_lower in text_lower
    
    results = [t for t in tasks if any(match(getattr(t, field)) for field in ['name', 'zone', 'frequency'])]
    return sorted(results, key=lambda x: len(x.get('name') or ''), reverse=True)
