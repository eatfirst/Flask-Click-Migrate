"""Flask Click Migrate."""
from .migrate import Migrate
from .group import MigrateGroup

__all__ = ('Migrate', 'MigrateGroup')
