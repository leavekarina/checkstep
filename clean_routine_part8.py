# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: CleanRoutine
def show_menu():
    print("\n=== CleanRoutine: Меню действий ===")
    print("1. Показать все зоны уборки")
    print("2. Добавить новую зону")
    print("3. Изменить периодичность для зоны")
    print("4. Просмотреть статистику выполнения")
    print("5. Выход из программы")
    choice = input("\nВыберите действие (1-5): ")
    return choice

def run_command(choice: str, zones: dict, stats: dict) -> None:
    if choice == "1":
        for zone_name, data in zones.items():
            print(f"\nЗона: {zone_name}")
            print(f"  Периодичность: {data['periodicity']}")
            print(f"  Выполнено за месяц: {stats.get(zone_name, {}).get('completed', 0)} раз(а)")
    elif choice == "2":
        name = input("Название новой зоны: ")
        if not zones.get(name):
            periodicity = input("Периодичность (ежедневно/раз в неделю/раз в месяц): ")
            zones[name] = {"periodicity": periodicity, "tasks": []}
            print(f"Зона '{name}' добавлена.")
        else:
            print("Такая зона уже существует.")
    elif choice == "3":
        name = input("Название зоны для изменения периодичности: ")
        if zones.get(name):
            new_periodicity = input("Новая периодичность (ежедневно/раз в неделю/раз в месяц): ")
            zones[name]["periodicity"] = new_periodicity
            print(f"Периодичность для '{name}' обновлена.")
    elif choice == "4":
        for zone_name, data in stats.items():
            total_tasks = len(data.get("tasks", []))
            completed_count = data.get("completed", 0)
            if total_tasks > 0:
                print(f"\nЗона '{zone_name}': выполнено {completed_count}/{total_tasks} задач")
    elif choice == "5":
        print("Выход из программы.")
    else:
        print("Неверный выбор. Попробуйте снова.")
