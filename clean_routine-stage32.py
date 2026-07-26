# === Stage 32: Добавь журнал действий пользователя ===
# Project: CleanRoutine
class ActionLog:
    _log = []

    @classmethod
    def log(cls, user, action_type, details):
        cls._log.append({"user": user, "type": action_type, "details": details})

    @classmethod
    def get_log(cls):
        return cls._log.copy()

    @classmethod
    def clear(cls):
        cls._log.clear()

    @classmethod
    def recent(cls, count=5):
        return cls._log[-count:] if len(cls._log) >= count else cls._log[:]
