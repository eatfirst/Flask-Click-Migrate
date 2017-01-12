"""Configurable parameters should be here."""
import os

from alembic.config import Config as OriginalAlembicConfig
from flask import current_app


class MigrateConfig(object):
    """Configuration for the migration."""

    def __init__(self, database, directory):
        """Initialize the config."""
        self.database = database
        self.directory = directory

    @property
    def metadata(self):
        """Keep backwards compatibility.

        In old releases, app.extensions['migrate'] was set to db,
        and env.py accessed app.extensions['migrate'].metadata.
        """
        return self.database.metadata


class AlembicConfig(OriginalAlembicConfig):
    """Alembic configuration class."""

    def get_template_directory(self):
        """Return the template directory."""
        package_dir = os.path.abspath(os.path.dirname(__file__))
        return os.path.join(package_dir, 'templates')


def _get_config(directory):
    """Read the Alembic config file in the directory.

    :param directory: Directory for the config.ini file.
    :return:
    """
    if directory is None:
        directory = current_app.extensions['migrate'].directory
    possible_config_paths = (os.path.join(directory, 'alembic.ini'), os.path.join(directory, '..', 'alembic.ini'))
    for path in possible_config_paths:
        if os.path.exists(path):
            config_file = path
            break
    else:
        raise RuntimeError('alembic.ini was not found in these directories {!r}'.format(possible_config_paths))
    config = AlembicConfig(config_file)
    config.set_main_option('script_location', directory)
    return config
