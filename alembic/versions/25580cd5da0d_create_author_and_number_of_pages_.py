"""create author and number_of_pages columns in books

Revision ID: 25580cd5da0d
Revises: 991de3c50d87
Create Date: 2022-07-05 15:08:35.320378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25580cd5da0d'
down_revision = '991de3c50d87'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('books', sa.Column('author', sa.String, nullable=True))
    op.add_column('books', sa.Column('number_of_pages', sa.Integer, nullable=True))
    


def downgrade() -> None:
    op.drop_column('books', 'author')
    op.drop_column('books', 'number_of_pages')
