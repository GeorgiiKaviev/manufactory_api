"""dell_place_comment

Revision ID: 9440ff1e007b
Revises: f0726a962ad8
Create Date: 2024-06-06 17:48:47.655648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9440ff1e007b'
down_revision: Union[str, None] = 'f0726a962ad8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('places', 'comment')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('places', sa.Column('comment', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
