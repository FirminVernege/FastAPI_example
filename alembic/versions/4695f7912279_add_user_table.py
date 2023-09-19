"""add user table

Revision ID: 4695f7912279
Revises: 6fdda30814fb
Create Date: 2023-09-19 14:45:41.628485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4695f7912279'
down_revision: Union[str, None] = '6fdda30814fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass


def downgrade():
    pass
