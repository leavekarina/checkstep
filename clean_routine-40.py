# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: CleanRoutine
import argparse

def main():
    parser = argparse.ArgumentParser(description="CleanRoutine CLI")
    parser.add_argument("--add", action="store_true", help="Добавить зону/чек-лист")
    parser.add_argument("--remove", action="store_true", help="Удалить зону/чек-лист")
    parser.add_argument("--mark", action="store_true", help="Отметить выполнение")
    parser.add_argument("--stats", action="store_true", help="Показать статистику")
    parser.add_argument("--list", action="store_true", help="Вывести все элементы")
    args = parser.parse_args()
    
    if args.add:
        print("Режим добавления: введите зону и чек-лист")
    elif args.remove:
        print("Режим удаления: введите ID элемента")
    elif args.mark:
        print("Режим отметки: введите ID элемента")
    elif args.stats:
        print("Статистика выполнения")
    elif args.list:
        print("Вывод всех элементов")
    else:
        print("Выберите операцию с помощью --add, --remove, --mark, --stats, или --list")

if __name__ == "__main__":
    main()
