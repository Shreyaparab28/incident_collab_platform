"""Add created_by to incidents

Revision ID: 76526cd238fa
Revises: d4998ae9471e
Create Date: 2025-07-06 17:01:25.456071

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76526cd238fa'
down_revision: Union[str, Sequence[str], None] = 'd4998ae9471e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    def upgrade() -> None:
        op.add_column('incidents', sa.Column('created_by', sa.String(), nullable=True))



def downgrade() -> None:
    """Downgrade schema."""
    def downgrade() -> None:
        op.drop_column('incidents', 'created_by')

