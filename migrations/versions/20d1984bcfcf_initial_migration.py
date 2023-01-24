"""Initial migration

Revision ID: 20d1984bcfcf
Revises: 
Create Date: 2023-01-24 16:04:46.475166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20d1984bcfcf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=100), nullable=False))
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###