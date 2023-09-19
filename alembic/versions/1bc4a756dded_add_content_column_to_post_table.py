"""add content column to post table

Revision ID: 1bc4a756dded
Revises: 2273a91abe7b
Create Date: 2023-09-19 14:19:33.324234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1bc4a756dded'
down_revision: Union[str, None] = '2273a91abe7b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
