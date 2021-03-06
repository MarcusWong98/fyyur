"""empty message

Revision ID: 03962cefd29e
Revises: 7a03a997ad17
Create Date: 2021-04-02 17:28:51.180653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03962cefd29e'
down_revision = '7a03a997ad17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Show_artist_id_fkey', 'Show', type_='foreignkey')
    op.drop_column('Show', 'artist_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('Show_artist_id_fkey', 'Show', 'Artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###
