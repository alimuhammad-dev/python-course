# import json

# orders = [
#     {"id": "A101", "total": 4500, "status": "delivered"},
#     {"id": "A102", "total": 12800, "status": "pending"},
#     {"id": "A103", "total": 2300, "status": "delivered"},
# ]

# with open("orders.json", "w") as file:
#     json.dump(orders, file, indent=2)

# with open("orders.json") as file:
#     loaded = json.load(file)

# print(len(loaded))              
# print(loaded[1]["status"])        




# Practice: reading and writing files

# Five problems, each harder than the last: 1 to 3 are core, 4 and 5 are stretch. After each one, open the file you created in your editor to check what's actually inside it.

# 1. A shopping list. Write four items to shopping.txt, one per line. Then read the file back and print each item numbered: 1. Rice, 2. Oil and so on.


# shopping_items = ["Rice", "Oil", "Sugar", "Milk"]

# # Write items to the file
# with open("shopping.txt", "w") as file:
#     for item in shopping_items:
#         file.write(item + "\n")

# # Read items from the file
# with open("shopping.txt", "r") as file:
#     content = file.readlines()

# # Print numbered items
# for index, item in enumerate(content, start=1):
#     print(f"{index}. {item.strip()}")



# 2. Append, don't erase. Write a function add_note(text) that adds one line to log.txt using append mode. Call it three times, then run your script a second time. How many lines does the file have now? Change the mode to "w" and run it twice more. What changed, and when would you want each behaviour?


# def add_note(text):
#     with open("log.txt", "a") as file:
#         file.write(text + "\n")


# add_note("Started Python learning")
# add_note("Practiced dictionaries")
# add_note("Learned file handling")



# 3. A week of sales. Create sales.txt in your editor with one number per line: 18500, 22300, 19800, 25400, 31200, 42800 and 38600. Read the file, convert each line to a number, and print the weekly total and daily average using your format_rupees() function (expected: Rs 198,600 and Rs 28,371). What error do you get if you forget to convert?

# def format_rupees(amount):
#     return f"Rs {amount:,.0f}"


# with open("sales.txt", "r") as file:
#     lines = file.readlines()

# sales = []

# for line in lines:
#     sales.append(int(line.strip()))

# weekly_total = sum(sales)
# daily_average = weekly_total / len(sales)

# print("Weekly total:", format_rupees(weekly_total))
# print("Daily average:", format_rupees(daily_average))



# 4. Comma-separated orders. Create orders.txt with these lines:

# Copy
# A101,Noor Foods,4500,delivered
# A102,Karachi Crafts,12800,pending
# A103,Noor Foods,2300,delivered
# A104,Bilal Traders,7600,delivered
# A105,Karachi Crafts,3900,cancelled
# Look up the string .split() method. Read the file and turn each line into a dictionary with the keys id, customer, total and status, with total as a number. Collect them in a list, then print 3 delivered orders, Rs 14,400. If your file ends with an empty line, what happens, and how can you skip it?

# orders = []

# with open("orders.txt", "r") as file:
#     for line in file:
#         if not line.strip():
#             continue

#         parts = line.strip().split(",")

#         order = {
#             "id": parts[0],
#             "customer": parts[1],
#             "total": int(parts[2]),
#             "status": parts[3]
#         }

#         orders.append(order)


# delivered_count = 0
# delivered_total = 0

# for order in orders:
#     if order["status"] == "delivered":
#         delivered_count += 1
#         delivered_total += order["total"]

# print(f"{delivered_count} delivered orders, Rs {delivered_total:,}")



# 5. Write a report. Using your list from problem 4, work out each customer's total, leaving out cancelled orders. Write the result to report.txt so the file contains exactly:

# Copy
# Order report
# Noor Foods: Rs 6,800
# Karachi Crafts: Rs 12,800
# Bilal Traders: Rs 7,600
# Total: Rs 27,200
# Add a sixth order to orders.txt and run your script again. The report should change with no other code changes.


# # Step 1: Read orders from the file
# orders = []

# with open("orders.txt", "r") as file:
#     for line in file:
#         if not line.strip():
#             continue

#         parts = line.strip().split(",")

#         order = {
#             "id": parts[0],
#             "customer": parts[1],
#             "total": int(parts[2]),
#             "status": parts[3]
#         }

#         orders.append(order)


# # Step 2: Calculate each customer's total
# customer_totals = {}

# for order in orders:
#     if order["status"] == "cancelled":
#         continue

#     customer = order["customer"]
#     total = order["total"]

#     if customer in customer_totals:
#         customer_totals[customer] += total
#     else:
#         customer_totals[customer] = total


# # Step 3: Calculate overall total
# grand_total = sum(customer_totals.values())


# # Step 4: Write the report
# with open("report.txt", "w") as file:
#     file.write("Order report\n")

#     for customer, total in customer_totals.items():
#         file.write(f"{customer}: Rs {total:,}\n")

#     file.write(f"Total: Rs {grand_total:,}\n")





# Exercise

# Practice: saving and loading data with JSON

# Five problems, each harder than the last: 1 to 3 are core, 4 and 5 are stretch.

# 1. Python to JSON. Create a dictionary for a product with the keys name, price, in_stock (a boolean) and discount (set to None). Print it with print(), then print json.dumps() of it, then json.dumps() with indent=2. Write a comment listing every difference you can see between the Python and the JSON.

# import json

# # Create a Python dictionary
# product = {
#     "name": "Laptop",
#     "price": 85000,
#     "in_stock": True,
#     "discount": None
# }

# # Print the Python dictionary
# print(product)

# # Convert Python dictionary into JSON string
# print(json.dumps(product))

# # Convert into formatted JSON with indentation
# print(json.dumps(product, indent=2))



# 2. JSON to Python. An API sends you this text:

# Copy
# text = '{"name": "Amna Raza", "plan": "pro", "active": true, "tags": ["vip", "lahore"]}'
# Turn it into a dictionary with json.loads(). Print the name, the number of tags and the type of active. Then try text["name"] before converting it. Why doesn't that work?

# import json

# text = '{"name": "Amna Raza", "plan": "pro", "active": true, "tags": ["vip", "lahore"]}'

# # Convert JSON string into Python dictionary
# data = json.loads(text)

# # Print the requested information
# print(data["name"])
# print(len(data["tags"]))
# print(type(data["active"]))



# 3. Save in one script, load in another. In save_orders.py, save the orders list from the demo to orders.json. Open the file in your editor and look at it. Then, in a separate file, load_orders.py, load it and print 3 orders, Rs 19,600 in total.

# import json

# # Create orders list
# orders = [
#     {
#         "id": "A101",
#         "customer": "Noor Foods",
#         "total": 4500,
#         "status": "delivered"
#     },
#     {
#         "id": "A102",
#         "customer": "Karachi Crafts",
#         "total": 12800,
#         "status": "pending"
#     },
#     {
#         "id": "A103",
#         "customer": "Noor Foods",
#         "total": 2300,
#         "status": "delivered"
#     }
# ]

# # Save orders to JSON file
# with open("orders.json", "w") as file:
#     json.dump(orders, file, indent=2)

# print("Orders saved successfully!")

# import json

# # Load orders from JSON file
# with open("orders.json", "r") as file:
#     orders = json.load(file)

# # Count orders
# order_count = len(orders)

# # Calculate total
# total = 0

# for order in orders:
#     total += order["total"]

# # Display result
# print(f"{order_count} orders, Rs {total:,} in total")



# 4. Keep stock between runs. Create stock.json containing {"pens": 120, "notebooks": 45, "staplers": 8}. Write a script that loads it, records a sale of 30 notebooks, adds "markers" with 60 in stock if they aren't already there, and saves it back. Run the script three times and open the file after each run. What happens to the notebook count, and what would happen if the count went below zero?

# {
#     "pens": 120,
#     "notebooks": 45,
#     "staplers": 8
# }

# import json

# # Step 1: Load existing stock
# with open("stock.json", "r") as file:
#     stock = json.load(file)

# # Step 2: Record a sale of 30 notebooks
# stock["notebooks"] -= 30

# # Step 3: Add markers if they don't already exist
# if "markers" not in stock:
#     stock["markers"] = 60

# # Step 4: Save updated stock
# with open("stock.json", "w") as file:
#     json.dump(stock, file, indent=2)

# print("Stock updated successfully!")
# print(stock)



# 5. An API-shaped response. Save this as response.json. It's the shape of data you'll get from real APIs in week 3:

# Copy
# {
#   "status": "ok",
#   "data": {
#     "customer": {"name": "Noor Foods", "city": "Karachi"},
#     "orders": [
#       {"id": "A101", "total": 4500, "items": ["rice", "oil"]},
#       {"id": "A103", "total": 2300, "items": ["sugar"]},
#       {"id": "A106", "total": 6100, "items": ["flour", "tea", "rice"]}
#     ]
#   }
# }
# Load it and print Noor Foods (Karachi): 3 orders, 6 items, Rs 12,900, working out every value in code. Then save a new file, summary.json, with the keys customer, order_count, item_count and total, and check it in your editor.

# import json
# import os

# # Step 1: Get the folder where this Python script is located
# folder = os.path.dirname(os.path.abspath(__file__))

# # Step 2: Load response.json
# file_path = os.path.join(folder, "response.json")

# with open(file_path, "r") as file:
#     response = json.load(file)


# # Step 3: Extract customer information
# customer = response["data"]["customer"]

# customer_name = customer["name"]
# customer_city = customer["city"]


# # Step 4: Extract orders
# orders = response["data"]["orders"]

# order_count = len(orders)


# # Step 5: Calculate total items and order value
# item_count = 0
# total = 0

# for order in orders:
#     item_count += len(order["items"])
#     total += order["total"]


# # Step 6: Print the result
# print(
#     f"{customer_name} ({customer_city}): "
#     f"{order_count} orders, "
#     f"{item_count} items, "
#     f"Rs {total:,}"
# )


# # Step 7: Create summary dictionary
# summary = {
#     "customer": customer_name,
#     "order_count": order_count,
#     "item_count": item_count,
#     "total": total
# }


# # Step 8: Save summary.json in the same folder
# summary_path = os.path.join(folder, "summary.json")

# with open(summary_path, "w") as file:
#     json.dump(summary, file, indent=2)

# print("Summary saved successfully!")