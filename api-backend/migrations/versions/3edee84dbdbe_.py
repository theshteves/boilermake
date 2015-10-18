"""empty message

Revision ID: 3edee84dbdbe
Revises: 5314306ceea4
Create Date: 2015-10-17 23:55:01.000890

"""

# revision identifiers, used by Alembic.
revision = '3edee84dbdbe'
down_revision = '5314306ceea4'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('site_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('reply_to', sa.Integer(), nullable=True),
    sa.Column('time_stamp', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['site_id'], ['sites.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_site_id'), 'comments', ['site_id'], unique=False)
    op.create_index(op.f('ix_comments_user_id'), 'comments', ['user_id'], unique=False)
    op.add_column(u'votes', sa.Column('time_stamp', sa.Integer(), nullable=True))
    op.drop_column(u'votes', 'date')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'votes', sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column(u'votes', 'time_stamp')
    op.drop_index(op.f('ix_comments_user_id'), table_name='comments')
    op.drop_index(op.f('ix_comments_site_id'), table_name='comments')
    op.drop_table('comments')
    ### end Alembic commands ###
