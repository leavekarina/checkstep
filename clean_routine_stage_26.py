# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: CleanRoutine
def demo_quick_test():
    """Демо-команды для ручного тестирования CleanRoutine."""
    import random
    zones = [
        {"name": "Кухня", "period": "ежедневно", "checks": ["Протереть столешницу", "Помыть раковину", "Вынести мусор"]},
        {"name": "Ванная", "period": "раз в неделю", "checks": ["Убрать волосы с пола", "Протереть зеркала", "Постирать шторку"]}
    ]
    stats = {z["name"]: {"done": 0, "total": 0} for z in zones}
    print("=== Демо-тест CleanRoutine ===")
    for i in range(5):
        zone = random.choice(zones)
        check = random.choice(zone["checks"])
        stats[zone["name"]]["total"] += 1
        if random.random() > 0.3:
            stats[zone["name"]]["done"] += 1
            print(f"✓ {check} (зона: {zone['name']})")
        else:
            print(f"✗ {check} (пропущено)")
    print("\n=== Статистика ===")
    for name, s in stats.items():
        pct = round(s["done"] / s["total"] * 100) if s["total"] else 0
        print(f"{name}: {s['done']}/{s['total']} ({pct}%)")

demo_quick_test()
