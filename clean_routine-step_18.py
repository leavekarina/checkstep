# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: CleanRoutine
class TagManager:
    def __init__(self, db):
        self.db = db
    
    def add_tag(self, name=None):
        if not name:
            raise ValueError("Name is required")
        existing_tags = [t for t in self.db['tags'] if t['name'].lower() == name.lower()]
        if existing_tags:
            return existing_tags[0]
        new_id = max(self.db['tags'], key=lambda x: x.get('id', 0), default={'id': 0})['id'] + 1
        self.db['tags'].append({'id': new_id, 'name': name.lower(), 'created_at': datetime.now().isoformat()})
        return self.db['tags'][-1]
    
    def remove_tag(self, tag_name):
        tags_to_remove = [t for t in self.db['tasks'] if any(t.get('tag') == tag_name.lower())]
        for task in tasks_to_remove:
            task.pop('tag', None)
        existing_tags = [t for t in self.db['tags'] if t['name'].lower() == tag_name.lower()]
        if not existing_tags:
            return False
        self.db['tags'] = [t for t in self.db['tags'] if t['name'].lower() != tag_name.lower()]
        return True
    
    def get_tag(self, tag_name):
        tags = [t for t in self.db['tags'] if t['name'].lower() == tag_name.lower()]
        return tags[0] if tags else None

def add_tags_to_tasks(tasks_data, db):
    from datetime import datetime
    tag_manager = TagManager(db)
    tasks_with_tags = []
    for task in tasks_data:
        new_task = dict(task)
        if 'tag' in new_task and new_task['tag']:
            added_tag = tag_manager.add_tag(new_task.pop('tag'))
            new_task['tags'] = [added_tag]
        else:
            new_task['tags'] = []
        tasks_with_tags.append(new_task)
    return tasks_with_tags

def remove_tags_from_tasks(tasks_data, db):
    from datetime import datetime
    tag_manager = TagManager(db)
    cleaned_tasks = []
    for task in tasks_data:
        if 'tag' in task and task['tag']:
            removed_tag = tag_manager.remove_tag(task.pop('tag'))
            if not removed_tag:
                continue
        new_task = dict(task)
        new_task['tags'] = [t for t in new_task.get('tags', [])]
        cleaned_tasks.append(new_task)
    return cleaned_tasks
