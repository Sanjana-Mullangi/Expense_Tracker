import matplotlib.pyplot as plt
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
expenses = []

# ---------------- Utility Functions ----------------
def load_expenses():
    """Load expenses from CSV file."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Date"])
        return []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header
        return [(float(amount), category, date) for amount, category, date in reader]

def save_expense(amount, category, date):
    """Save a single expense to CSV file."""
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date])

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ---------------- Expense Functions ----------------
def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    category = input("Enter category: ").strip().title()
    date = datetime.now().strftime("%Y-%m-%d")

    expenses.append((amount, category, date))
    save_expense(amount, category, date)
    print("✅ Expense added!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nExpenses:")
    for amt, cat, dt in expenses:
        print(f"Amount: {amt:.2f} | Category: {cat} | Date: {dt}")

def show_total():
    total = sum(e[0] for e in expenses)
    print("\n💰 Total Expense:", total)

def show_category_bar():
    category_totals = {}
    for amt, cat, dt in expenses:
        category_totals[cat] = category_totals.get(cat, 0) + amt

    if not category_totals:
        print("No expenses to show.")
        return

    print("\nCategory-wise Totals:")
    for cat, amt in category_totals.items():
        print(f"{cat}: {amt:.2f}")

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    plt.bar(labels, values, color=plt.cm.Paired(range(len(values))))
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Total Expense", fontsize=12)
    plt.title("Category-wise Expenses", fontsize=14, fontweight='bold')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()

def show_monthly_summary():
    monthly_totals = {}
    for amt, cat, dt in expenses:
        month = dt[:7]  # YYYY-MM
        monthly_totals[month] = monthly_totals.get(month, 0) + amt

    if not monthly_totals:
        print("No expenses to show.")
        return

    print("\nMonthly Totals:")
    for month, amt in sorted(monthly_totals.items()):
        print(f"{month}: {amt:.2f}")

    months = list(sorted(monthly_totals.keys()))
    values = [monthly_totals[m] for m in months]

    plt.bar(months, values, color='skyblue')
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Total Expense", fontsize=12)
    plt.title("Monthly Expense Summary", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ---------------- Main Program ----------------
expenses = load_expenses()

while True:
    clear_screen()
    print("\n📊 Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Show Category Bar Chart")
    print("5. Show Monthly Summary")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        show_total()
    elif choice == '4':
        show_category_bar()
    elif choice == '5':
        show_monthly_summary()
    elif choice == '6':
        confirm = input("Are you sure you want to exit? (y/n): ")
        if confirm.lower() == 'y':
            break
    else:
        print("Invalid choice!")

    input("\nPress Enter to continue...")