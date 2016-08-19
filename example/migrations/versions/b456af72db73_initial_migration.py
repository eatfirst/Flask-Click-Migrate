"""Just a sample generated using the click migration script.

Revision ID: b456af72db73
Revises:
Create Date: 2016-08-19 23:23:00.012162

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b456af72db73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'my_model',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('phone', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('my_model')
