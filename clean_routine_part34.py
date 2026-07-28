# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: CleanRoutine
TEMPLATES = {
    "daily_kitchen": {
        "name": "Ежедневная кухня",
        "schedule": {"period": "day", "interval": 1},
        "zone": "kitchen",
        "tasks": [
            {"title": "Протереть столешницы", "category": "cleaning"},
            {"title": "Помыть посуду", "category": "cleaning"},
            {"title": "Вынести мусор", "category": "waste"},
        ],
    },
    "weekly_bathroom": {
        "name": "Еженедельная ванная",
        "schedule": {"period": "week", "interval": 1},
        "zone": "bathroom",
        "tasks": [
            {"title": "Помыть раковину", "category": "cleaning"},
            {"title": "Протереть зеркала", "category": "cleaning"},
            {"title": "Вымыть пол", "category": "cleaning"},
        ],
    },
    "monthly_deep": {
        "name": "Ежемесячная генеральная уборка",
        "schedule": {"period": "month", "interval": 1},
        "zone": "whole_house",
        "tasks": [
            {"title": "Протереть стены от пыли", "category": "cleaning"},
            {"title": "Вымыть окна", "category": "cleaning"},
            {"title": "Пропылить все комнаты", "category": "dusting"},
        ],
    },
}

def register_template(template_name):
    if template_name not in TEMPLATES:
        raise ValueError(f"Unknown template: {template_name}")
    tmpl = TEMPLATES[template_name].copy()
    return {
        "name": tmpl["name"],
        "schedule": tmpl["schedule"].copy(),
        "zone": tmpl["zone"],
        "tasks": [t.copy() for t in tmpl["tasks"]],
    }

def list_templates():
    return dict(TEMPLATES)
