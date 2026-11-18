
from enum import StrEnum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Noor Foods Products API")


# 1. Product categories
class Category(StrEnum):
    rice = "rice"
    oil = "oil"
    spices = "spices"
    flour = "flour"


# 2. Models
class NewProduct(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    price: int = Field(gt=0)
    category: Category
    in_stock: int = Field(default=0, ge=0)


class Product(NewProduct):
    id: str


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=80)
    price: int | None = Field(default=None, gt=0)
    category: Category | None = None
    in_stock: int | None = Field(default=None, ge=0)


# 3. Summary response model
class ProductSummary(BaseModel):
    product_count: int
    stock_value: int
    by_category: dict[str, int]


# 4. Initial products
products = {
    "P101": Product(
        id="P101",
        name="Basmati rice 5kg",
        price=2400,
        category=Category.rice,
        in_stock=40,
    ),
    "P102": Product(
        id="P102",
        name="Cooking oil 1L",
        price=650,
        category=Category.oil,
        in_stock=0,
    ),
    "P103": Product(
        id="P103",
        name="Red chilli powder 200g",
        price=320,
        category=Category.spices,
        in_stock=120,
    ),
    "P104": Product(
        id="P104",
        name="Sella rice 10kg",
        price=4600,
        category=Category.rice,
        in_stock=15,
    ),
}

next_product_id = 105


# 5. Shared product lookup
def find_product(product_id: str) -> Product:
    product = products.get(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail=f"Product {product_id} not found",
        )

    return product


# 6. GET all products with filters
@app.get("/products")
def get_products(
    category: Category | None = None,
    max_price: int | None = None,
    limit: int = 10,
) -> list[Product]:
    result = list(products.values())

    if category is not None:
        result = [
            product for product in result
            if product.category == category
        ]

    if max_price is not None:
        result = [
            product for product in result
            if product.price <= max_price
        ]

    return result[:limit]


# 7. GET one product
@app.get("/products/{product_id}")
def get_product(product_id: str) -> Product:
    return find_product(product_id)


# 8. POST create product
@app.post("/products", status_code=201)
def create_product(new_product: NewProduct) -> Product:
    global next_product_id

    product_id = f"P{next_product_id}"

    product = Product(
        id=product_id,
        **new_product.model_dump(),
    )

    products[product_id] = product
    next_product_id += 1

    return product


# 9. PATCH update product
@app.patch("/products/{product_id}")
def update_product(
    product_id: str,
    product_update: ProductUpdate,
) -> Product:
    product = find_product(product_id)

    update_data = product_update.model_dump(exclude_unset=True)

    updated_product = product.model_copy(update=update_data)

    products[product_id] = updated_product

    return updated_product


# 10. DELETE product with stock protection
@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: str) -> None:
    product = find_product(product_id)

    if product.in_stock > 0:
        raise HTTPException(
            status_code=409,
            detail=(
                f"Cannot delete product {product_id}: "
                f"{product.in_stock} items are still in stock."
            ),
        )

    del products[product_id]


# 11. GET product summary
@app.get("/summary")
def get_summary() -> ProductSummary:
    product_count = len(products)

    stock_value = sum(
        product.price * product.in_stock
        for product in products.values()
    )

    by_category = {}

    for category in Category:
        by_category[category.value] = sum(
            1
            for product in products.values()
            if product.category == category
        )

    return ProductSummary(
        product_count=product_count,
        stock_value=stock_value,
        by_category={
            category: count
            for category, count in by_category.items()
            if count > 0
        },
    )


# 12. Health check
@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
