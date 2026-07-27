# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: CleanRoutine
class UndoStack:
    def __init__(self):
        self._stack = []

    def push(self, state):
        self._stack.append(state)

    def undo(self):
        return self._stack.pop() if self._stack else None


class CleanRoutine:
    _undo_stack = UndoStack()

    @classmethod
    def reset(cls):
        cls._undo_stack = UndoStack()

    @staticmethod
    def clean_zone(zone, checklist, interval='daily', now=None):
        if not zone or not checklist:
            return False
        cls._undo_stack.push({'zone': zone, 'checklist': checklist})
        success = all(checklist)
        if now is None:
            from datetime import datetime
            now = datetime.now()
        last_cleaned[zone] = {
            'last': now,
            'interval': interval,
            'next_due': _compute_next(now, interval),
        }
        return success


def _compute_next(start, interval):
    if start is None:
        from datetime import datetime
        dt = datetime.now()
    else:
        dt = start

    intervals_map = {
        'daily': timedelta(days=1),
        'weekly': timedelta(weeks=1),
        'monthly': timedelta(days=30),
        'yearly': timedelta(days=365),
    }

    period = intervals_map.get(interval, intervals_map['daily'])
    return dt + period


def _update_stats():
    stats = {
        'cleaned_zones': len({k for k in last_cleaned if last_cleaned[k]['last'] is not None}),
        'latest': max((v['last'] for v in last_cleaned.values() if v['last']), default=None),
    }

    if stats['latest']:
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        stats['today'] = (stats['latest'].date() == today).to_json()
        stats['yesterday'] = (stats['latest'].date() == yesterday).to_json()

    return stats


class CleanRoutineApp:
    @staticmethod
    def run():
        print("CleanRoutine App started.")
        try:
            zone_name = input("Zone name: ").strip().lower()
        except EOFError:
            zone_name = "default"

        checklist_input = input("Checklist (comma-separated): ").strip().split(',')
        interval = input(f"Interval ({', '.join(intervals_map.keys())}): ") or 'daily'

        cleaned = clean_zone(zone_name, checklist_input, interval=interval)
        if cleaned:
            print(f"Zone '{zone_name}' cleaned successfully!")
        else:
            print("Not all items checked.")

        stats = _update_stats()
        print("\n--- Stats ---")
        for key in ['cleaned_zones', 'latest', 'today', 'yesterday']:
            print(f"{key}: {stats[key]}")

        if undo_stack.undo():
            print("Undo action applied.")


if __name__ == '__main__':
    CleanRoutineApp.run()
