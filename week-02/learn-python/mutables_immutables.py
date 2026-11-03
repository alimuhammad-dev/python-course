# In a shallow copy:
# 1. If you change the outer object, the original remains unchanged.
# 2. If you change a nested object, the original changes too.
# 3. If you change both, the original's outer values remain unchanged, but its nested values change.


# For deep copy, both the outer object and nested objects are independent.

# That means:
# 1. Change the outer object → original remains unchanged.
# 2. Change the nested object → original remains unchanged.
# 3. Change both → original remains completely unchanged.


# Exercise

# Practice: strings can't change

# 1. Predict the output. What does this print? Predict it first, then fix the code so it prints ORD0042:

# code = "ord-0042"

# code = code.upper()
# code = code.replace("-", "")

# print(code)


# 2. Cleaning names. Loop over [" amna ", "BILAL", " zara khan"] and build a new list of cleaned names using .strip() and .title(). Print it (expected: ['Amna', 'Bilal', 'Zara Khan']). Why do you need a new list instead of changing each string where it is?

# names = [" amna ", "BILAL", " zara khan"]

# cleaned_names = []

# for name in names:
#     cleaned_name = name.strip().title()
#     cleaned_names.append(cleaned_name)

# print(cleaned_names)


# 3. Fixing a code. A product code was typed with a letter O instead of a zero: sku = "PEN-O42". Try sku[4] = "0" and read the error. Then fix it a different way, so print(sku) shows PEN-042.

# sku = "PEN-O42"
# sku = sku.replace("O", "0")
# print(sku)


# Exercise

# Practice: lists can change

# 1. Editing a cart. Start with cart = ["rice", "oil"]. Add "sugar" to the end, replace "oil" with "ghee" using its position, then look up the .remove() method and remove "rice". Print the cart (expected: ['ghee', 'sugar']).

# cart = ["rice", "oil"]

# # Add sugar to the end
# cart.append("sugar")

# # Replace oil with ghee using its position
# cart[1] = "ghee"

# # Remove rice from the list
# cart.remove("rice")

# print(cart)


# 2. Dictionaries change too. Start with stock = {"pens": 120, "notebooks": 45}. Record a sale of 20 pens, add "markers" with 60 in stock, then look up the del keyword and remove "notebooks". Print the dictionary (expected: {'pens': 100, 'markers': 60}).

# stock = {"pens": 120, "notebooks": 45}

# # Record a sale of 20 pens
# stock["pens"] = stock["pens"] - 20

# # Add markers to the dictionary
# stock["markers"] = 60

# # Remove notebooks
# del stock["notebooks"]

# print(stock)


# 3. A price rise that doesn't work. This loop is meant to raise every price by 10%, but the list doesn't change. Run it and explain why:

# Copy
# prices = [850, 1200, 400]
# for price in prices:
#     price = price * 1.1
# print(prices)
# Look up range() and len() together, then rewrite the loop so it changes each item in the list by its position. Use round() so it prints [935, 1320, 440].

# prices = [850, 1200, 400]

# for i in range(len(prices)):
#     prices[i] = round(prices[i] * 1.1)

# print(prices)


# Exercise

# Practice: watching identity with id()

# 1. Predict the result. Predict whether each print shows True or False, then run it:

# Copy
# status = "pending"
# before = id(status)
# status = status.upper()
# print(id(status) == before)

# order = {"status": "pending"}
# before = id(order)
# order["status"] = "delivered"
# print(id(order) == before)

# First example: String (Immutable)
# status = "pending"before = id(status)status = status.upper()


# - id(status) records the identity of the original string.
# - .upper() creates a new string "PENDING".
# - status now refers to the new string.
# - Its identity is different.
# Therefore: False.

# Second example: Dictionary (Mutable)
# order = {"status": "pending"}before = id(order)order["status"] = "delivered"


# - id(order) records the dictionary's identity.
# - We update its existing value.
# - We modify the same dictionary rather than creating a new one.
# - Its identity remains unchanged.
# Therefore: True.


# 2. Same list or a copy? Run this and explain each result:

# Copy
# a = [4500, 12800]
# b = a
# c = a.copy()
# print(id(a) == id(b), id(a) == id(c))
# Then look up Python's is operator and rewrite the last line to use it instead of comparing id() values.

# b = a — Same list

# Both a and b refer to the same list in memory.
# b = a

# Therefore, id(a) == id(b) returns True.

# c = a.copy() — New list

# .copy() creates a separate list with the same elements.
# c = a.copy()

# Therefore, id(a) == id(c) returns False.
# 3. Rewrite using is
# Instead of comparing IDs, Python provides the is operator.
# a = [4500, 12800]b = ac = a.copy()print(a is b, a is c)

# Output:
# True False

# 4. Understanding is vs ==
# Operator	What it checks
# is	Are they the same object?
# ==	Do they have the same values?

# Try this:
# print(a == c)  # Trueprint(a is c)  # False

# Why?

# Both lists contain [4500, 12800], so their values are equal. But they are two separate objects.

# Remember:
# - b = a → Same object.
# - c = a.copy() → Different object.
# - is → Identity comparison.
# - == → Value comparison.


# 3. Two ways to sort. Look up the list .sort() method and the built-in sorted() function. Start with prices = [1200, 400, 850], save its id(), and sort it with prices.sort(). Is it still the same list? Now try prices = sorted(prices, reverse=True). Is it still the same list? Which one changes the list, and which one creates a new one?

# - .sort() changes the original list.
# - It sorts the items in ascending order.
# - The list's identity stays the same.
# 2. Using sorted()
# prices = [1200, 400, 850]before = id(prices)prices = sorted(prices, reverse=True)print(prices)print(id(prices) == before)

# Output:
# [1200, 850, 400]
# False

# Why?
# - sorted() creates a new sorted list.
# - reverse=True sorts in descending order.
# - Assigning the result back to prices makes it refer to the new list.
# - The identity changes.
# 3. Comparison
# Feature	.sort()	sorted()
# Changes original list?	Yes	No
# Creates a new list?	No	Yes
# Returns	None	New sorted list
# Supports descending order?	Yes	Yes

# 4. Remember
# prices.sort()

# Modifies the existing list.
# prices = sorted(prices)

# Creates a new list and assigns it to prices.

# Mentor tip: Use .sort() when you want to modify the original list. Use sorted() when you want to preserve the original list.


# Exercise

# Practice: functions can change your data

# 1. Predict the output. What does this print?

# Copy
# def close_order(order):
#     order["status"] = "closed"


# order = {"id": "A101", "status": "pending"}
# close_order(order)
# print(order["status"])
# Now write closed_copy(order), which returns a closed copy of the order and leaves the original as pending. Print both to check.

# 2. Replacing isn't changing. Predict what both print calls show, then run it:

# Copy
# def rename(customer):
#     customer = "Bilal Traders"


# def empty_cart(cart):
#     cart = []


# name = "Noor Foods"
# rename(name)
# print(name)

# cart = ["rice", "oil"]
# empty_cart(cart)
# print(cart)
# The cart is a list, so why didn't empty_cart() empty it? What's the difference between cart = [] and cart.append(...) inside a function?

# 3. Change or return. Write two functions and test both on the same starting cart:

# add_item(cart, item) adds the item to the cart itself and returns nothing.
# with_item(cart, item) returns a new cart with the item added and leaves the original unchanged.
# Print the cart after each call to prove which one changed it. Write a comment explaining how each function's name tells the caller what to expect.

# Here are the three complete exercises, ready to copy and run.
# 1. An order line
# line = ("Rice", 2, 1450)# Print order details using indexesprint(f"{line[1]} x {line[0]} = Rs {line[1] * line[2]:,}")# Try changing quantity (this will produce an error)# line[1] = 3# Create a new tuple with updated quantitynew_line = (line[0], 3, line[2])print("Updated order:", new_line)


# Output:
# 2 x Rice = Rs 2,900
# Updated order: ('Rice', 3, 1450)


# 2. Tuple unpacking
# lines = [    ("Rice", 2, 1450),    ("Oil", 1, 2100),    ("Sugar", 3, 160)]total = 0for line in lines:    item, quantity, price = line    order_total = quantity * price    total = total + order_totalprint("Order total:", total)


# Output:
# Order total: 5480


# 3. List or tuple?
# # List: Shopping cart items can be added or removed.cart = ["Rice", "Oil"]# Tuple: A date is a fixed group of values.date = (2026, 11, 3)# List: New orders can arrive throughout the day.orders = ["Order 1", "Order 2"]# Tuple: Warehouse coordinates represent a fixed pair.warehouse_location = (33.6844, 73.0479)print("Cart:", cart)print("Date:", date)print("Orders:", orders)print("Warehouse location:", warehouse_location)


# Remember:
# - Lists use [] and are mutable.
# - Tuples use () and are immutable.
# - Tuple unpacking lets you assign values to multiple variables in one statement.


# Exercise

# Practice: tuples

# 1. An order line. Store one order line as a tuple: line = ("Rice", 2, 1450), meaning the item, the quantity and the unit price. Using indexes, print 2 x Rice = Rs 2,900. Then try to change the quantity to 3 and read the error. Create a new tuple with the new quantity instead.

# 2. Unpacking. Look up tuple unpacking, for example item, quantity, price = line. Then loop over this list of order lines, unpack each one, and print the order total (expected: 5480):

# Copy
# lines = [("Rice", 2, 1450), ("Oil", 1, 2100), ("Sugar", 3, 160)]
# 3. List or tuple? For each of these, decide whether you'd use a list or a tuple, and write a one-line comment explaining why:

# the items in a customer's shopping cart
# a date stored as year, month and day
# the orders that arrive during a day
# the latitude and longitude of a warehouse


# Here are the three complete Python programs, with comments and expected outputs.
# 1. An order line — Tuples
# line = ("Rice", 2, 1450)# Print using indexesprint(f"{line[1]} x {line[0]} = Rs {line[1] * line[2]:,}")# Try changing quantity (uncomment to see the error)# line[1] = 3# Create a new tuple with quantity 3new_line = (line[0], 3, line[2])print("Updated order:", new_line)


# Output:
# 2 x Rice = Rs 2,900
# Updated order: ('Rice', 3, 1450)


# The error is TypeError because tuples are immutable. You cannot change their elements directly.
# 2. Unpacking — Calculate order total
# lines = [    ("Rice", 2, 1450),    ("Oil", 1, 2100),    ("Sugar", 3, 160)]total = 0for line in lines:    item, quantity, price = line    order_total = quantity * price    total += order_totalprint("Order total:", total)


# Output:
# Order total: 5480


# How unpacking works:
# item, quantity, price = line


# Python automatically assigns each tuple value to its corresponding variable.

# For example:
# ("Rice", 2, 1450)


# Becomes:
# item = "Rice"quantity = 2price = 1450


# 3. List or tuple?
# # List: Shopping cart items can be added or removed.cart = ["Rice", "Oil"]# Tuple: Date represents a fixed group of values.date = (2026, 11, 3)# List: New orders can arrive throughout the day.orders = ["Order 1", "Order 2"]# Tuple: Warehouse coordinates represent a fixed pair.warehouse_location = (33.6844, 73.0479)print(cart)print(date)print(orders)print(warehouse_location)


# Output:
# ['Rice', 'Oil']
# (2026, 11, 3)
# ['Order 1', 'Order 2']
# (33.6844, 73.0479)


# Quick revision
# Concept	Meaning
# List []	Mutable — can be changed
# Tuple ()	Immutable — cannot be changed
# Indexing	Access values using positions
# Unpacking	Assign tuple values to variables
# .copy()	Creates a shallow copy of a list or dictionary

# Remember: Use lists for collections that change and tuples for fixed groups of related values.


# Exercise

# Practice: functions can change your data

# 1. Predict the output. What does this print?

# Copy
# def close_order(order):
#     order["status"] = "closed"


# order = {"id": "A101", "status": "pending"}
# close_order(order)
# print(order["status"])
# Now write closed_copy(order), which returns a closed copy of the order and leaves the original as pending. Print both to check.

# 2. Replacing isn't changing. Predict what both print calls show, then run it:

# Copy
# def rename(customer):
#     customer = "Bilal Traders"


# def empty_cart(cart):
#     cart = []


# name = "Noor Foods"
# rename(name)
# print(name)

# cart = ["rice", "oil"]
# empty_cart(cart)
# print(cart)
# The cart is a list, so why didn't empty_cart() empty it? What's the difference between cart = [] and cart.append(...) inside a function?

# 3. Change or return. Write two functions and test both on the same starting cart:

# add_item(cart, item) adds the item to the cart itself and returns nothing.
# with_item(cart, item) returns a new cart with the item added and leaves the original unchanged.
# Print the cart after each call to prove which one changed it. Write a comment explaining how each function's name tells the caller what to expect.


# # 1. Change the original dictionary
# def close_order(order):
#     order["status"] = "closed"


# # Return a closed copy without changing the original
# def closed_copy(order):
#     new_order = order.copy()
#     new_order["status"] = "closed"
#     return new_order


# order = {"id": "A101", "status": "pending"}

# close_order(order)
# print(order)


# order = {"id": "A101", "status": "pending"}

# new_order = closed_copy(order)
# print("Original:", order)
# print("Copy:", new_order)


# # 2. Replacing isn't changing
# def rename(customer):
#     customer = "Bilal Traders"


# def empty_cart(cart):
#     cart = []


# name = "Noor Foods"
# rename(name)
# print(name)

# cart = ["rice", "oil"]
# empty_cart(cart)
# print(cart)


# # 3. Change or return
# def add_item(cart, item):
#     cart.append(item)


# def with_item(cart, item):
#     new_cart = cart.copy()
#     new_cart.append(item)
#     return new_cart


# cart = ["rice", "oil"]

# add_item(cart, "sugar")
# print("After add_item:", cart)

# new_cart = with_item(cart, "milk")
# print("Original cart:", cart)
# print("New cart:", new_cart)


# Exercise

# Practice: copies of nested data

# 1. Predict the output. What do both print calls show? Predict first, then run it:

# prices = [850, 1200]
# prices_copy = prices.copy()
# prices_copy.append(400)
# print(prices)

# price_lists = [[850, 1200], [400]]
# lists_copy = price_lists.copy()
# lists_copy[0].append(3100)
# print(price_lists)
# Both use .copy(). Why did the first original stay the same while the second changed?


# 2. A test run. You want to try out a status change without touching the real orders. Predict what this prints, then run it:

# import copy

# orders = [
#     {"id": "A101", "status": "pending"},
#     {"id": "A102", "status": "pending"},
# ]

# test_orders = copy.deepcopy(orders)
# for order in test_orders:
#     order["status"] = "delivered"

# print(orders)
# print(test_orders)


# Which object did .copy() create, and which objects are still shared? Fix it so orders stays pending while test_orders becomes delivered.


# 3. Settings for each customer. Every customer starts from the same default settings:

# defaults = {"currency": "PKR", "tags": ["standard"]}
# Write settings_for(defaults, tag), which returns a separate copy of the settings with tag added to its tags list. Call it once with "wholesale" and once with "vip", then print both results and defaults. Expected output:

# {'currency': 'PKR', 'tags': ['standard', 'wholesale']}
# {'currency': 'PKR', 'tags': ['standard', 'vip']}
# {'currency': 'PKR', 'tags': ['standard']}
# Now swap deepcopy() for .copy() in your function and run it again. Explain what changes.

# # 1. deep copy
# import copy

# defaults = {"currency": "PKR", "tags": ["standard"]}


# def settings_for(defaults, tag):
#     new_settings = copy.deepcopy(defaults)
#     new_settings["tags"].append(tag)
#     return new_settings


# wholesale_settings = settings_for(defaults, "wholesale")
# vip_settings = settings_for(defaults, "vip")

# print(wholesale_settings)
# print(vip_settings)
# print(defaults)


# # 1. deep copy
# import copy

# defaults = {"currency": "PKR", "tags": ["standard"]}


# def settings_for(defaults, tag):
#     new_settings = defaults.copy()
#     new_settings["tags"].append(tag)
#     return new_settings


# wholesale_settings = settings_for(defaults, "wholesale")
# vip_settings = settings_for(defaults, "vip")

# print(wholesale_settings)
# print(vip_settings)
# print(defaults)


# Exercise

# Practice: the default value trap

# 1. Predict the output. What do the three print calls show? Predict first, then run it:

# def add_tag(tag, tags=[]):
#     tags.append(tag)
#     return tags


# first = add_tag("new")
# second = add_tag("vip")
# print(first)
# print(second)
# print(first is second)
# first was created before "vip" was added, so why does it contain "vip"?

# def add_tag(tag, tags=None):
#     if tags is None:
#         tags = []

#     tags.append(tag)
#     return tags


# first = add_tag("new")
# second = add_tag("vip")

# print(first)
# print(second)
# print(first is second)


# 2. Counting items. This function is meant to start a new count on each call unless you pass in your own dictionary. Run it and explain the output:

# def count_item(item, counts={}):
#     if item not in counts:
#         counts[item] = 0
#     counts[item] += 1
#     return counts


# print(count_item("rice"))
# print(count_item("oil"))
# Fix it so it prints {'rice': 1} and then {'oil': 1}. Then check that passing your own dictionary still works: calling count_item("rice", shop) twice with shop = {} should leave shop as {'rice': 2}.

# def count_item(item, counts=None):
#     if counts is None:
#         counts = {}

#     if item not in counts:
#         counts[item] = 0

#     counts[item] += 1

#     return counts


# print(count_item("rice"))
# print(count_item("oil"))


# 3. A fix that isn't quite right. Someone fixed the trap by writing if not cart instead of if cart is None. Predict what this prints, then run it:

# def add_item(item, cart=None):
#     if not cart:
#         cart = []
#     cart.append(item)
#     return cart


# my_cart = []
# add_item("rice", my_cart)
# print(my_cart)
# Look up what not does with an empty list. Why did rice never reach my_cart? Fix the function, and explain why is None is the right check here.

# def add_item(item, cart=None):
#     if cart is None:
#         cart = []

#     cart.append(item)
#     return cart


# my_cart = []
# add_item("rice", my_cart)

# print(my_cart)


# Exercise

# Practice: dictionary keys

# 1. Which keys work? Predict which of these lines fail, then run them. An error stops the script, so comment out each failing line to reach the next one:

# a = {"A101": "pending"}
# b = {42: "pending"}
# c = {(24.86, 67.01): "Karachi warehouse"}
# d = {["rice", "oil"]: 2}  A list is mutable, so it cannot be used as a dictionary key.
# e = {{"id": "A101"}: "pending"}

# What do the keys that work have in common?
# They are all hashable.
# Python uses a hash value to find and retrieve dictionary keys efficiently.


# 2. Looking up prices. Prices are stored by product and size, but the order arrives from JSON, which has no tuples, so each item is a list:

# prices = {("Rice", "5kg"): 1450, ("Rice", "10kg"): 2800, ("Oil", "1L"): 650}
# items = [["Rice", "10kg"], ["Oil", "1L"], ["Rice", "5kg"]]
# Loop over items and try prices[item]. Read the error. Then look up the built-in tuple() function, use it to convert each item, and print the order total (expected: 4900).

# prices = {
#     ("Rice", "5kg"): 1450,
#     ("Rice", "10kg"): 2800,
#     ("Oil", "1L"): 650
# }

# items = [
#     ["Rice", "10kg"],
#     ["Oil", "1L"],
#     ["Rice", "5kg"]
# ]

# total = 0

# for item in items:
#     key = tuple(item)
#     price = prices[key]
#     total += price

# print("Order total:", total)


# 3. A tuple that can change. Predict what this prints and where it fails, then run it:

# branch = ("Karachi", ["Clifton", "Saddar"])
# branch[1].append("DHA")
# print(branch)

# stock = {branch: 12}
# Tuples can't change, so how did "DHA" get in? Why does Python refuse this tuple as a key when it accepted ("Karachi", "Clifton") in the example? Fix it so branch can be used as a key.

# branch = ("Karachi", ("Clifton", "Saddar", "DHA"))

# stock = {branch: 12}

# print(stock)


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





# 3. Stock by branch (examples 4 and 9). A shop keeps its stock in a dictionary with a (city, area) tuple as each key:

# stock = {
#     ("Karachi", "Clifton"): 12,
#     ("Karachi", "Saddar"): 30,
#     ("Lahore", "Gulberg"): 18,
# }
# Add a new branch, ("Lahore", "DHA"), with 25 in stock. Then loop over stock.items() and add up the stock for every Karachi branch (expected: 42). Use key[0] to get the city from each tuple. Finally, try to change the city inside one of the keys. What error do you get, and why does Python stop you?


# stock = {
#     ("Karachi", "Clifton"): 12,
#     ("Karachi", "Saddar"): 30,
#     ("Lahore", "Gulberg"): 18,
# }

# # 1. Add a new branch
# stock[("Lahore", "DHA")] = 25

# # 2. Calculate total stock for Karachi branches
# total = 0

# for key, quantity in stock.items():
#     if key[0] == "Karachi":
#         total += quantity

# print("Total Karachi stock:", total)

# # 3. Try to change the city inside a tuple key
# key = ("Karachi", "Clifton")
# key[0] = "Lahore"  # Raises TypeError because tuples are immutable




# 4. One template, two orders (example 5). What does this print? Predict it first:

# Copy
# template = {"status": "pending", "total": 0}

# order_a = template
# order_a["total"] = 4500

# order_b = template
# order_b["total"] = 12800

# print(order_a["total"], order_b["total"], template["total"])
# Fix it so it prints 4500 12800 0, changing only the two lines that create the orders.


# template = {"status": "pending", "total": 0}

# order_a = template.copy()
# order_a["total"] = 4500

# order_b = template.copy()
# order_b["total"] = 12800

# print(order_a["total"], order_b["total"], template["total"])




# 5. A safe discount (example 6). Write apply_discount(prices, rate) that returns a new list of discounted prices and leaves the original list unchanged. Test it with [1000, 2500, 400] and 0.1, then print both lists to prove the original didn't change.

# def apply_discount(prices, rate):
#     discounted_prices = []

#     for price in prices:
#         discounted_price = price - (price * rate)
#         discounted_prices.append(discounted_price)

#     return discounted_prices


# # Test the function
# prices = [1000, 2500, 400]

# discounted = apply_discount(prices, 0.1)

# # Print both lists
# print("Original prices:", prices)
# print("Discounted prices:", discounted)




# 6. A branch copy (example 7). Noor Foods is opening a Lahore branch, and you want to start its record as a copy of the main one:

# Copy
# customer = {
#     "name": "Noor Foods",
#     "address": {"city": "Karachi", "area": "Clifton"},
#     "tags": ["wholesale"],
# }

# branch = customer.copy()
# branch["name"] = "Noor Foods Lahore"
# branch["address"]["city"] = "Lahore"
# branch["tags"].append("new")
# print(customer)
# Predict which of the three changes also show up in customer, then run it. Fix it with deepcopy() so customer stays exactly as it started, and explain why changing name was safe even with .copy(). 


# import copy

# customer = {
#     "name": "Noor Foods",
#     "address": {"city": "Karachi", "area": "Clifton"},
#     "tags": ["wholesale"],
# }

# branch = copy.deepcopy(customer)

# branch["name"] = "Noor Foods Lahore"
# branch["address"]["city"] = "Lahore"
# branch["tags"].append("new")

# print("Customer:", customer)
# print("Branch:", branch)



# 7. Fix the bug (example 8). This function is meant to start a fresh log for each order, but the logs keep growing. Explain why, then fix it:

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