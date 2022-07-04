"""create user column in books table

Revision ID: 991de3c50d87
Revises: 
Create Date: 2022-07-04 15:31:40.107406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '991de3c50d87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('books', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('books_users_fk', source_table='books', referent_table='users', local_cols=['user_id'], remote_cols=['id'],
    ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('books_users_fk', table_name='books')
    op.drop_column('books', 'user_id')
