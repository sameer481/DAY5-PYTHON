"""
===============================================================================
DAY 5: PYTHON LISTS & TUPLES - PART 6: PRACTICAL REAL-WORLD PROJECTS
===============================================================================
This script features 4 production-grade practical projects:
1. Project 1: Student Academic Grade Manager & Class Analytics Engine
2. Project 2: E-Commerce Shopping Cart & Checkout Receipt System
3. Project 3: Personal Financial Expense & Category Analyzer (using namedtuples)
4. Project 4: Task Priority Queue Scheduler & Status Dispatcher
===============================================================================
"""

import sys
from collections import namedtuple

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def section_header(title):
    print(f"\n{'=' * 75}")
    print(f" 🚀 {title.upper()}")
    print(f"{'=' * 75}")


# =============================================================================
# PROJECT 1: STUDENT ACADEMIC GRADE MANAGER & CLASS ANALYTICS
# =============================================================================
def run_project_1():
    section_header("Project 1: Student Grade Manager & Class Analytics")

    # Raw database: List of student records (tuples: id, name, scores_list)
    raw_students = [
        ("STU-101", "Alice Vance", [88, 92, 95, 90]),
        ("STU-102", "Bob Miller", [72, 65, 80, 74]),
        ("STU-103", "Charlie Davis", [95, 98, 92, 99]),
        ("STU-104", "Diana Prince", [58, 62, 70, 55]),
        ("STU-105", "Ethan Hunt", [84, 86, 89, 91]),
    ]

    def get_letter_grade(avg):
        if avg >= 90: return "A+"
        elif avg >= 80: return "A"
        elif avg >= 70: return "B"
        elif avg >= 60: return "C"
        else: return "F"

    # Processing analytics using list comprehensions & tuple unpacking
    processed = []
    for sid, name, scores in raw_students:
        avg_score = sum(scores) / len(scores)
        letter = get_letter_grade(avg_score)
        processed.append((sid, name, scores, round(avg_score, 2), letter))

    # Sort students by average score in descending order
    processed.sort(key=lambda s: s[3], reverse=True)

    print(f"{'ID':<10} | {'Student Name':<16} | {'Scores':<20} | {'Avg':<6} | {'Grade'}")
    print("-" * 65)
    for sid, name, scores, avg, letter in processed:
        scores_str = ", ".join(str(s) for s in scores)
        print(f"{sid:<10} | {name:<16} | [{scores_str:<18}] | {avg:<6.2f} | {letter}")

    # Class-wide aggregate analytics
    all_averages = [student[3] for student in processed]
    class_avg = sum(all_averages) / len(all_averages)
    top_student = processed[0]
    lowest_student = processed[-1]

    # Filter honor roll students (Avg >= 85) using list comprehension
    honor_roll = [f"{s[1]} ({s[3]})" for s in processed if s[3] >= 85]

    print("-" * 65)
    print(f"📊 Class Overall Average  : {class_avg:.2f}%")
    print(f"🏆 Top Performing Student : {top_student[1]} ({top_student[3]}% - {top_student[4]})")
    print(f"⚠️ Lowest Student Score  : {lowest_student[1]} ({lowest_student[3]}% - {lowest_student[4]})")
    print(f"🌟 Honor Roll (Avg >= 85) : {', '.join(honor_roll)}")


# =============================================================================
# PROJECT 2: E-COMMERCE SHOPPING CART & CHECKOUT RECEIPT SYSTEM
# =============================================================================
def run_project_2():
    section_header("Project 2: E-Commerce Shopping Cart & Checkout System")

    # Shopping cart: list of item tuples (item_id, name, unit_price, qty)
    cart = [
        ("P101", "Wireless Noise-Canceling Headphones", 149.99, 1),
        ("P102", "Ergonomic Mechanical Keyboard", 89.50, 2),
        ("P103", "USB-C Fast Charging Hub", 29.99, 3),
        ("P104", "Ultra-wide 34\" Monitor", 499.00, 1),
    ]

    print("🛒 ORIGINAL CART CONTENTS:")
    for item in cart:
        print(f"  [{item[0]}] {item[1]:<38} x{item[3]} @ ${item[2]:.2f}")

    # Cart Manipulation: Add new item, update quantity, remove an item
    # 1. Add item
    cart.append(("P105", "Precision Gaming Mouse", 45.00, 1))

    # 2. Remove P103 (Fast Charging Hub)
    cart = [item for item in cart if item[0] != "P103"]

    # 3. Update quantity for P102 (Keyboard from 2 -> 1)
    updated_cart = []
    for item_id, name, price, qty in cart:
        if item_id == "P102":
            updated_cart.append((item_id, name, price, 1))
        else:
            updated_cart.append((item_id, name, price, qty))
    cart = updated_cart

    # Checkout Calculations
    PROMO_DISCOUNT_PERCENT = 10.0  # 10% OFF
    TAX_RATE_PERCENT = 8.5        # 8.5% Sales Tax
    SHIPPING_FEE = 15.00          # Flat shipping fee

    subtotal = sum(price * qty for _, _, price, qty in cart)
    discount_amount = subtotal * (PROMO_DISCOUNT_PERCENT / 100.0)
    discounted_subtotal = subtotal - discount_amount
    tax_amount = discounted_subtotal * (TAX_RATE_PERCENT / 100.0)
    grand_total = discounted_subtotal + tax_amount + SHIPPING_FEE

    # Print Itemized Checkout Receipt
    print("\n" + "=" * 60)
    print(f"{'OFFICIAL PURCHASE RECEIPT':^60}")
    print("=" * 60)
    print(f"{'Item Description':<35} | {'Qty':<4} | {'Unit':<8} | {'Total'}")
    print("-" * 60)
    for _, name, price, qty in cart:
        line_total = price * qty
        print(f"{name:<35} | {qty:<4} | ${price:<7.2f} | ${line_total:>7.2f}")
    print("-" * 60)
    print(f"{'Subtotal':<47} : ${subtotal:>8.2f}")
    print(f"{'Promo Discount (' + str(PROMO_DISCOUNT_PERCENT) + '%)':<47} : -${discount_amount:>7.2f}")
    print(f"{'Sales Tax (' + str(TAX_RATE_PERCENT) + '%)':<47} : +${tax_amount:>7.2f}")
    print(f"{'Flat Rate Shipping':<47} : +${SHIPPING_FEE:>7.2f}")
    print("=" * 60)
    print(f"{'GRAND TOTAL PAID':<47} : ${grand_total:>8.2f}")
    print("=" * 60)


# =============================================================================
# PROJECT 3: PERSONAL FINANCIAL EXPENSE ANALYZER
# =============================================================================
def run_project_3():
    section_header("Project 3: Personal Financial Expense Analyzer")

    # Struct using namedtuple
    Expense = namedtuple("Expense", ["date", "category", "amount", "description"])

    expenses = [
        Expense("2026-09-01", "Groceries", 125.50, "Supermarket weekly restock"),
        Expense("2026-09-02", "Utilities", 85.00, "Monthly electricity bill"),
        Expense("2026-09-03", "Dining", 42.75, "Dinner with friends"),
        Expense("2026-09-04", "Groceries", 68.20, "Organic market produce"),
        Expense("2026-09-05", "Transportation", 50.00, "Gas station refill"),
        Expense("2026-09-06", "Entertainment", 29.99, "Streaming subscriptions"),
        Expense("2026-09-07", "Dining", 18.50, "Lunch cafe combo"),
        Expense("2026-09-08", "Groceries", 210.00, "Bulk wholesale store"),
    ]

    total_spent = sum(e.amount for e in expenses)

    # Aggregate by Category using dictionary with tuple items
    category_totals = {}
    for e in expenses:
        category_totals[e.category] = category_totals.get(e.category, 0.0) + e.amount

    # Convert dictionary items to sorted list of tuples (Category, Amount)
    sorted_categories = sorted(category_totals.items(), key=lambda cat: cat[1], reverse=True)

    # Highest single expense
    highest_expense = max(expenses, key=lambda e: e.amount)

    print(f"💰 Total Monthly Expenditures : ${total_spent:,.2f}")
    print(f"⚡ Highest Single Expense     : {highest_expense.description} (${highest_expense.amount:.2f} on {highest_expense.date})")

    print("\n📌 SPENDING BY CATEGORY BREAKDOWN:")
    print(f"  {'Category':<16} | {'Total Amount':<12} | {'Percentage'}")
    print("  " + "-" * 45)
    for category, amount in sorted_categories:
        percentage = (amount / total_spent) * 100
        bar = "█" * int(percentage // 5)
        print(f"  {category:<16} | ${amount:<11.2f} | {percentage:>5.1f}%  {bar}")

    # Top 3 Largest Expenses sorted
    sorted_expenses = sorted(expenses, key=lambda e: e.amount, reverse=True)
    print("\n🔍 TOP 3 LARGEST INDIVIDUAL TRANSACTIONS:")
    for idx, e in enumerate(sorted_expenses[:3], 1):
        print(f"  #{idx}. [{e.date}] {e.category:<14} - ${e.amount:<7.2f} ({e.description})")


# =============================================================================
# PROJECT 4: TASK PRIORITY QUEUE SCHEDULER
# =============================================================================
def run_project_4():
    section_header("Project 4: Task Priority Queue Scheduler")

    # Priority Task tuple structure: (priority_num, task_id, title, status)
    # Priority: 1 = CRITICAL, 2 = HIGH, 3 = MEDIUM, 4 = LOW
    task_queue = [
        (3, "TASK-101", "Update user documentation", "PENDING"),
        (1, "TASK-102", "Fix critical security vulnerability in API", "PENDING"),
        (2, "TASK-103", "Refactor database query performance", "PENDING"),
        (4, "TASK-104", "Clean up unused image assets", "PENDING"),
        (1, "TASK-105", "Resolve server crash in checkout endpoint", "PENDING"),
        (2, "TASK-106", "Implement OAuth2 social login", "PENDING"),
    ]

    priority_labels = {1: "🔴 CRITICAL", 2: "🟠 HIGH", 3: "🟡 MEDIUM", 4: "🟢 LOW"}

    print("📋 INITIAL UNORDERED TASK QUEUE:")
    for t in task_queue:
        print(f"  [{priority_labels[t[0]]}] ({t[1]}) {t[2]}")

    # Sorting tasks by priority number (1 comes before 2, 3, 4)
    task_queue.sort(key=lambda task: task[0])

    print("\n⚡ PROCESSING TASKS IN PRIORITY ORDER:")
    print("-" * 65)

    processed_tasks = []
    while task_queue:
        # Pop highest priority task (first element at index 0)
        prio, tid, title, _ = task_queue.pop(0)
        status = "COMPLETED"

        print(f"  Processing [{priority_labels[prio]}] {tid}: '{title}' -> Status: {status}")
        processed_tasks.append((prio, tid, title, status))

    print("-" * 65)
    print(f"✅ Successfully processed all {len(processed_tasks)} queued tasks!")


# =============================================================================
# MAIN DISPATCHER
# =============================================================================
if __name__ == "__main__":
    run_project_1()
    run_project_2()
    run_project_3()
    run_project_4()
