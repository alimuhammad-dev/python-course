# def apply_discount(total, rate):
#     discount = total * rate
#     return total - discount

# print(apply_discount(12800, 0.1))   # 11520.0 
# print(apply_discount(4500, 0.2))    # 3600.0




# Exercise

# Practice: writing your own functions

# Five problems, each harder than the last: 1 to 3 are core, 4 and 5 are stretch. Call every function at least twice with different arguments, and check the results.

# 1. Formatting rupees. Write a function format_rupees(amount) that returns text such as Rs 12,800. Test it with 12800, 999 and 1250000. Then use it to print Noor Foods owes Rs 11,520.

# def format_rupees(amount):
#     return amount
# print(format_rupees(12800))
# print(format_rupees(999))
# print(format_rupees(1250000))

# def format_rupees(amount):
#     data = f"Noor food owes {amount}"
#     return data
# print(format_rupees(11520))



# 2. Return or print? Write add_tax(subtotal, rate=0.18). The rate=0.18 part is a default value: it's used when you don't pass a rate. Check that add_tax(7200) returns 8496.0 and add_tax(7200, 0.05) returns 7560.0. Now write a second version that uses print() instead of return, store its result in a variable and print the variable. What do you get, and why?

# def add_tax(subtotal, rate=0.18):
#     tax = subtotal * rate
#     total = subtotal + tax
#     return total

# print(add_tax(7200))
# print(add_tax(7200, 0.05))



# 3. Shipping as a function. Write shipping_charge(weight_kg, city) that returns the charge as a number: Rs 200 for Karachi, Lahore and Islamabad, Rs 350 for every other city, and double that when the weight is over 5 kg. Clean the city inside the function, so " karachi " counts as Karachi. Call it for at least four combinations, including exactly 5 kg, and print each result with your format_rupees() function, for example Shipping to Karachi: Rs 200. If you solved Demo 4, problem 4, add its free-shipping rule as a third parameter, order_total.

# def format_rupees(amount):
#     return f"{amount:,}"

# def shipping_charge(weight_kg, city):
#     city = city.strip().title()

#     if city in ["Karachi", "Lahore", "Islamabad"]:
#         charge = 200
#     else:
#         charge = 350

#     if weight_kg > 5:
#         charge *= 2

#     return charge

# charge = shipping_charge(5, " karachi ")
# print(f"Shipping to Karachi: Rs {format_rupees(charge)}")



# 4. Totals by status. Write total_by_status(orders, status) that takes a list of order dictionaries and a status, and returns the sum of the totals with that status. Using the orders list from Demo 5, check that "delivered" gives 6800, "pending" gives 12800 and "cancelled" gives 0.

# orders = [
#     {"id": "A101", "status": "delivered", "total": 4500},
#     {"id": "A102", "status": "pending", "total": 12800},
#     {"id": "A103", "status": "delivered", "total": 2300},
# ]
# def total_by_status(orders, status):
#     total = 0

#     for order in orders:
#         if order["status"] == status:
#             total += order["total"]

#     return total

# print(total_by_status(orders, "delivered"))
# print(total_by_status(orders, "pending"))
# print(total_by_status(orders, "cancelled"))



# 5. Refactor the reorder report. Take your reorder report from Demo 5, problem 5, and split it into three small functions:

# needs_reorder(product) returns True or False
# reorder_quantity(product) returns how many to order
# reorder_cost(product) returns the cost of that order, using reorder_quantity()
# Rewrite the loop so it uses these functions, and check you still get the same lines and the same total (Rs 8,920). Write a comment explaining one way the new version is easier to read, test or change than the old one.
    

# inventory = [
#     {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
#     {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
#     {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
#     {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
#     {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
# ]


# # Checks whether a product needs reordering
# def needs_reorder(product):
#     return product["stock"] < product["reorder_level"]


# # Calculates the quantity required to reach twice the reorder level
# def reorder_quantity(product):
#     target_stock = product["reorder_level"] * 2
#     return target_stock - product["stock"]


# # Calculates the total cost of the required quantity
# def reorder_cost(product):
#     quantity = reorder_quantity(product)
#     return quantity * product["unit_cost"]


# # Generate the reorder report
# total_cost = 0
# items_to_reorder = 0

# for product in inventory:
#     if needs_reorder(product):
#         quantity = reorder_quantity(product)
#         cost = reorder_cost(product)

#         print(f"Reorder {quantity} x {product['name']} (Rs {cost:,})")

#         total_cost += cost
#         items_to_reorder += 1

# if items_to_reorder == 0:
#     print("All stock OK")
# else:
#     print(f"Total cost: Rs {total_cost:,}")


