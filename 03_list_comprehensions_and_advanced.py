"""
===============================================================================
DAY 5: PYTHON LISTS & TUPLES - PART 3: LIST COMPREHENSIONS & ADVANCED CONCEPTS
===============================================================================
This script covers:
1. Basic List Comprehension vs Traditional loops
2. Conditional List Comprehensions (Filtering with 'if')
3. Ternary Conditional Comprehensions ('if-else' expression mapping)
4. Nested List Comprehensions (Flattening matrices, Transposition, Grids)
5. Memory & Performance Benchmark (List Comprehension vs Generator vs Loop vs map/filter)
===============================================================================
"""

import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def line_separator(title=""):
    print(f"\n{'=' * 25} {title} {'=' * 25}")


# -----------------------------------------------------------------------------
# 1. BASIC LIST COMPREHENSION
# -----------------------------------------------------------------------------
line_separator("1. Basic List Comprehension vs Traditional Loop")

# Objective: Create a list of squares for numbers 1 to 10

# Approach A: Traditional For-Loop
squares_loop = []
for i in range(1, 11):
    squares_loop.append(i ** 2)

# Approach B: List Comprehension -> [expression for item in iterable]
squares_comp = [i ** 2 for i in range(1, 11)]

print(f"Traditional Loop Result : {squares_loop}")
print(f"Comprehension Result    : {squares_comp}")
print(f"Are results identical?  : {squares_loop == squares_comp}")

# String manipulation using comprehension
names = ["alice", "bob", "charlie", "diana"]
uppercase_names = [name.upper() for name in names]
print(f"\nOriginal Names          : {names}")
print(f"Uppercase Names         : {uppercase_names}")


# -----------------------------------------------------------------------------
# 2. CONDITIONAL LIST COMPREHENSION (FILTERING WITH 'IF')
# -----------------------------------------------------------------------------
line_separator("2. Filtering with 'if' Condition")

# Syntax: [expression for item in iterable if condition]

numbers = [12, 45, 68, 23, 89, 90, 34, 11, 76, 50]
print(f"Original Numbers        : {numbers}")

# Filter even numbers
evens = [n for n in numbers if n % 2 == 0]
print(f"Even Numbers Only       : {evens}")

# Filter numbers greater than 50
greater_50 = [n for n in numbers if n > 50]
print(f"Numbers > 50            : {greater_50}")

# Filter words based on criteria (starts with 'p' and length > 4)
words = ["python", "java", "php", "pandas", "pytorch", "c", "perl"]
filtered_words = [w.capitalize() for w in words if w.startswith('p') and len(w) > 4]
print(f"Filtered Python Words   : {filtered_words}")


# -----------------------------------------------------------------------------
# 3. TERNARY CONDITIONAL IN COMPREHENSION ('IF-ELSE')
# -----------------------------------------------------------------------------
line_separator("3. Ternary 'if-else' Mapping")

# Syntax: [true_expr if condition else false_expr for item in iterable]

scores = [85, 42, 90, 58, 73, 38, 95, 61]
print(f"Student Scores          : {scores}")

# Map scores to "PASS" (>=60) or "FAIL" (<60)
results = ["PASS" if s >= 60 else "FAIL" for s in scores]
print(f"Pass/Fail Labels        : {results}")

# Zip names and pass/fail status
students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]
graded_students = [(name, score, "PASS" if score >= 60 else "FAIL")
                   for name, score in zip(students, scores)]
print("\nGraded Student Roster:")
for student in graded_students:
    print(f"  {student[0]:<10} | Score: {student[1]:<3} | Status: {student[2]}")


# -----------------------------------------------------------------------------
# 4. NESTED LIST COMPREHENSIONS
# -----------------------------------------------------------------------------
line_separator("4. Nested List Comprehensions")

# Example 1: Flattening a 2D Matrix (Converting 2D list to 1D)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Original 2D Matrix      : {matrix}")

flattened = [num for row in matrix for num in row]
print(f"Flattened 1D List       : {flattened}")

# Example 2: Matrix Transposition (Rows become columns)
# Original matrix: 3x3
# Row 0: [1, 2, 3] -> Col 0: [1, 4, 7]
transposed = [[row[col_idx] for row in matrix] for col_idx in range(len(matrix[0]))]
print(f"Transposed Matrix       :")
for r in transposed:
    print(f"  {r}")

# Example 3: Generating Coordinate Grid (x, y) for x, y in range(3)
grid = [(x, y) for x in range(3) for y in range(3)]
print(f"\nGenerated 3x3 Grid      : {grid}")


# -----------------------------------------------------------------------------
# 5. PERFORMANCE & MEMORY COMPARISON
# -----------------------------------------------------------------------------
line_separator("5. Memory & Performance Benchmark")

LIMIT = 1_000_000

print(f"Benchmarking with N = {LIMIT:,} items...\n")

# Memory Footprint Comparison using sys.getsizeof()
comp_list = [x * 2 for x in range(LIMIT)]
gen_expr = (x * 2 for x in range(LIMIT))

list_bytes = sys.getsizeof(comp_list)
gen_bytes = sys.getsizeof(gen_expr)

print(f"Memory Usage:")
print(f"  List Comprehension : {list_bytes / (1024 * 1024):.2f} MB ({list_bytes:,} bytes)")
print(f"  Generator Expression: {gen_bytes} bytes ({gen_bytes / 1024:.2f} KB)")
print(f"  -> Generator saves ~{(list_bytes - gen_bytes) / (1024 * 1024):.2f} MB of RAM!")

# Speed Comparison: Loop vs Comprehension vs map()
t0 = time.perf_counter()
res_loop = []
for x in range(LIMIT):
    res_loop.append(x * 2)
t1 = time.perf_counter()

t2 = time.perf_counter()
res_comp = [x * 2 for x in range(LIMIT)]
t3 = time.perf_counter()

t4 = time.perf_counter()
res_map = list(map(lambda x: x * 2, range(LIMIT)))
t5 = time.perf_counter()

print(f"\nExecution Speed Comparison:")
print(f"  Traditional Loop   : {(t1 - t0) * 1000:.2f} ms")
print(f"  List Comprehension : {(t3 - t2) * 1000:.2f} ms")
print(f"  map() + list()     : {(t5 - t4) * 1000:.2f} ms")
