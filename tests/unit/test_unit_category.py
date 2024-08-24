
from app.schemas.category_schema import CategoryCreate


def test_unit_schema_category_validation():
    valid_data = {"name": "test_category", "slug": "test_slug"}
    category = CategoryCreate(**valid_data)
    assert category.name == "test_category"
    assert category.slug == "test_slug"