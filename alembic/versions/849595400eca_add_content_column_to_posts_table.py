"""add content column to posts table

Revision ID: 849595400eca
Revises: ae450a8e0807
Create Date: 2023-12-04 17:13:58.189882

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '849595400eca'
down_revision: Union[str, None] = 'ae450a8e0807'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
