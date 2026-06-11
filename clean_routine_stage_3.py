# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: CleanRoutine
class RoutineState:
    def __init__(self):
        self.records = []
        
    def add_record(self, zone_name: str, task_description: str, completed: bool, timestamp=None):
        if timestamp is None:
            import datetime
            timestamp = datetime.datetime.now()
        record = {
            "zone": zone_name,
            "task": task_description,
            "completed": completed,
            "timestamp": timestamp.isoformat(),
            "id": len(self.records) + 1
        }
        self.records.append(record)
        
    def get_records_by_zone(self, zone: str):
        return [r for r in self.records if r["zone"] == zone]
        
    def get_statistics(self):
        total = len(self.records)
        completed_count = sum(1 for r in self.records if r["completed"])
        completion_rate = (completed_count / total * 100) if total > 0 else 0.0
        return {
            "total_records": total,
            "completed_tasks": completed_count,
            "completion_percentage": round(completion_rate, 2)
        }

state_manager = RoutineState()
