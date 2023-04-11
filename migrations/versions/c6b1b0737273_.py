"""empty message

Revision ID: c6b1b0737273
Revises: 
Create Date: 2023-04-11 07:24:22.534799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6b1b0737273'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('list_id', sa.Integer(), nullable=False))
        batch_op.alter_column('completed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
        batch_op.create_foreign_key(None, 'todolists', ['list_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('completed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
        batch_op.drop_column('list_id')

    # ### end Alembic commands ###
