# from fastapi import FastAPI

# app = FastAPI(title="Noor Foods Orders API")


# @app.get("/")
# def read_root() -> dict[str, str]:
#     return {"app": "Noor Foods Orders API", "docs": "/docs"}


# Exercise

# Practice: your first routes

# 1. A health check. Add a route GET /health that returns {"status": "ok"}. Deployment platforms and monitoring tools call a route like this to check your app is alive. Check it in the browser and on the docs page.

# @app.get("/health")
# def read_root() -> dict[str, str]:
#     return {"status": "ok", "docs": "/docs"}


# 2. A list. Add a route GET /products that returns a list of three Noor Foods products, each a dictionary with name and price. What return type should the function have? What does the docs page show for it?

# @app.get("/products")
# def read_root() -> list[dict]:
#     return [
#   {"name": "Rice", "price": 2500},
#   {"name": "Cooking Oil", "price": 1800},
#   {"name": "Flour", "price": 1200}
# ]


# 3. Break it. Change the path of /health to health, without the slash, and save. What happens in the terminal? Put the slash back.

# @app.get("/health")
# def read_root() -> dict[str, str]:
#     return {"status": "ok", "docs": "/docs"}


# ROUTES AND PARAMETERS

# from fastapi import FastAPI, HTTPException

# app = FastAPI(title="Noor Foods Orders API")

# ORDERS = {
#     "A101": {
#         "id": "A101",
#         "customer": "Noor Foods",
#         "total": 4500,
#         "status": "pending",
#     },
#     "A102": {
#         "id": "A102",
#         "customer": "Bilal Traders",
#         "total": 12800,
#         "status": "delivered",
#     },
#     "A103": {
#         "id": "A103",
#         "customer": "Karachi Crafts",
#         "total": 2300,
#         "status": "pending",
#     },
# }


# @app.get("/orders")
# def list_orders() -> list[dict]:
#     return list(ORDERS.values())


# Sending a 404
# @app.get("/orders/{order_id}")
# def get_order(order_id: str) -> dict:
#     if order_id not in ORDERS:
#         raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
#     return ORDERS[order_id]


# Query parameters
# @app.get("/orders")
# def list_orders(limit: int = 10) -> list[dict]:
#     return list(ORDERS.values())[:limit]


# # Filtering with an enum
# from enum import StrEnum

# from fastapi import FastAPI, HTTPException

# app = FastAPI(title="Noor Foods Orders API")

# ORDERS = {
#     "A101": {
#         "id": "A101",
#         "customer": "Noor Foods",
#         "total": 4500,
#         "status": "pending",
#     },
#     "A102": {
#         "id": "A102",
#         "customer": "Bilal Traders",
#         "total": 12800,
#         "status": "delivered",
#     },
#     "A103": {
#         "id": "A103",
#         "customer": "Karachi Crafts",
#         "total": 2300,
#         "status": "pending",
#     },
# }

# class OrderStatus(StrEnum):
#     PENDING = "pending"
#     DELIVERED = "delivered"

# # ... ORDERS and the other routes stay the same ...

# @app.get("/orders")
# def list_orders(status: OrderStatus | None = None, limit: int = 10) -> list[dict]:
#     orders = []
#     for order in ORDERS.values():
#         if status is None or order["status"] == status:
#             orders.append(order)
#     return orders[:limit]


# Exercise

# Practice: routes and parameters

# 1. Filter by customer. Add an optional customer query parameter to GET /orders that returns only that customer's orders. Make it ignore capital letters, so ?customer=noor foods finds Noor Foods.

# from fastapi import FastAPI

# app = FastAPI(title="Noor Foods Orders API")

# ORDERS = {
#     "A101": {
#         "id": "A101",
#         "customer": "Noor Foods",
#         "total": 4500,
#         "status": "pending",
#     },
#     "A102": {
#         "id": "A102",
#         "customer": "Bilal Traders",
#         "total": 12800,
#         "status": "delivered",
#     },
#     "A103": {
#         "id": "A103",
#         "customer": "Karachi Crafts",
#         "total": 2300,
#         "status": "pending",
#     },
# }


# @app.get("/orders")
# def list_orders(
#     customer: str | None = None,
#     limit: int = 10,
# ) -> list[dict]:

#     orders = []

#     for order in ORDERS.values():
#         if (
#             customer is None
#             or order["customer"].lower() == customer.lower()
#         ):
#             orders.append(order)

#     return orders[:limit]


# 2. Orders above a total. Add an optional min_total query parameter, an int, that returns only orders with a total of at least that amount. Check that ?min_total=4500 includes A101 and that ?min_total=lots gives a 422. Check that it works together with status.


# from enum import StrEnum

# from fastapi import FastAPI

# app = FastAPI(title="Noor Foods Orders API")

# ORDERS = {
#     "A101": {
#         "id": "A101",
#         "customer": "Noor Foods",
#         "total": 4500,
#         "status": "pending",
#     },
#     "A102": {
#         "id": "A102",
#         "customer": "Bilal Traders",
#         "total": 12800,
#         "status": "delivered",
#     },
#     "A103": {
#         "id": "A103",
#         "customer": "Karachi Crafts",
#         "total": 2300,
#         "status": "pending",
#     },
# }


# class OrderStatus(StrEnum):
#     PENDING = "pending"
#     DELIVERED = "delivered"


# @app.get("/orders")
# def list_orders(
#     customer: str | None = None,
#     status: OrderStatus | None = None,
#     min_total: int | None = None,
#     limit: int = 10,
# ) -> list[dict]:

#     orders = []

#     for order in ORDERS.values():
#         if (
#             (customer is None or order["customer"].lower() == customer.lower())
#             and (status is None or order["status"] == status)
#             and (min_total is None or order["total"] >= min_total)
#         ):
#             orders.append(order)

#     return orders[:limit]


# 3. A customer's orders. Add a route GET /customers/{name}/orders that returns all orders for one customer. If the customer has no orders, return a 404 with a message that names the customer. When would you use this route instead of GET /orders?customer=...?


# from enum import StrEnum

# from fastapi import FastAPI, HTTPException

# app = FastAPI(title="Noor Foods Orders API")

# ORDERS = {
#     "A101": {
# all orders with optional filters

# @app.get("/customers/{name}/orders")
# def customer_orders(name: str) -> list[dict]:
#     orders = []

#     for order in ORDERS.values():
#         if order["customer"].lower() == name.lower():
#             orders.append(order)

#     if not orders:
#         raise HTTPException(
#             status_code=404,
#             detail=f"No orders found for customer {name}"
#         )

#     return orders


# Request bodies and validation
# from enum import StrEnum

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field

# app = FastAPI(title="Noor Foods Orders API")


# class OrderStatus(StrEnum):
#     PENDING = "pending"
#     DELIVERED = "delivered"


# class NewOrder(BaseModel):
#     customer: str = Field(min_length=2, max_length=120)
#     total: int = Field(gt=0)


# class Order(BaseModel):
#     id: str
#     customer: str
#     total: int
#     status: OrderStatus


# ORDERS = {
#     "A101": Order(
#         id="A101",
#         customer="Noor Foods",
#         total=4500,
#         status=OrderStatus.PENDING,
#     ),
#     "A102": Order(
#         id="A102",
#         customer="Bilal Traders",
#         total=12800,
#         status=OrderStatus.DELIVERED,
#     ),
#     "A103": Order(
#         id="A103",
#         customer="Karachi Crafts",
#         total=2300,
#         status=OrderStatus.PENDING,
#     ),
# }


# @app.get("/")
# def read_root() -> dict[str, str]:
#     return {"app": "Noor Foods Orders API", "docs": "/docs"}


# @app.get("/orders")
# def list_orders(
#     status: OrderStatus | None = None, limit: int = 10
# ) -> list[Order]:
#     orders = []
#     for order in ORDERS.values():
#         if status is None or order.status == status:
#             orders.append(order)
#     return orders[:limit]


# @app.get("/orders/{order_id}")
# def get_order(order_id: str) -> Order:
#     if order_id not in ORDERS:
#         raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
#     return ORDERS[order_id]


# @app.post("/orders", status_code=201)
# def create_order(new_order: NewOrder) -> Order:
#     order_id = f"A{101 + len(ORDERS)}"
#     order = Order(
#         id=order_id,
#         customer=new_order.customer,
#         total=new_order.total,
#         status=OrderStatus.PENDING,
#     )
#     ORDERS[order_id] = order
#     return order


# Exercise

# Practice: request bodies

# 1. A city for each order. Add an optional city field to both models, at most 50 characters, and include it when you create an order. Create an order with a city and one without it on the docs page. What does the response show for the order without a city?


# from enum import StrEnum

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field

# app = FastAPI(title="Noor Foods Orders API")


# class OrderStatus(StrEnum):
#     PENDING = "pending"
#     DELIVERED = "delivered"


# # Data sent by the client
# class NewOrder(BaseModel):
#     customer: str = Field(min_length=2, max_length=120)
#     total: int = Field(gt=0)
#     city: str | None = Field(default=None, max_length=50)


# # Complete order stored and returned by the API
# class Order(BaseModel):
#     id: str
#     customer: str
#     total: int
#     status: OrderStatus
#     city: str | None = None


# ORDERS = {
#     "A101": Order(
#         id="A101",
#         customer="Noor Foods",
#         total=4500,
#         status=OrderStatus.PENDING,
#     ),
#     "A102": Order(
#         id="A102",
#         customer="Bilal Traders",
#         total=12800,
#         status=OrderStatus.DELIVERED,
#     ),
#     "A103": Order(
#         id="A103",
#         customer="Karachi Crafts",
#         total=2300,
#         status=OrderStatus.PENDING,
#     ),
# }


# @app.post("/orders", status_code=201)
# def create_order(new_order: NewOrder) -> Order:
#     order_id = f"A{101 + len(ORDERS)}"

#     order = Order(
#         id=order_id,
#         customer=new_order.customer,
#         total=new_order.total,
#         status=OrderStatus.PENDING,
#         city=new_order.city,
#     )

#     ORDERS[order_id] = order
#     return order


# 2. A delivery note. Add a note field to NewOrder that's optional and at most 200 characters, and store it on the order. Send a note that's too long. What does loc say in the 422?


# from enum import StrEnum

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field

# app = FastAPI(title="Noor Foods Orders API")


# class OrderStatus(StrEnum):
#     PENDING = "pending"
#     DELIVERED = "delivered"


# # Data sent by the client
# class NewOrder(BaseModel):
#     customer: str = Field(min_length=2, max_length=120)
#     total: int = Field(gt=0)
#     city: str | None = Field(default=None, max_length=50)


# # Complete order stored and returned by the API
# class Order(BaseModel):
#     id: str
#     customer: str
#     total: int
#     status: OrderStatus
#     city: str | None = None


# ORDERS = {
#     "A101": Order(
#         id="A101",
#         customer="Noor Foods",
#         total=4500,
#         status=OrderStatus.PENDING,
#     ),
#     "A102": Order(
#         id="A102",
#         customer="Bilal Traders",
#         total=12800,
#         status=OrderStatus.DELIVERED,
#     ),
#     "A103": Order(
#         id="A103",
#         customer="Karachi Crafts",
#         total=2300,
#         status=OrderStatus.PENDING,
#     ),
# }

# @app.post("/orders", status_code=201)
# def create_order(new_order: NewOrder) -> Order:
#     order_id = f"A{101 + len(ORDERS)}"

#     order = Order(
#         id=order_id,
#         customer=new_order.customer,
#         total=new_order.total,
#         status=OrderStatus.PENDING,
#         city=new_order.city,
#     )

#     ORDERS[order_id] = order
#     return order


# Exercise

# Practice: CRUD

# 1. A typo in a total. Use PATCH to change only A102's total to 13000. Check that its customer and status didn't change. Then send {"total": -5}. What comes back, and did A102 change?


# from enum import StrEnum

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field

# app = FastAPI(title="Noor Foods Orders API")


# class OrderStatus(StrEnum):
#     PENDING = "pending"
#     DELIVERED = "delivered"


# # Data sent by the client when creating an order
# class NewOrder(BaseModel):
#     customer: str = Field(min_length=2, max_length=120)
#     total: int = Field(gt=0)
#     city: str | None = Field(default=None, max_length=50)


# # Complete order stored and returned by the API
# class Order(BaseModel):
#     id: str
#     customer: str
#     total: int
#     status: OrderStatus
#     city: str | None = None


# # Data sent by the client when updating an order
# class OrderUpdate(BaseModel):
#     total: int | None = Field(default=None, gt=0)


# ORDERS = {
#     "A101": Order(
#         id="A101",
#         customer="Noor Foods",
#         total=4500,
#         status=OrderStatus.PENDING,
#     ),
#     "A102": Order(
#         id="A102",
#         customer="Bilal Traders",
#         total=12800,
#         status=OrderStatus.DELIVERED,
#     ),
#     "A103": Order(
#         id="A103",
#         customer="Karachi Crafts",
#         total=2300,
#         status=OrderStatus.PENDING,
#     ),
# }


# @app.patch("/orders/{order_id}")
# def update_order(order_id: str, updates: OrderUpdate) -> Order:
#     if order_id not in ORDERS:
#         raise HTTPException(
#             status_code=404,
#             detail=f"Order {order_id} not found",
#         )

#     existing_order = ORDERS[order_id]

#     updated_order = existing_order.model_copy(
#         update=updates.model_dump(exclude_unset=True)
#     )

#     ORDERS[order_id] = updated_order

#     return updated_order


# # 2. An empty update. Send PATCH /orders/A101 with the body {}. What happens, and why? Should an empty update be an error? Make a case for each answer.

# from enum import StrEnum

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field

# app = FastAPI(title="Noor Foods Orders API")


# class OrderStatus(StrEnum):
#     PENDING = "pending"
#     DELIVERED = "delivered"


# # Data sent by the client when creating an order
# class NewOrder(BaseModel):
#     customer: str = Field(min_length=2, max_length=120)
#     total: int = Field(gt=0)
#     city: str | None = Field(default=None, max_length=50)


# # Complete order stored and returned by the API
# class Order(BaseModel):
#     id: str
#     customer: str
#     total: int
#     status: OrderStatus
#     city: str | None = None


# # Data sent by the client when updating an order
# class OrderUpdate(BaseModel):
#     total: int | None = Field(default=None, gt=0)


# ORDERS = {
#     "A101": Order(
#         id="A101",
#         customer="Noor Foods",
#         total=4500,
#         status=OrderStatus.PENDING,
#     ),
#     "A102": Order(
#         id="A102",
#         customer="Bilal Traders",
#         total=12800,
#         status=OrderStatus.DELIVERED,
#     ),
#     "A103": Order(
#         id="A103",
#         customer="Karachi Crafts",
#         total=2300,
#         status=OrderStatus.PENDING,
#     ),
# }

# @app.patch("/orders/{order_id}")
# def update_order(order_id: str, updates: OrderUpdate) -> Order:
#     if order_id not in ORDERS:
#         raise HTTPException(
#             status_code=404,
#             detail=f"Order {order_id} not found",
#         )

#     update_data = updates.model_dump(exclude_unset=True)

#     # Reject an empty update
#     if not update_data:
#         raise HTTPException(
#             status_code=400,
#             detail="Empty update. Provide at least one field.",
#         )

#     existing_order = ORDERS[order_id]

#     updated_order = existing_order.model_copy(
#         update=update_data
#     )

#     ORDERS[order_id] = updated_order

#     return updated_order


# 3. Delete only pending orders. Noor Foods doesn't want delivered orders deleted, because they're needed for accounts. Change delete_order() so that deleting a delivered order returns a 409 Conflict with a message that explains why. Add a request for it in Bruno.


from enum import StrEnum

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Noor Foods Orders API")


class OrderStatus(StrEnum):
    PENDING = "pending"
    DELIVERED = "delivered"


# Data sent by the client when creating an order
class NewOrder(BaseModel):
    customer: str = Field(min_length=2, max_length=120)
    total: int = Field(gt=0)
    city: str | None = Field(default=None, max_length=50)


# Complete order stored and returned by the API
class Order(BaseModel):
    id: str
    customer: str
    total: int
    status: OrderStatus
    city: str | None = None


# Data sent by the client when updating an order
class OrderUpdate(BaseModel):
    total: int | None = Field(default=None, gt=0)


ORDERS = {
    "A101": Order(
        id="A101",
        customer="Noor Foods",
        total=4500,
        status=OrderStatus.PENDING,
    ),
    "A102": Order(
        id="A102",
        customer="Bilal Traders",
        total=12800,
        status=OrderStatus.DELIVERED,
    ),
    "A103": Order(
        id="A103",
        customer="Karachi Crafts",
        total=2300,
        status=OrderStatus.PENDING,
    ),
}


@app.delete("/orders/{order_id}", status_code=204)
def delete_order(order_id: str) -> None:
    if order_id not in ORDERS:
        raise HTTPException(
            status_code=404,
            detail=f"Order {order_id} not found",
        )

    order = ORDERS[order_id]

    if order.status == OrderStatus.DELIVERED:
        raise HTTPException(
            status_code=409,
            detail="Delivered orders cannot be deleted because they are required for accounting records.",
        )

    del ORDERS[order_id]


@app.get("/orders")
def list_orders(
    status: OrderStatus | None = None,
    limit: int = 10,
) -> list[Order]:
    orders = []

    for order in ORDERS.values():
        if status is None or order.status == status:
            orders.append(order)

    return orders[:limit]
