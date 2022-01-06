"""Added schedule table

Revision ID: 5fe4b2ea4c02
Revises: ce62ff4e5d7a
Create Date: 2022-01-06 01:43:06.256725

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fe4b2ea4c02'
down_revision = 'ce62ff4e5d7a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'schedule',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('tournament', sa.String(), nullable=False),
        sa.Column('location', sa.String(), nullable=False),
        sa.Column('course_name', sa.String(), nullable=False),
        sa.Column('tournament_id', sa.String(length=4), nullable=False),
        sa.Column('start_date', sa.Date(), nullable=False),
        sa.Column('end_date', sa.Date(), nullable=False),
        sa.Column('schedule_year', sa.Integer(), nullable=False),
        sa.Column('leaderboard_url', sa.String(), nullable=True),
        sa.Column('notes', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('tournament_id', 'schedule_year')
    )


def downgrade():
    op.drop_table('schedule')
