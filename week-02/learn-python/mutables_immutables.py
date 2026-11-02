# Exercise

# Practice: mutable and immutable objects

# Three problems, each harder than the last. Predict the output before you run each one, then check.

# 1. Predict the output. What does this print, and why?

# Copy
# city = " lahore "
# city.strip()
# tags = ["new"]
# tags.append("vip")
# print(f"[{city}]", tags)

# # 1. Immutable object: String
# city = " lahore "

# # strip() returns a new string, but doesn't modify the original
# city.strip()

# # 2. Mutable object: List
# tags = ["new"]

# # append() modifies the existing list
# tags.append("vip")

# # Print both values
# print(f"[{city}]", tags)



# 2. A safe discount. Write apply_discount(prices, rate) that returns a new list of discounted prices and leaves the original list unchanged. Test it with [1000, 2500, 400] and 0.1, then print both lists to prove the original didn't change.

# def apply_discount(prices, rate):
#     discounted_prices = []

#     for price in prices:
#         discounted_price = price - (price * rate)
#         discounted_prices.append(discounted_price)

#     return discounted_prices


# # Original prices
# prices = [1000, 2500, 400]

# # Apply 10% discount
# new_prices = apply_discount(prices, 0.1)

# # Print both lists
# print("Original prices:", prices)
# print("Discounted prices:", new_prices)



# 3. Fix the bug. This function is meant to start a fresh log for each order, but the logs keep growing. Explain why, then fix it:

# Copy
# def log_event(event, log=[]):
#     log.append(event)
#     return log


# print(log_event("order created"))
# print(log_event("payment received"))

# def log_event(event, log=None):
#     if log is None:
#         log = []

#     log.append(event)
#     return log


# print(log_event("order created"))
# print(log_event("payment received"))