"""create auth_user_roles table

Revision ID: 5ed212fe1cb3
Revises: 105e1e1e030f
Create Date: 2026-03-18 01:08:56.388915

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op



# revision identifiers, used by Alembic.
revision: str = '5ed212fe1cb3'
down_revision: Union[str, Sequence[str], None] = '105e1e1e030f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'auth_user_roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['auth_users.id'], ),
        sa.ForeignKeyConstraint(['role_id'], ['auth_roles.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('auth_user_roles')
