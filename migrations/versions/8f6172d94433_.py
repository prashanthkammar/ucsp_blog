"""empty message

Revision ID: 8f6172d94433
Revises: bedb489957eb
Create Date: 2020-08-02 10:19:54.482229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f6172d94433'
down_revision = 'bedb489957eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'dummy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('dummy', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
