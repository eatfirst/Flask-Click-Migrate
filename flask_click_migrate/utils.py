REGISTERED_COMMANDS = []


def register_command(func):
    """Register commands to be used lazily."""
    REGISTERED_COMMANDS.append(func)
    return func
