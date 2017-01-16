"""Migrate commands using click."""

from alembic import __version__ as __alembic_version__

from .config import MigrateConfig

alembic_version = tuple([int(v) for v in __alembic_version__.split('.') if v.isnumeric()])


class Migrate(object):
    """Handle migration commands."""

    def __init__(self, app=None, database=None, directory='migrations'):
        """Init object.

        :param app: Application.
        :param database: Database.
        :param directory: Migration directory.
        :return:
        """
        self.app = app
        if app is not None and database is not None:
            self.init_app(app, database, directory)

    def init_app(self, app, database, directory='migrations'):  # pylint: disable=no-self-use
        """Init app.

        :param app: Application.
        :param database: Database.
        :param directory: Migration directory.
        """
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['migrate'] = MigrateConfig(database, directory)
