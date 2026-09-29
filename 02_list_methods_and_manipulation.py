"""
===============================================================================
DAY 5: PYTHON LISTS & TUPLES - PART 2: BUILT-IN METHODS & LIST MANIPULATION
===============================================================================
This script covers:
1. Insertion Methods (append, extend, insert)
2. Removal Methods (pop, remove, clear, del)
3. Searching & Counting Methods (index, count)
4. Sorting & Reversing (sort, sorted, reverse, custom lambda key functions)
5. Copying Lists (Shallow Copy vs Deep Copy using copy module)
===============================================================================
"""

import sys
import copy

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def line_separator(title=""):
    print(f"\n{'=' * 25} {title} {'=' * 25}")


# -----------------------------------------------------------------------------
# 1. INSERTION METHODS (append, extend, insert)
# -----------------------------------------------------------------------------
line_separator("1. Insertion Methods (append, extend, insert)")

languages = ["Python", "JavaScript"]
print(f"Initial List      : {languages}")

# append(item): Adds a SINGLE element to the end of the list
languages.append("Go")
print(f"After append('Go'): {languages}")

# append with a list creates a nested element!
languages.append(["C++", "Rust"])
print(f"After append list : {languages}")  # Notice nested list at the end

# extend(iterable): Unpacks and appends each element of the iterable
languages.pop()  # Remove nested list
languages.extend(["C++", "Rust"])
print(f"After extend list : {languages}")

# insert(index, item): Inserts an element at a specific index
languages.insert(1, "TypeScript")
print(f"After insert(1)   : {languages}")


# -----------------------------------------------------------------------------
# 2. REMOVAL METHODS (pop, remove, clear, del)
# -----------------------------------------------------------------------------
line_separator("2. Removal Methods (pop, remove, clear, del)")

items = ["apple", "banana", "cherry", "date", "banana", "fig"]
print(f"Initial Items     : {items}")

# remove(value): Removes FIRST occurrence of value
items.remove("banana")
print(f"After remove('banana') : {items}")

# Trying to remove a non-existent item raises ValueError
try:
    items.remove("mango")
except ValueError as e:
    print(f"Caught expected error: {e}")

# pop(index): Removes and RETURNS item at specified index (default is last index -1)
popped_last = items.pop()
print(f"Popped last item  : '{popped_last}' -> List now: {items}")

popped_index_1 = items.pop(1)
print(f"Popped index 1    : '{popped_index_1}' -> List now: {items}")

# del statement: Deletes element or slice
del items[0]
print(f"After del items[0]: {items}")

# clear(): Removes all elements, leaving empty list
items_copy = items.copy()
items_copy.clear()
print(f"After clear()     : {items_copy}")


# -----------------------------------------------------------------------------
# 3. SEARCHING & COUNTING (index, count)
# -----------------------------------------------------------------------------
line_separator("3. Searching & Counting (index, count)")

scores = [85, 92, 78, 92, 100, 85, 92, 64]
print(f"Scores List       : {scores}")

# count(value): Number of occurrences
count_92 = scores.count(92)
print(f"Count of 92       : {count_92}")

# index(value, [start, stop]): Index of first occurrence
first_85 = scores.index(85)
print(f"First index of 85 : {first_85}")

# Index search with start index parameter
second_85 = scores.index(85, first_85 + 1)
print(f"Second index of 85: {second_85}")

# Safe search pattern using 'in' operator
search_val = 99
if search_val in scores:
    print(f"Found {search_val} at index {scores.index(search_val)}")
else:
    print(f"Value {search_val} is NOT present in the list.")


# -----------------------------------------------------------------------------
# 4. SORTING & REVERSING (sort vs sorted, key functions)
# -----------------------------------------------------------------------------
line_separator("4. Sorting & Reversing")

nums = [42, 12, 89, 7, 33, 100, 25]
print(f"Original Nums     : {nums}")

# sorted(): Returns a NEW sorted list, leaves original unchanged
sorted_nums = sorted(nums)
print(f"sorted(nums)      : {sorted_nums}")
print(f"Original Unchanged: {nums}")

# sort(): Sorts the list IN-PLACE (returns None)
nums.sort()
print(f"nums.sort()       : {nums}")

# Sorting in Descending Order
nums.sort(reverse=True)
print(f"Descending sort   : {nums}")

# Custom Sorting using `key` parameter (Lambda functions)
words = ["python", "c", "javascript", "assembly", "go", "typescript"]

# Sort by word length
words.sort(key=len)
print(f"\nSorted by length  : {words}")

# Sort tuples by 2nd element (score)
students = [("Alice", 88), ("Bob", 95), ("Charlie", 72), ("Diana", 91)]
students.sort(key=lambda s: s[1], reverse=True)
print(f"Students by score : {students}")

# reverse() vs reversed()
sample = [1, 2, 3, 4, 5]
sample.reverse()  # In-place reversal
print(f"\nIn-place reversed : {sample}")

rev_iter = reversed([10, 20, 30])  # Returns an iterator
print(f"reversed() list   : {list(rev_iter)}")


# -----------------------------------------------------------------------------
# 5. COPYING LISTS (Shallow vs Deep Copy)
# -----------------------------------------------------------------------------
line_separator("5. Shallow Copy vs Deep Copy")

# 1D List Shallow Copy (Works fine for flat lists)
orig = [1, 2, 3]
shallow = orig.copy()  # or list(orig) or orig[:]
shallow[0] = 99
print(f"1D Shallow Copy test -> Orig: {orig}, Shallow: {shallow}")

# Nested List Shallow Copy Failure
nested_orig = [[1, 2], [3, 4]]
nested_shallow = nested_orig.copy()
nested_shallow[0][0] = 999  # Mutating nested sublist

print(f"\nNested Shallow Copy (FAILURE CASE):")
print(f"  nested_orig    : {nested_orig}  (Notice index [0][0] CHANGED!)")
print(f"  nested_shallow : {nested_shallow}")

# Deep Copy Fix using `copy.deepcopy()`
nested_orig_2 = [[1, 2], [3, 4]]
nested_deep = copy.deepcopy(nested_orig_2)
nested_deep[0][0] = 999

print(f"\nNested Deep Copy (CORRECT CASE):")
print(f"  nested_orig_2  : {nested_orig_2}  (Original stays UNTOUCHED)")
print(f"  nested_deep    : {nested_deep}")
