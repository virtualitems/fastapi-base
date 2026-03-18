"""create auth_permissions table

Revision ID: 105e1e1e030f
Revises: da61bcb26bc2
Create Date: 2026-03-18 01:08:49.670378

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op



# revision identifiers, used by Alembic.
revision: str = '105e1e1e030f'
down_revision: Union[str, Sequence[str], None] = 'da61bcb26bc2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'auth_permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('slug', sa.String(length=100), nullable=False),
        sa.Column('description', sa.String(length=500), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )
    op.create_index(op.f('ix_auth_permissions_id'), 'auth_permissions', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_auth_permissions_id'), table_name='auth_permissions')
    op.drop_table('auth_permissions')
