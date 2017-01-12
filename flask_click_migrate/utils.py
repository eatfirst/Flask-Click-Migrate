"""Random utils."""
import threading

REGISTERED_COMMANDS = []
LOCK = threading.Lock()


def register_command(func):
    """Register commands to be used lazily."""
    with LOCK:
        REGISTERED_COMMANDS.append(func)
    return func
