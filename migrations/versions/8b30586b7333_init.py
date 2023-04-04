"""'Init'

Revision ID: 8b30586b7333
Revises: a035344fd005
Create Date: 2023-04-03 20:18:39.205670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b30586b7333'
down_revision = 'a035344fd005'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('contacts', 'phone',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'phone',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
