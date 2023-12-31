"""empty message

Revision ID: 824aa798323b
Revises: f9d6735d3783
Create Date: 2023-06-23 14:47:34.661396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '824aa798323b'
down_revision = 'f9d6735d3783'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authorization_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('code', sa.String(length=120), nullable=False),
    sa.Column('client_id', sa.String(length=48), nullable=True),
    sa.Column('redirect_uri', sa.Text(), nullable=True),
    sa.Column('response_type', sa.Text(), nullable=True),
    sa.Column('scope', sa.Text(), nullable=True),
    sa.Column('nonce', sa.Text(), nullable=True),
    sa.Column('auth_time', sa.Integer(), nullable=False),
    sa.Column('code_challenge', sa.Text(), nullable=True),
    sa.Column('code_challenge_method', sa.String(length=48), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('authorization_code')
    # ### end Alembic commands ###
