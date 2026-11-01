import json

EXPENSES_FILE = "week-01/expenses.json"
APPROVAL_LIMIT = 25000
SUMMARY_FILE = "week-01/summary.json"


# Function 1: Load expenses from JSON file
def load_expenses(path):
    try:
        with open(path, "r") as file:
            expenses = json.load(file)

        if not isinstance(expenses, list):
            raise ValueError("Expected a JSON list of expenses")

        return expenses

    except FileNotFoundError:
        print(f"Could not read {path}: file not found")
        return None

    except json.JSONDecodeError:
        print(f"Could not read {path}: invalid JSON")
        return None

    except ValueError as error:
        print(f"Could not read {path}: {error}")
        return None


# Function 2: Format amounts in rupees
def format_rupees(amount):
    return f"Rs {amount:,}"


# Function 3: Calculate totals for each category
def category_totals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    return totals


# Function 4: Find the largest expense
def largest_expense(expenses):
    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


# Function 5: Find expenses requiring approval
def approval_expenses(expenses, limit):
    approvals = []

    for expense in expenses:
        if expense["amount"] > limit:
            approvals.append(expense)

    return approvals


# Function 6: Calculate the overall total
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# Function 7: Save summary to JSON
def save_summary(path, expenses, total, categories):
    summary = {
        "expense_count": len(expenses),
        "total": total,
        "by_category": categories
    }

    with open(path, "w") as file:
        json.dump(summary, file, indent=2)


# Main program
def main():

    # Load expenses
    expenses = load_expenses(EXPENSES_FILE)

    # Stop if loading fails
    if expenses is None:
        return

    # Handle an empty expense list
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    # Calculate values
    total = calculate_total(expenses)
    categories = category_totals(expenses)
    largest = largest_expense(expenses)
    approvals = approval_expenses(expenses, APPROVAL_LIMIT)

    # Print report
    print("Cafe expense report")
    print(f"Expenses recorded: {len(expenses)}")
    print(f"Total spent: {format_rupees(total)}")

    print("\nBy category:")

    for category, amount in categories.items():
        print(f"  {category:<10} {format_rupees(amount):>12}")

    print(
        f"\nLargest expense: {largest['item']} "
        f"({format_rupees(largest['amount'])})"
    )

    print(
        f"\nNeeds approval (over {format_rupees(APPROVAL_LIMIT)}): "
        f"{len(approvals)}"
    )

    for expense in approvals:
        print(
            f"  - {expense['item']}: "
            f"{format_rupees(expense['amount'])}"
        )

    # Save summary
    try:
        save_summary(SUMMARY_FILE, expenses, total, categories)
        print("\nSummary saved successfully!")

    except OSError as error:
        print(f"Could not save {SUMMARY_FILE}: {error}")


# Run the program
if __name__ == "__main__":
    main()