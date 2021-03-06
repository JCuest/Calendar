"""friend_request table

Revision ID: a09c1bfe00e7
Revises: dbf9147e5f70
Create Date: 2020-02-05 00:51:21.539649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a09c1bfe00e7'
down_revision = 'dbf9147e5f70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friend_request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user1', sa.Integer(), nullable=True),
    sa.Column('user2', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user1'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user2'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('friend_request')
    # ### end Alembic commands ###
