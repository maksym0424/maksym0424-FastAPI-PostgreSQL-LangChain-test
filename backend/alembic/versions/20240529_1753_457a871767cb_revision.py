"""revision

Revision ID: 457a871767cb
Revises: 
Create Date: 2024-05-29 17:53:01.391378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '457a871767cb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deals',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('merchant_id', sa.Integer(), nullable=True),
    sa.Column('merchant_name', sa.String(), nullable=True),
    sa.Column('network', sa.String(), nullable=True),
    sa.Column('network_id', sa.Integer(), nullable=True),
    sa.Column('homepage_url', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('merchant_about', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_deals_id'), 'deals', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_deals_id'), table_name='deals')
    op.drop_table('deals')
    # ### end Alembic commands ###
