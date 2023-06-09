"""empty message

Revision ID: 188829b6f2c4
Revises: e8048ce8889a
Create Date: 2023-04-04 23:02:50.353005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '188829b6f2c4'
down_revision = 'e8048ce8889a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('job', schema=None) as batch_op:
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###
