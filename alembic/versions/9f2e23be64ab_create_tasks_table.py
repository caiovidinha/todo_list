"""create tasks table

Revision ID: 9f2e23be64ab
Revises: 715cc5863676
Create Date: 2025-06-28 14:53:36.309941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = '9f2e23be64ab'
down_revision: Union[str, Sequence[str], None] = '715cc5863676'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'tasks',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('is_done', sa.Boolean(), nullable=False, server_default=sa.text('false')),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('user_id', UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
    )


def downgrade():
    op.drop_table('tasks')