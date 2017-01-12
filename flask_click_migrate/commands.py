"""Register all the commands that we will expose for the app."""
import os

import click
from alembic import command
from flask import current_app

from .config import AlembicConfig, _get_config
from .migrate import alembic_version
from .utils import register_command


@register_command
@click.option('-d', '--directory', default=None,
              help="migration script directory (default is 'migrations')")
def init(directory=None):
    """Generate a new migration.

    :param directory: Path to the migrations directory.
    """
    if directory is None:
        directory = current_app.extensions['migrate'].directory
    config = AlembicConfig()
    config.set_main_option('script_location', directory)
    config.config_file_name = os.path.join(directory, 'alembic.ini')
    command.init(config, directory, 'flask')


@register_command
@click.option('--rev-id', default=None, help='Specify a hardcoded revision id instead of generating one')
@click.option('--version-path', default=None,
              help='Specify specific path from config for version file')
@click.option('--branch-label', default=None,
              help='Specify a branch label to apply to the new revision')
@click.option('--splice', is_flag=True, default=False,
              help='Allow a non-head revision as the "head" to splice onto')
@click.option('--head', default='head',
              help='Specify head revision or <branchname>@head to base new revision on')
@click.option('--sql', is_flag=True, default=False,
              help="Don't emit SQL to database - dump to standard output instead")
@click.option('--autogenerate', is_flag=True, default=False,
              help='Populate revision script with candidate migration operations, based on comparison of database to '
                   'model')
@click.option('-m', '--message', default=None)
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def revision(directory=None, message=None, autogenerate=False, sql=False,
             head='head', splice=False, branch_label=None, version_path=None,
             rev_id=None):
    """Create a new revision file."""
    config = _get_config(directory)
    if alembic_version >= (0, 7, 0):
        command.revision(config, message, autogenerate=autogenerate, sql=sql,
                         head=head, splice=splice, branch_label=branch_label,
                         version_path=version_path, rev_id=rev_id)
    else:
        command.revision(config, message, autogenerate=autogenerate, sql=sql)


@register_command
@click.option('--rev-id', default=None, help='Specify a hardcoded revision id instead of generating one')
@click.option('--version-path', default=None, help='Specify specific path from config for version file')
@click.option('--branch-label', default=None, help='Specify a branch label to apply to the new revision')
@click.option('--splice', is_flag=True, default=False, help='Allow a non-head revision as the "head" to splice onto')
@click.option('--head', default='head', help='Specify head revision or <branchname>@head to base new revision on')
@click.option('--sql', is_flag=True, default=False, help="Don't emit SQL to database - dump to standard output instead")
@click.option('-m', '--message', default=None)
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def migrate(directory=None, message=None, sql=False, head='head', splice=False,
            branch_label=None, version_path=None, rev_id=None):
    """Create a new migration based on SQLAlchemy models and the database.

    Alias for 'revision --autogenerate'.
    """
    config = _get_config(directory)
    if alembic_version >= (0, 7, 0):
        command.revision(config, message, autogenerate=True, sql=sql, head=head,
                         splice=splice, branch_label=branch_label,
                         version_path=version_path, rev_id=rev_id)
    else:
        command.revision(config, message, autogenerate=True, sql=sql)


@register_command
@click.option('--rev-id', default=None, help='Specify a hardcoded revision id instead of generating one')
@click.option('--branch-label', default=None, help='Specify a branch label to apply to the new revision')
@click.option('-m', '--message', default=None)
@click.argument('revisions', nargs=-1)
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def merge(directory=None, revisions='', message=None, branch_label=None,
          rev_id=None):
    """Merge two revisions together.  Create a new migration file."""
    if alembic_version >= (0, 7, 0):
        config = _get_config(directory)
        command.merge(config, revisions, message=message,
                      branch_label=branch_label, rev_id=rev_id)
    else:
        raise RuntimeError('Alembic 0.7.0 or greater is required')


@register_command
@click.option('--tag', default=None, help="Arbitrary 'tag' name - can be used by custom env.py scripts")
@click.option('--sql', is_flag=True, default=False, help="Don't emit SQL to database - dump to standard output instead")
@click.argument('revision_id', default='head')
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def upgrade(directory=None, revision_id='head', sql=False, tag=None):
    """Upgrade to a later version."""
    config = _get_config(directory)
    command.upgrade(config, revision_id, sql=sql, tag=tag)


@register_command
@click.option('--tag', default=None, help="Arbitrary 'tag' name - can be used by custom env.py scripts")
@click.option('--sql', is_flag=True, default=False, help="Don't emit SQL to database - dump to standard output instead")
@click.argument('revision_id', default='-1')
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def downgrade(directory=None, revision_id='-1', sql=False, tag=None):
    """Revert to a previous version."""
    config = _get_config(directory)
    command.downgrade(config, revision_id, sql=sql, tag=tag)


@register_command
@click.argument('revision_id', default='head')
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def show(directory=None, revision_id='head'):
    """Show the revision denoted by the given symbol."""
    if alembic_version >= (0, 7, 0):
        config = _get_config(directory)
        command.show(config, revision_id)
    else:
        raise RuntimeError('Alembic 0.7.0 or greater is required')


@register_command
@click.option('-v', '--verbose', is_flag=True, default=False, help='Use more verbose output')
@click.option('-r', '--rev-range', default=None, help='Specify a revision range; format is [start]:[end]')
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def history(directory=None, rev_range=None, verbose=False):
    """List changeset scripts in chronological order."""
    config = _get_config(directory)
    if alembic_version >= (0, 7, 0):
        command.history(config, rev_range, verbose=verbose)
    else:
        command.history(config, rev_range)


@register_command
@click.option('--resolve-dependencies', is_flag=True, default=False, help='Treat dependency versions as down revisions')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Use more verbose output')
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def heads(directory=None, verbose=False, resolve_dependencies=False):
    """Show current available heads in the script directory."""
    if alembic_version >= (0, 7, 0):
        config = _get_config(directory)
        command.heads(config, verbose=verbose,
                      resolve_dependencies=resolve_dependencies)
    else:
        raise RuntimeError('Alembic 0.7.0 or greater is required')


@register_command
@click.option('-v', '--verbose', is_flag=True, default=False, help='Use more verbose output')
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def branches(directory=None, verbose=False):
    """Show current branch points."""
    config = _get_config(directory)
    if alembic_version >= (0, 7, 0):
        command.branches(config, verbose=verbose)
    else:
        command.branches(config)


@register_command
@click.option('--head-only', is_flag=True, default=False, help='Deprecated. Use --verbose for additional output')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Use more verbose output')
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def current(directory=None, verbose=False, head_only=False):
    """Display the current revision for each database."""
    config = _get_config(directory)
    if alembic_version >= (0, 7, 0):
        command.current(config, verbose=verbose, head_only=head_only)
    else:
        command.current(config)


@register_command
@click.option('--tag', default=None, help="Arbitrary 'tag' name - can be used by custom env.py scripts")
@click.option('--sql', is_flag=True, default=False, help="Don't emit SQL to database - dump to standard output instead")
@click.argument('revision_id', default='head')
@click.option('-d', '--directory', default=None, help="migration script directory (default is 'migrations')")
def stamp(directory=None, revision_id='head', sql=False, tag=None):
    """Stamp the revision table with the given revision; don't run any migrations."""
    config = _get_config(directory)
    command.stamp(config, revision_id, sql=sql, tag=tag)
