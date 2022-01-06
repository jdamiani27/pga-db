"""Added api_requests table

Revision ID: ce62ff4e5d7a
Revises: 
Create Date: 2021-10-04 22:36:43.399105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce62ff4e5d7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'api_requests',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('request_dtm', sa.DateTime(), nullable=True),
        sa.Column('status_code', sa.Integer(), nullable=True),
        sa.Column('response_text', sa.String(), nullable=True),
        sa.Column('response_json', sa.JSON(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('api_requests')
