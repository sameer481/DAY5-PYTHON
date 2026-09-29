"""
===============================================================================
DAY 5: PYTHON LISTS & TUPLES - PART 4: TUPLE BASICS & IMMUTABILITY
===============================================================================
This script covers:
1. Tuple Creation Methods (literals, single-element gotcha, tuple() constructor)
2. Tuple Immutability & Why Tuples Exist (data safety, performance, hashability)
3. Core Operations & Built-in Methods (count, index, slicing)
4. Tuples Containing Mutable Objects (Reference immutability vs value mutability)
===============================================================================
"""

import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def line_separator(title=""):
    print(f"\n{'=' * 25} {title} {'=' * 25}")


# -----------------------------------------------------------------------------
# 1. TUPLE CREATION METHODS
# -----------------------------------------------------------------------------
line_separator("1. Tuple Creation Syntax")

# Empty tuple
empty_tup = ()
empty_tup_2 = tuple()

# Standard tuple with parentheses
point_2d = (10, 20)
rgb_color = (255, 128, 0)
mixed_tup = (1, "Python", 3.14, True)

# Implicit tuple creation (Packing without parentheses)
implicit_tup = 100, 200, 300

# Single-element tuple GOTCHA!
not_a_tuple = (42)       # Evaluates to int 42!
is_a_tuple = (42,)       # Trailing comma creates a 1-element tuple!
is_a_tuple_2 = 42,       # Also creates a 1-element tuple!

print(f"Empty Tuple            : {empty_tup} (type: {type(empty_tup).__name__})")
print(f"2D Point Tuple         : {point_2d}")
print(f"RGB Color Tuple        : {rgb_color}")
print(f"Implicit Tuple (Packing): {implicit_tup} (type: {type(implicit_tup).__name__})")
print(f"\nSingle Element GOTCHA:")
print(f"  (42)  -> Type: {type(not_a_tuple).__name__:<5} | Value: {not_a_tuple}")
print(f"  (42,) -> Type: {type(is_a_tuple).__name__:<5} | Value: {is_a_tuple}")

# Converted from other iterables using tuple()
str_tup = tuple("PYTHON")
lst_tup = tuple([10, 20, 30, 40])

print(f"\nConverted from String  : {str_tup}")
print(f"Converted from List    : {lst_tup}")


# -----------------------------------------------------------------------------
# 2. TUPLE IMMUTABILITY & WHY TUPLES EXIST
# -----------------------------------------------------------------------------
line_separator("2. Tuple Immutability & Benefits")

coordinates = (37.7749, -122.4194)  # San Francisco Lat/Lon
print(f"Coordinates Tuple      : {coordinates} | ID: {id(coordinates)}")

# Attempting in-place element assignment raises TypeError
try:
    coordinates[0] = 40.7128  # Throws TypeError
except TypeError as err:
    print(f"Caught expected error  : {err}")

print("-> Explanation: Tuples are immutable, guaranteeing data integrity across applications.")

# Hashability: Tuples as Dictionary Keys & Set Elements
# Since tuples are immutable, they are HASHABLE (if all elements inside are hashable).
location_dict = {
    (37.7749, -122.4194): "San Francisco",
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

target_coords = (40.7128, -74.0060)
print(f"\nDictionary lookup using Tuple Key {target_coords}:")
print(f"  Result: '{location_dict[target_coords]}'")

# Lists CANNOT be used as dictionary keys because lists are unhashable!
try:
    invalid_dict = {[1, 2]: "Invalid"}
except TypeError as err:
    print(f"List as key error      : {err}")


# -----------------------------------------------------------------------------
# 3. CORE OPERATIONS & METHODS (count, index)
# -----------------------------------------------------------------------------
line_separator("3. Tuple Operations & Built-in Methods")

# Tuples only have TWO built-in methods: count() and index()
data = (10, 20, 30, 20, 40, 20, 50)
print(f"Tuple Data             : {data}")

# 1. count(value)
count_20 = data.count(20)
print(f"data.count(20)         : {count_20}")

# 2. index(value)
first_20_idx = data.index(20)
print(f"data.index(20)         : {first_20_idx}")

second_20_idx = data.index(20, first_20_idx + 1)
print(f"data.index(20, start=2): {second_20_idx}")

# Slicing & Concatenation
tup_a = (1, 2, 3)
tup_b = (4, 5, 6)
combined_tup = tup_a + tup_b
sliced_tup = combined_tup[1:5]
reversed_tup = combined_tup[::-1]

print(f"\nConcatenation (+)      : {tup_a} + {tup_b} -> {combined_tup}")
print(f"Sliced Tuple [1:5]     : {sliced_tup}")
print(f"Reversed Tuple [::-1]  : {reversed_tup}")


# -----------------------------------------------------------------------------
# 4. TUPLES CONTAINING MUTABLE OBJECTS
# -----------------------------------------------------------------------------
line_separator("4. Mutable Objects Inside Immutability")

# A tuple itself cannot be mutated (you cannot replace index [2] with a new object),
# BUT if an element inside the tuple is a mutable object (like a list), THAT OBJECT can be mutated!

hybrid_tuple = ("Alice", 25, ["Math", "Physics"])
print(f"Original Hybrid Tuple  : {hybrid_tuple}")
print(f"Tuple ID               : {id(hybrid_tuple)}")

# Modifying the list inside the tuple
hybrid_tuple[2].append("Computer Science")
print(f"\nAfter mutating sub-list: {hybrid_tuple}")
print(f"Tuple ID after mutation: {id(hybrid_tuple)}")
print("-> Notice: The tuple reference remains immutable, but the contained list was mutated!")

# Attempting to reassign the entire index fails:
try:
    hybrid_tuple[2] = ["Chemistry"]  # TypeError
except TypeError as err:
    print(f"Reassigning element err: {err}")
