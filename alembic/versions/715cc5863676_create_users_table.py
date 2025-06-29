"""create users table

Revision ID: 715cc5863676
Revises: 
Create Date: 2025-06-28 14:51:57.227676

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision: str = '715cc5863676'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    op.create_table(
        'users',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
        sa.Column('username', sa.String(), unique=True, index=True, nullable=False),
        sa.Column('token', sa.String(), unique=True, index=True, nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False)
    )


def downgrade():
    op.drop_table('users')
