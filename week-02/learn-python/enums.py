# Exercise

# Practice: enums and the standard library

# Three problems, each harder than the last. Work in a new file in your learn-python project and run it with uv run.

# 1. Today's date. Import date from datetime and print Report for 2026-11-02, using today's date. Then rewrite your import as import datetime and change the rest of your code to match.

# from datetime import date

# today = date.today()
# print(f"Report for {today}")


# 2. Payment methods. Create a StrEnum called PaymentMethod with the options CASH, CARD and BANK_TRANSFER, using auto(). Loop over it and print each option. Then print whether PaymentMethod.CARD == "card".

# from enum import StrEnum, auto

# class PaymentMethod(StrEnum):
#     CASH = auto()
#     CARD = auto()
#     BANK_TRANSFER = auto()

# for method in PaymentMethod:
#     print(method)

# print(PaymentMethod.CARD == "card")


# 3. Checking orders. Using the TaskStatus idea, create an OrderStatus enum with PENDING, DELIVERED and CANCELLED. Loop over the statuses below, as they might arrive from a file. Turn each into an OrderStatus, print the valid ones, and for the invalid ones print Skipping 'lost': not a valid status:

# statuses = ["pending", "delivered", "lost", "Cancelled", "cancelled"]
# Why is "Cancelled" rejected? How could you clean it first so it's accepted?

# from enum import StrEnum, auto


# class OrderStatus(StrEnum):
#     PENDING = auto()
#     DELIVERED = auto()
#     CANCELLED = auto()


# statuses = ["pending", "delivered", "lost", "Cancelled", "cancelled"]

# for status in statuses:
#     try:
#         order_status = OrderStatus(status.lower())
#         print(order_status)

#     except ValueError:
#         print(f"Skipping '{status}': not a valid status")
