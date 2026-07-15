# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: CleanRoutine
def parse_date_safe(date_str, default=None):
    """Парсит строку даты в объект datetime.date, возвращая значение по умолчанию при ошибках."""
    if not date_str:
        return default
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d.%m.%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    if date_str.lower() == "сегодня":
        return datetime.now().date()
    if default is not None:
        return default
    raise ValueError(f"Некорректная дата: '{date_str}'")


def format_date(date):
    """Форматирует объект datetime.date в строку YYYY-MM-DD."""
    if date is None:
        return "—"
    return str(date)
