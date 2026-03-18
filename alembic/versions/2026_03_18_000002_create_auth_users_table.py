"""create auth_users table

Revision ID: 6cf9f5ecb27c
Revises:
Create Date: 2026-03-18 01:08:31.445945

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op



# revision identifiers, used by Alembic.
revision: str = '6cf9f5ecb27c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'auth_users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('slug', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=300), nullable=False),
        sa.Column('password', sa.String(length=300), nullable=False),
        sa.Column('last_login', sa.DateTime(), nullable=True),
        sa.Column('jwt_version', sa.String(length=15), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug'),
        sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_auth_users_id'), 'auth_users', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_auth_users_id'), table_name='auth_users')
    op.drop_table('auth_users')
