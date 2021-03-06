"""empty message

Revision ID: 7a03a997ad17
Revises: 347e5f57a535
Create Date: 2021-03-29 23:08:06.362931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a03a997ad17'
down_revision = '347e5f57a535'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('Show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('Show', 'id')
    # ### end Alembic commands ###
