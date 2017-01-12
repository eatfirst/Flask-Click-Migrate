"""We extend the click group to always have the Flask app inside of it and the commands are executed in a context."""
import click
from click import Command
from click.decorators import _make_command
from flask import _app_ctx_stack

import flask_click_migrate.commands

from .utils import REGISTERED_COMMANDS

assert flask_click_migrate.commands


class MigrateGroup(click.Group):
    """A group that makes sure that current app is up."""

    def __init__(self, name='db', help_text='Perform database migrations', *args, **kwargs):
        """Init object.

        :param name: Name of the command group (default 'db').
        :param help_text: Help text.
        :param args: Arguments.
        :param kwargs: Keyword arguments.
        :return:
        """
        if 'migrate_instance' not in kwargs:
            raise RuntimeError('You must supply a Migrate instance.')

        self.migrate_instance = kwargs.pop('migrate_instance')
        super(MigrateGroup, self).__init__(name=name, help=help_text, *args, **kwargs)

        for func in REGISTERED_COMMANDS:
            self.add_command(_make_command(func, None, {}, cls=Command))

    def invoke(self, ctx):
        """Make sure that current app is up."""
        if _app_ctx_stack.top is not None:
            return super(MigrateGroup, self).invoke(ctx)
        with self.migrate_instance.app.app_context():
            return super(MigrateGroup, self).invoke(ctx)
