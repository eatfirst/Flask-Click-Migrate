# Flask Click Migrate
A simple click "addon" to add an alembic wrapper (basically a port from Flask-Migrate to click).

## Usage
```
Usage: manage.py db [OPTIONS] COMMAND [ARGS]...

  Perform database migrations

Options:
  --help  Show this message and exit.

Commands:
  branches   Show current branch points.
  current    Display the current revision for each...
  downgrade  Revert to a previous version.
  heads      Show current available heads in the script...
  history    List changeset scripts in chronological...
  init       Generate a new migration.
  merge      Merge two revisions together.
  migrate    Create a new migration based on SQLAlchemy...
  revision   Create a new revision file.
  show       Show the revision denoted by the given...
  stamp      'Stamp' the revision table with the given...
  upgrade    Upgrade to a later version.
```

## Configuring
```python
import click
from flask_click_migrate import Migrate, MigrateGroup

from my_app import app, db

migrate = Migrate(app, db)
migrate_command = MigrateGroup(migrate_instance=migrate)


@click.group()
def your_click_group():
    """Click group."""
    pass


your_click_group.add_command(migrate_command)

if __name__ == '__main__':
    your_click_group()
```
