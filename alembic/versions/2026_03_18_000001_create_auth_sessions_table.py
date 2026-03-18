"""create auth_sessions table

Revision ID: 5a18525e103a
Revises: 544fb240f0da
Create Date: 2026-03-18 01:09:21.660904

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op



# revision identifiers, used by Alembic.
revision: str = '5a18525e103a'
down_revision: Union[str, Sequence[str], None] = '544fb240f0da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'auth_sessions',
        sa.Column('session_key', sa.String(length=255), nullable=False),
        sa.Column('session_data', sa.Text(), nullable=False),
        sa.Column('expire_date', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('session_key')
    )
    op.create_index(op.f('ix_auth_sessions_expire_date'), 'auth_sessions', ['expire_date'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_auth_sessions_expire_date'), table_name='auth_sessions')
    op.drop_table('auth_sessions')
