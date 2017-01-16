"""Example of a manage file which would use flask click migrate."""
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
