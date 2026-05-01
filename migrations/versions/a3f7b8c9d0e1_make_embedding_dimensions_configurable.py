"""make embedding dimensions configurable

This is a no-op migration that documents the change from hardcoded 1536-dimension
vectors to configurable dimensions via EMBEDDING.VECTOR_DIMENSIONS setting.

Existing deployments using the default 1536 dimensions are unaffected.
Changing EMBEDDING.VECTOR_DIMENSIONS to a different value requires either:
  - A fresh database, or
  - Manually altering the embedding columns and re-indexing all embeddings.

The Vector column type in SQLAlchemy models now reads from
settings.EMBEDDING.VECTOR_DIMENSIONS at class definition time. This migration
exists to mark the schema's logical dependency on that configuration value.

Revision ID: a3f7b8c9d0e1
Revises: e4eba9cfaa6f
Create Date: 2026-05-01 00:00:00.000000

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "a3f7b8c9d0e1"
down_revision: str | None = "e4eba9cfaa6f"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
