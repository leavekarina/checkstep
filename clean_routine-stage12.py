# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: CleanRoutine
import json, os, sys

def load_routine_from_file(filepath: str) -> dict | None:
    if not filepath or not os.path.exists(filepath):
        print(f"Файл '{filepath}' не найден или путь пуст.")
        return None
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, dict):
            print("Ошибка: JSON должен содержать корневой объект (dict).")
            return None
            
        # Простая валидация структуры данных
        required_keys = {'zones', 'tasks'}
        missing = required_keys - set(data.keys())
        if missing:
            print(f"Ошибка: отсутствуют обязательные ключи {missing}.")
            return None
        
        for zone_name, tasks in data.get('zones', {}).items():
            if not isinstance(tasks, list):
                print(f"Ошибка: задачи для зоны '{zone_name}' должны быть списком.")
                return None
                
            for task in tasks:
                if 'periodicity' not in task or 'completed' not in task:
                    print(f"Ошибка: задача в зоне '{zone_name}' некорректна (не хватает periodicity/completed).")
                    return None
        
        print(f"Успешно загружен план уборки из файла '{filepath}'.")
        return data

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле '{filepath}': {e}")
        return None
    except IOError as e:
        print(f"Ошибка чтения файла '{filepath}': {e}")
        return None
