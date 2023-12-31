"""fix mistake foreign key for election

Revision ID: dd6174bd3d8c
Revises: 1cb6c443acb1
Create Date: 2023-12-12 08:06:34.840148

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd6174bd3d8c'
down_revision: Union[str, None] = '1cb6c443acb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('election_tribe_id_fkey', 'election', type_='foreignkey')
    op.create_foreign_key(None, 'election', 'tribe', ['tribe_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'election', type_='foreignkey')
    op.create_foreign_key('election_tribe_id_fkey', 'election', 'user', ['tribe_id'], ['id'])
    # ### end Alembic commands ###
