# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: CleanRoutine
def edit_task(task_id: int, updates: dict) -> bool | None:
    if not (1 <= task_id <= len(tasks)):
        return False
    
    index = task_id - 1
    current = tasks[index]
    
    for key in ['area', 'frequency', 'checklist']:
        if key in updates and updates[key]:
            setattr(current, key, updates[key])
    
    if not updates.get('active', True):
        current.active = False
    
    return True

def delete_task(task_id: int) -> bool | None:
    if not (1 <= task_id <= len(tasks)):
        return False
    
    del tasks[task_id - 1]
    for i, t in enumerate(tasks):
        if t.id > task_id:
            t.id -= 1
    
    return True

def save_tasks():
    with open('clean_routine.py', 'r') as f:
        content = f.read()
    
    lines = content.splitlines()
    new_lines = []
    added = False
    
    for i, line in enumerate(lines):
        if not added and line.strip().startswith('tasks = ['):
            new_lines.append(line)
            new_lines.append('\n')
            new_lines.extend([edit_task.__doc__, delete_task.__doc__])
            added = True
        else:
            new_lines.append(line)
    
    with open('clean_routine.py', 'w') as f:
        f.write('\n'.join(new_lines))
