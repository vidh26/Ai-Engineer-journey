# Personal Expense Analyzer
# Uses Python basics + NumPy to analyze daily expenses and show reports/alerts.

import numpy as np


# =====================
# 1. Data definitions
# =====================

# Days of the week
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri"])

# Expense categories
categories = np.array(["Food", "Travel", "Shopping", "Bills"])

# Expenses: each row = one day, each column = one category
# Order of columns matches 'categories' list: [Food, Travel, Shopping, Bills]
expenses = np.array([
    [200,  50, 300,  0],   # Mon
    [150, 100,  50, 200],  # Tue
    [300,  80, 400,  0],   # Wed
    [180,  60, 100, 200],  # Thu
    [250, 120, 600,  0],   # Fri
])

# Daily budget limit
daily_budget = 600


# =====================
# 2. Calculation functions (NumPy-based)
# =====================

def total_per_day(expenses_array):
    """
    Return total expense per day as a 1D NumPy array.
    """
    return expenses_array.sum(axis=1)


def total_per_category(expenses_array):
    """
    Return total expense per category as a 1D NumPy array.
    """
    return expenses_array.sum(axis=0)


def average_per_day(expenses_array):
    """
    Return average expense per day as a 1D NumPy array.
    """
    return expenses_array.mean(axis=1)


def average_per_category(expenses_array):
    """
    Return average expense per category as a 1D NumPy array.
    """
    return expenses_array.mean(axis=0)


# =====================
# 3. Logic functions (conditionals, etc.)
# =====================

def classify_day(total, budget):
    """
    Classify a day as Low/Normal/High based on total spending and budget.
    """
    if total < 0.5 * budget:
        return "Low"
    elif total <= budget:
        return "Normal"
    else:
        return "High"


# =====================
# 4. Reporting functions (printing)
# =====================

def print_daily_summary(days, totals, avgs, budget):
    """
    Print a per-day expense summary with classification.
    """
    print("Daily Expense Summary")
    print("-" * 55)
    for i in range(len(days)):
        status = classify_day(totals[i], budget)
        print(f"{days[i]}: Total={totals[i]}, Avg={avgs[i]:.2f}, Status={status}")
    print("-" * 55)


def print_category_summary(categories, totals, avgs):
    """
    Print a per-category expense summary.
    """
    print("
Category-wise Summary")
    print("-" * 55)
    for j in range(len(categories)):
        print(f"{categories[j]}: Total={totals[j]}, Avg={avgs[j]:.2f}")
    print("-" * 55)
")"

def find_highest_spending_day(days, totals):
    """
    Return (day_name, total_amount) for the highest spending day.
    """
    idx = totals.argmax()
    return days[idx], totals[idx]


def find_highest_spending_category(categories, totals):
    """
    Return (category_name, total_amount) for the highest spending category.
    """
    idx = totals.argmax()
    return categories[idx], totals[idx]


# =====================
# 5. Main program flow
# =====================

if __name__ == "__main__":
    # Compute statistics using NumPy-based functions
    daily_totals = total_per_day(expenses)
    daily_avgs = average_per_day(expenses)

    cat_totals = total_per_category(expenses)
    cat_avgs = average_per_category(expenses)

    # Print daily summary report
    print_daily_summary(days, daily_totals, daily_avgs, daily_budget)

    # Print category-wise summary report
    print_category_summary(categories, cat_totals, cat_avgs)

    # Find and print highest spending day and category
    day_name, day_amt = find_highest_spending_day(days, daily_totals)
    cat_name, cat_amt = find_highest_spending_category(categories, cat_totals)

    print(f"\nHighest spending day: {day_name} ({day_amt})")
    print(f"Highest spending category: {cat_name} ({cat_amt})")

    # Budget alerts using loops + conditionals
    print("\nBudget Alerts")
    print("-" * 55)
    for i in range(len(days)):
        if daily_totals[i] > daily_budget:
            excess = daily_totals[i] - daily_budget
            print(f"⚠️  {days[i]}: You exceeded your daily budget by {excess}")
    print("-" * 55)