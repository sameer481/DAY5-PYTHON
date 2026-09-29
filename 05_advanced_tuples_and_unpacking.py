"""
===============================================================================
DAY 5: PYTHON LISTS & TUPLES - PART 5: ADVANCED TUPLES, UNPACKING & NAMEDTUPLES
===============================================================================
This script covers:
1. Standard Tuple Unpacking & Variable Swapping
2. Extended Unpacking using Star (*) Expressions
3. Function Multi-value Returns via Tuples
4. Tuple Iteration with zip(), enumerate(), and dict.items()
5. Struct-like Records with collections.namedtuple
===============================================================================
"""

import sys
from collections import namedtuple

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def line_separator(title=""):
    print(f"\n{'=' * 25} {title} {'=' * 25}")


# -----------------------------------------------------------------------------
# 1. STANDARD TUPLE UNPACKING & VARIABLE SWAPPING
# -----------------------------------------------------------------------------
line_separator("1. Standard Unpacking & Variable Swapping")

# Packing values into a tuple
person = ("Alice", 28, "Software Engineer")

# Unpacking into individual variables
name, age, profession = person
print(f"Unpacked Variables:")
print(f"  Name       : {name}")
print(f"  Age        : {age}")
print(f"  Profession : {profession}")

# Pythonic Variable Swapping (No temporary variable required!)
x = 10
y = 20
print(f"\nBefore Swap : x = {x}, y = {y}")
x, y = y, x  # Swapping via tuple packing/unpacking under the hood
print(f"After Swap  : x = {x}, y = {y}")

# Mismatched Unpacking Error Demo
try:
    a, b = (1, 2, 3)  # Raises ValueError: too many values to unpack
except ValueError as err:
    print(f"\nMismatched Unpacking Error: {err}")


# -----------------------------------------------------------------------------
# 2. EXTENDED TUPLE UNPACKING WITH STAR (*) EXPRESSIONS
# -----------------------------------------------------------------------------
line_separator("2. Extended Unpacking with Star (*)")

numbers = [10, 20, 30, 40, 50, 60, 70]
print(f"Original List       : {numbers}")

# Extracting head and remaining tail
head, *tail = numbers
print(f"head                : {head}")
print(f"tail (*tail)        : {tail}")

# Extracting first, middle list, and last element
first, *middle, last = numbers
print(f"\nfirst               : {first}")
print(f"middle (*middle)    : {middle}")
print(f"last                : {last}")

# Ignoring unwanted elements using underscore (_) placeholder
product_record = ("Laptop Pro", "SKU-99412", 1299.99, "Electronics", "Warehouse-A", 45)
title, _, price, category, *_ = product_record
print(f"\nExtracted Record:")
print(f"  Title    : {title}")
print(f"  Price    : ${price}")
print(f"  Category : {category}")


# -----------------------------------------------------------------------------
# 3. FUNCTION MULTI-VALUE RETURNS VIA TUPLES
# -----------------------------------------------------------------------------
line_separator("3. Returning Multiple Values from Functions")


def calculate_dataset_stats(data_list):
    """Calculates min, max, sum, and average of a list, returning a tuple."""
    if not data_list:
        return 0, 0, 0, 0.0

    minimum = min(data_list)
    maximum = max(data_list)
    total_sum = sum(data_list)
    average = total_sum / len(data_list)

    return minimum, maximum, total_sum, average  # Returns tuple implicitly


dataset = [88, 92, 79, 95, 64, 83, 100, 72]
# Unpacking function return values directly
min_val, max_val, total, avg = calculate_dataset_stats(dataset)

print(f"Dataset             : {dataset}")
print(f"Minimum Score       : {min_val}")
print(f"Maximum Score       : {max_val}")
print(f"Total Sum           : {total}")
print(f"Average Score       : {avg:.2f}")


# -----------------------------------------------------------------------------
# 4. TUPLE ITERATION (zip, enumerate, dict.items)
# -----------------------------------------------------------------------------
line_separator("4. Iteration Patterns with Tuples")

students = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 91]
grades = ["A+", "B+", "A"]

# 1. zip(): Pair multiple iterables into tuples
print("1. zip() iteration:")
for name, score, grade in zip(students, scores, grades):
    print(f"   Student: {name:<8} | Score: {score} | Grade: {grade}")

# 2. enumerate(): Returns (index, item) tuples
print("\n2. enumerate() iteration:")
for idx, student in enumerate(students, start=1):
    print(f"   Rank #{idx}: {student}")

# 3. dict.items(): Returns (key, value) tuples
user_roles = {"alice": "Admin", "bob": "Editor", "charlie": "Viewer"}
print("\n3. dict.items() iteration:")
for username, role in user_roles.items():
    print(f"   User: {username:<8} -> Role: {role}")


# -----------------------------------------------------------------------------
# 5. STRUCT-LIKE RECORDS WITH collections.namedtuple
# -----------------------------------------------------------------------------
line_separator("5. Structured Records with collections.namedtuple")

# Creating a Named Tuple class blueprint
# Syntax: namedtuple(TypeName, [field_names])
Car = namedtuple("Car", ["make", "model", "year", "price", "is_electric"])

# Instantiating named tuple objects
car1 = Car(make="Tesla", model="Model 3", year=2024, price=38990.00, is_electric=True)
car2 = Car("Porsche", "911 Carrera", 2023, 114400.00, False)

print(f"Car 1 Object        : {car1}")

# Accessing fields by name (Dot Notation)
print(f"\nAccess by Field Name:")
print(f"  Make        : {car1.make}")
print(f"  Model       : {car1.model}")
print(f"  Price       : ${car1.price:,.2f}")
print(f"  Electric?   : {car1.is_electric}")

# Accessing fields by Index (standard tuple behavior still works!)
print(f"\nAccess by Index:")
print(f"  car1[0]     : {car1[0]}")
print(f"  car1[1]     : {car1[1]}")

# Helper Methods of namedtuple
print(f"\nNamedtuple Helper Methods:")
# _asdict(): Converts to OrderedDict / dict
car_dict = car1._asdict()
print(f"  _asdict()   : {car_dict}")

# _replace(): Returns a NEW instance with updated fields (immutability preserved!)
car1_updated = car1._replace(price=36500.00, year=2025)
print(f"  _replace()  : {car1_updated}")
print(f"  Original    : {car1} (Unmodified!)")
