"""ediçao do tablename de Conta pra conta

Revision ID: 77ff1c821517
Revises: b33a6be60a68
Create Date: 2025-11-15 12:11:27.393269

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77ff1c821517'
down_revision: Union[str, Sequence[str], None] = 'b33a6be60a68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass
        #op.drop_table('Conta')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    pass
    # ### end Alembic commands ###
