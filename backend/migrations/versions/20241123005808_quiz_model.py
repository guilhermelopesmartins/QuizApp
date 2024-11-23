"""Quiz model

Revision ID: 34771b3dc3cf
Revises: 0734dbd87947
Create Date: 2024-11-23 00:58:08.115289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34771b3dc3cf'
down_revision = '0734dbd87947'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "quizzes",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("category", sa.String(length=255), nullable=False),
        sa.Column("difficulty", sa.String(length=255), nullable=False),
        sa.Column("owner_id", sa.BigInteger(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["owner_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("uuid"),
    )



def downgrade():
    op.drop_table("quizzes")
