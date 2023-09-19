"""empty message

Revision ID: 6fdda30814fb
Revises: 1bc4a756dded, 6d408a975b27
Create Date: 2023-09-19 14:45:34.920364

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fdda30814fb'
down_revision: Union[str, None] = ('1bc4a756dded', '6d408a975b27')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
