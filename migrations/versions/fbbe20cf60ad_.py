"""empty message

Revision ID: fbbe20cf60ad
Revises: 9d6df3c03e27
Create Date: 2020-10-18 22:11:13.835661

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fbbe20cf60ad'
down_revision = '9d6df3c03e27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'start_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('start_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    # ### end Alembic commands ###