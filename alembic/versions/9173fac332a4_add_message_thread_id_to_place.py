"""Add message_thread_id to Place

Revision ID: 9173fac332a4
Revises: 333e7561401a
Create Date: 2024-06-17 12:07:54.328131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9173fac332a4'
down_revision: Union[str, None] = '333e7561401a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Add the column with nullable=True
    op.add_column('places', sa.Column('message_thread_id', sa.String(), nullable=True))

    # Update existing rows to set message_thread_id to 'General'
    op.execute("UPDATE places SET message_thread_id = 'General'")

    # Alter the column to set nullable=False
    op.alter_column('places', 'message_thread_id', nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('places', 'message_thread_id', nullable=True)
    op.drop_column('places', 'message_thread_id')
    # ### end Alembic commands ###