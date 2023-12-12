"""empty message

Revision ID: 3dca02511772
Revises: 848bddc4be6d
Create Date: 2023-12-11 22:32:29.838281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dca02511772'
down_revision = '848bddc4be6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('countries_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'countries', ['countries_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('countries_id')

    # ### end Alembic commands ###
