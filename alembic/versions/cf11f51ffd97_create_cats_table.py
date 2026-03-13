"""create cats table

Revision ID: cf11f51ffd97
Revises: 
Create Date: 2026-03-13 14:37:10.198525

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'cf11f51ffd97'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "cats",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("cats")
