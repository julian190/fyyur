"""empty message

Revision ID: e4aae8e80cf7
Revises: c944ff83b062
Create Date: 2020-10-18 21:36:06.316248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4aae8e80cf7'
down_revision = 'c944ff83b062'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('start_time', sa.DateTime(), nullable=True))
    op.drop_column('Venue', 'upcoming')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('upcoming', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'start_time')
    # ### end Alembic commands ###
