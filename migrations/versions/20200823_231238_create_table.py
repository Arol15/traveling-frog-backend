"""create table

Revision ID: 202d695549f5
Revises: 72447bcb186b
Create Date: 2020-08-23 23:12:38.490391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '202d695549f5'
down_revision = '72447bcb186b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('placetypes', sa.Column('image', sa.String(length=50), nullable=True))
    op.alter_column('users', 'image',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'image',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('placetypes', 'image')
    # ### end Alembic commands ###
