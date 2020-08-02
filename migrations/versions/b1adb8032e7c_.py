"""empty message

Revision ID: b1adb8032e7c
Revises: f4e10d9eb79b
Create Date: 2020-08-02 09:40:23.405326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1adb8032e7c'
down_revision = 'f4e10d9eb79b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'dummy_col')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('dummy_col', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
