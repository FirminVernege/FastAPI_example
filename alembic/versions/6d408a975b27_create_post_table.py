"""create post table

Revision ID: 6d408a975b27
Revises: 2273a91abe7b
Create Date: 2023-09-19 14:02:52.300084

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d408a975b27'
down_revision: Union[str, None] = '2273a91abe7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
