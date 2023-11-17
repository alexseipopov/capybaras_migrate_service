"""add Capybara table for all capybaras

Revision ID: d4143ce83705
Revises: 05cb8e9c3309
Create Date: 2023-11-17 17:50:27.011949

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4143ce83705'
down_revision: Union[str, None] = '05cb8e9c3309'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('capybara',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('school_user_id', sa.String(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('is_subscribe', sa.Boolean(), nullable=True),
    sa.Column('telegram_id', sa.Integer(), nullable=True),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('is_student', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('capybara')
    # ### end Alembic commands ###