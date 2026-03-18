"""create auth_user_permissions table

Revision ID: 52356f3b1cff
Revises: 5ed212fe1cb3
Create Date: 2026-03-18 01:09:02.712730

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op



# revision identifiers, used by Alembic.
revision: str = '52356f3b1cff'
down_revision: Union[str, Sequence[str], None] = '5ed212fe1cb3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'auth_user_permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('permission_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['auth_users.id'], ),
        sa.ForeignKeyConstraint(['permission_id'], ['auth_permissions.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('auth_user_permissions')
