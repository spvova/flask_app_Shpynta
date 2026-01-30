"""Add legacy data products

Revision ID: 11972f1c7d74
Revises: b93e00de8c5f
Create Date: 2026-01-28 16:48:29.791133

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import table, column


# revision identifiers, used by Alembic.
revision = '11972f1c7d74'
down_revision = 'b93e00de8c5f'
branch_labels = None
depends_on = None


def upgrade():
    # --- Описи таблиць для bulk_insert ---
    categories_table = table('categories', column('id', sa.Integer), column('name', sa.String))

    products_table = table('products',
        column('name', sa.String),
        column('price', sa.Float),
        column('active', sa.Boolean),
        column('category_id', sa.Integer),
    )

    # --- Вставка нової категорії Laptops ---
    op.bulk_insert(categories_table, [
        {'name': 'Laptops'},
    ])

    # --- Вставка старих продуктів ---
    op.bulk_insert(products_table, [
        {'name': 'iPhone 15', 'price': 999.99, 'active': True, 'category_id': None},
        {'name': 'Gaming Laptop', 'price': 1500.00, 'active': False, 'category_id': 4},
        {'name': 'Pc', 'price': 700.0, 'active': True, 'category_id': None},
        {'name': 'MAC', 'price': 500.0, 'active': True, 'category_id': None},
    ])


def downgrade():
    # Видаляємо старі продукти
    op.execute("""
        DELETE FROM products
        WHERE name IN ('iPhone 15', 'Gaming Laptop', 'Pc', 'MAC');
    """)

    # Видаляємо категорію Laptops
    op.execute("""
        DELETE FROM categories
        WHERE name = 'Laptops';
    """)
