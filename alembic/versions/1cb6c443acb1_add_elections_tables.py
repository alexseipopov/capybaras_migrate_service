"""add Elections tables

Revision ID: 1cb6c443acb1
Revises: d4143ce83705
Create Date: 2023-12-12 07:49:35.287508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1cb6c443acb1'
down_revision: Union[str, None] = 'd4143ce83705'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tribe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('school_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('election',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tribe_id', sa.Integer(), nullable=False),
    sa.Column('time_start_collection', sa.DateTime(), nullable=False, comment='Время начала выдвижения кандидатов'),
    sa.Column('time_finish_collection', sa.DateTime(), nullable=False, comment='Время окончания выдвижения кандидатов'),
    sa.Column('time_start_voting', sa.DateTime(), nullable=False, comment='Время начала голосования'),
    sa.Column('time_finish_voting', sa.DateTime(), nullable=False, comment='Время окончания голосования'),
    sa.Column('is_finished', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['tribe_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('candidate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('election_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('is_approved', sa.Boolean(), nullable=True),
    sa.Column('about', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['election_id'], ['election.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['capybara.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('election_id', sa.Integer(), nullable=False),
    sa.Column('voter_id', sa.Integer(), nullable=False),
    sa.Column('candidate_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['candidate_id'], ['candidate.id'], ),
    sa.ForeignKeyConstraint(['election_id'], ['election.id'], ),
    sa.ForeignKeyConstraint(['voter_id'], ['capybara.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vote')
    op.drop_table('candidate')
    op.drop_table('election')
    op.drop_table('tribe')
    # ### end Alembic commands ###