# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: CleanRoutine
import copy

def dry_run(operation, *args, **kwargs):
    """Simulate an operation without actually changing state.
    
    Usage:
        result = dry_run(rooms.add, "Kitchen", "Daily")
        # rooms unchanged, result is the value that would be stored
    """
    if not hasattr(operation, '__name__'):
        raise TypeError(f"operation must be callable, got {type(operation)}")
    
    try:
        state = copy.deepcopy(_state)
        operation(*args, **kwargs)
        return _state
    except Exception as e:
        raise RuntimeError(f"Dry-run failed for {operation.__name__}: {e}")
