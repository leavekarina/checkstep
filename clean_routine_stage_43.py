# === Stage 43: Добавь пагинацию длинных списков ===
# Project: CleanRoutine
def paginate(items, page_size=10):
    """Page long lists: returns (page_items, total_pages, current_page)."""
    total_pages = max(1, (len(items) + page_size - 1) // page_size)
    current = min(page_size, len(items))
    return items[:current], total_pages, current
