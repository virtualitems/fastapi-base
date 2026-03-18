"""create auth_role_permissions table

Revision ID: 544fb240f0da
Revises: 52356f3b1cff
Create Date: 2026-03-18 01:09:10.546556

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op



# revision identifiers, used by Alembic.
revision: str = '544fb240f0da'
down_revision: Union[str, Sequence[str], None] = '52356f3b1cff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'auth_role_permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('permission_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['role_id'], ['auth_roles.id'], ),
        sa.ForeignKeyConstraint(['permission_id'], ['auth_permissions.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('auth_role_permissions')
