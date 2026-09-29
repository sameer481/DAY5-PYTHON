"""
===============================================================================
DAY 5: PYTHON LISTS & TUPLES - PART 1: LIST BASICS, MUTABILITY & OPERATIONS
===============================================================================
This script covers:
1. List Creation Methods (literals, list() constructor, mixed types, nested lists)
2. List Mutability & Memory Allocation (id() tracking, modifying elements by index & slice)
3. Core List Operations (Concatenation, Repetition, Membership, Identity vs Equality)
4. Indexing & Slicing Techniques (1D & 2D indexing, step stride, slice mutation & deletion)
===============================================================================
"""

import sys

# Ensure UTF-8 output encoding for terminal printing
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def line_separator(title=""):
    print(f"\n{'=' * 25} {title} {'=' * 25}")


# -----------------------------------------------------------------------------
# 1. LIST CREATION METHODS
# -----------------------------------------------------------------------------
line_separator("1. List Creation Methods")

# Empty lists
empty_list_1 = []
empty_list_2 = list()

# List with homogeneous data types
integers = [10, 20, 30, 40, 50]
languages = ["Python", "JavaScript", "C++", "Rust", "Go"]

# List with mixed data types
mixed_list = [42, "Python", 3.14159, True, None, [1, 2]]

# Creating list from iterables using list() constructor
range_list = list(range(1, 6))
str_to_list = list("PYTHON")
tuple_to_list = list((100, 200, 300))

# Nested lists (Matrices / 2D Arrays)
matrix_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Empty List (literal)   : {empty_list_1} (type: {type(empty_list_1).__name__})")
print(f"Integer List           : {integers}")
print(f"Mixed Data Type List   : {mixed_list}")
print(f"Converted from String  : {str_to_list}")
print(f"Converted from Range   : {range_list}")
print(f"2D Matrix (3x3)        :\n  {matrix_2d[0]}\n  {matrix_2d[1]}\n  {matrix_2d[2]}")


# -----------------------------------------------------------------------------
# 2. LIST MUTABILITY & MEMORY ALLOCATION
# -----------------------------------------------------------------------------
line_separator("2. List Mutability & Memory Allocation")

# Lists in Python are MUTABLE sequences. Elements can be updated, added, or removed in-place.
fruits = ["apple", "banana", "cherry"]
print(f"Original List     : {fruits} | Memory Address (id): {id(fruits)}")

# Updating single element in-place
fruits[1] = "blueberry"
print(f"After Update [1]  : {fruits} | Memory Address (id): {id(fruits)}")
print("-> Notice: The memory address (id) remains IDENTICAL after in-place mutation!")

# Modifying elements via slice assignment
numbers = [10, 20, 30, 40, 50]
print(f"\nBefore Slice Edit : {numbers}")
numbers[1:4] = [200, 300]  # Replacing 3 items with 2 items
print(f"After Slice Edit  : {numbers}")

# Comparing Mutability: List vs String
text_str = "hello"
text_lst = ['h', 'e', 'l', 'l', 'o']
try:
    # text_str[0] = 'H' # This raises TypeError because strings are immutable
    text_lst[0] = 'H'    # Works fine because lists are mutable
    print(f"Mutated List      : {text_lst}")
except TypeError as e:
    print(f"String Error      : {e}")


# -----------------------------------------------------------------------------
# 3. CORE LIST OPERATIONS
# -----------------------------------------------------------------------------
line_separator("3. Core List Operations")

list_a = [1, 2, 3]
list_b = [4, 5, 6]

# Concatenation (+)
combined = list_a + list_b
print(f"Concatenation (+) : {list_a} + {list_b} -> {combined}")

# Repetition (*)
repeated = list_a * 3
print(f"Repetition (*)    : {list_a} * 3 -> {repeated}")

# Membership Testing (in / not in)
print(f"Is 2 in list_a?   : {2 in list_a}")
print(f"Is 99 in list_a?  : {99 in list_a}")
print(f"Is 99 NOT in list?: {99 not in list_a}")

# Equality (==) vs Identity (is)
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l1

print(f"\nl1 == l2 (Same values?)   : {l1 == l2}")
print(f"l1 is l2 (Same object?)   : {l1 is l2}  | id(l1): {id(l1)}, id(l2): {id(l2)}")
print(f"l1 is l3 (Aliased object?): {l1 is l3}  | id(l1): {id(l1)}, id(l3): {id(l3)}")


# -----------------------------------------------------------------------------
# 4. INDEXING & SLICING TECHNIQUES
# -----------------------------------------------------------------------------
line_separator("4. Indexing & Slicing Techniques")

sample_list = ["P", "y", "t", "h", "o", "n", "3", ".", "1", "2"]
# Index positive: 0    1    2    3    4    5    6    7    8    9
# Index negative:-10  -9   -8   -7   -6   -5   -4   -3   -2   -1

print(f"Original List       : {sample_list}")
print(f"First element [0]   : {sample_list[0]}")
print(f"Last element [-1]   : {sample_list[-1]}")
print(f"5th element [4]     : {sample_list[4]}")

# Slicing syntax: list[start : stop : step]
print(f"\nSlicing [0:6]       : {sample_list[0:6]}")
print(f"Slicing [:4]        : {sample_list[:4]}")
print(f"Slicing [6:]        : {sample_list[6:]}")
print(f"Step Slicing [::2]  : {sample_list[::2]}")
print(f"Reversed list [::-1]: {sample_list[::-1]}")
print(f"Negative Step [8:2:-2]: {sample_list[8:2:-2]}")

# 2D Matrix Indexing
grid = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]
print(f"\nMatrix Element [1][2] (Row 1, Col 2) : {grid[1][2]}")
print(f"Matrix Sub-row [0][1:]               : {grid[0][1:]}")

# Deleting elements using del and slices
numbers_demo = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"\nBefore del numbers_demo[2:5] : {numbers_demo}")
del numbers_demo[2:5]
print(f"After del numbers_demo[2:5]  : {numbers_demo}")

del numbers_demo[0]
print(f"After del numbers_demo[0]    : {numbers_demo}")
