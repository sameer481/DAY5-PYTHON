# Day 5: Master Python Lists & Tuples 🐍

Welcome to Day 5 of learning Python! This repository contains comprehensive guides, detailed runnable Python scripts, custom algorithms, performance benchmarks, and production-grade practical projects covering **Python Lists**, **Tuples**, **Mutability vs Immutability**, **List Comprehensions**, **Tuple Unpacking & Star (*) Operators**, `collections.namedtuple`, and **Real-World Practical Applications**.

---

## 📁 Repository Structure

```text
DAY5-PYTHON/
│
├── 01_list_basics_and_operations.py         # List creation, mutability, id() tracking, 1D/2D indexing & slicing
├── 02_list_methods_and_manipulation.py     # append, extend, insert, pop, remove, sort, sorted, shallow vs deepcopy
├── 03_list_comprehensions_and_advanced.py  # Comprehensions, if filtering, ternary if-else, matrix flattening & memory benchmark
├── 04_tuple_basics_and_operations.py       # Tuple creation, single-item gotcha (42,), immutability, hashability & dict keys
├── 05_advanced_tuples_and_unpacking.py      # Unpacking, star (*) expressions, function returns, zip, enumerate & namedtuple
├── 06_practical_projects.py                # 4 Real-world projects: Grade manager, Shopping cart, Expense tracker, Task priority queue
└── README.md                               # Comprehensive documentation and quick execution guide
```

---

## 📚 Detailed Topic Breakdown

### 1. List Basics, Mutability & Operations (`01_list_basics_and_operations.py`)
- **List Creation**: Literals (`[]`), constructor (`list()`), mixed data types, nested matrices.
- **Mutability & Memory Allocation**:
  - Lists in Python are **mutable** sequences. Modifying elements in-place retains the object memory address (`id()`).
  - Comparing list mutability vs string immutability.
- **Slice Assignment & Deletion**: Modifying sub-ranges of elements with slice assignment (`lst[1:4] = [200, 300]`) and deleting elements with `del`.
- **Core Operations**: Concatenation (`+`), repetition (`*`), membership (`in` / `not in`), identity (`is`) vs equality (`==`).

---

### 2. Built-in List Methods & Manipulation (`02_list_methods_and_manipulation.py`)
- **Insertion**:
  - `append(item)`: Adds a single item to the end.
  - `extend(iterable)`: Unpacks and appends each element of the iterable.
  - `insert(index, item)`: Inserts element at a specific position.
- **Removal**:
  - `pop(index)`: Removes and returns item (defaults to last element `-1`).
  - `remove(value)`: Removes first occurrence of value (raises `ValueError` if missing).
  - `clear()`: Empties the list.
- **Sorting & Reversing**:
  - `sort(key=..., reverse=...)`: In-place sorting.
  - `sorted(iterable)`: Returns a new sorted list (original stays untouched).
  - Custom key sorting with `lambda` functions.
- **Shallow Copy vs Deep Copy**:
  - `copy()` / `[:]`: Shallow copy (fails for nested lists!).
  - `copy.deepcopy()`: Deep copy (recursively duplicates nested objects).

---

### 3. List Comprehensions & Memory Benchmarks (`03_list_comprehensions_and_advanced.py`)
- **Basic Comprehension**: `[expression for item in iterable]`.
- **Filtering with `if`**: `[expr for item in iterable if condition]`.
- **Ternary Mapping (`if-else`)**: `[true_expr if condition else false_expr for item in iterable]`.
- **Nested List Comprehensions**:
  - Flattening 2D matrices into 1D lists.
  - Matrix Transposition ($3 \times 3$ row-column swap).
  - Generating 2D coordinate grids.
- **Memory & Performance Benchmarks**:
  - Comparing `sys.getsizeof()` between List Comprehension ($8.06 \text{ MB}$) and Generator Expressions ($208 \text{ bytes}$).
  - Execution speed comparison between loops, list comprehensions, and `map()`.

---

### 4. Tuple Basics, Immutability & Hashability (`04_tuple_basics_and_operations.py`)
- **Tuple Creation & Gotchas**:
  - Parentheses syntax `()`, comma-separated values `1, 2, 3`.
  - **Single-Element Gotcha**: `(42)` is an `int`, whereas `(42,)` is a `tuple`.
- **Tuple Immutability**:
  - Elements cannot be modified or assigned after creation.
  - Attempting `tup[0] = X` raises a `TypeError`.
- **Hashability & Dictionary Keys**:
  - Because tuples are immutable, they are **hashable** and can be used as keys in dictionaries or elements in sets (lists cannot!).
- **Built-in Methods**: `count()` and `index()`.
- **Mutable Objects Inside Tuples**: Demonstrating reference immutability vs value mutability when a list is inside a tuple.

---

### 5. Advanced Tuples, Unpacking & Namedtuples (`05_advanced_tuples_and_unpacking.py`)
- **Standard Unpacking & Swapping**:
  - `a, b, c = tuple_data`
  - Pythonic variable swapping: `x, y = y, x`.
- **Extended Star (`*`) Unpacking**:
  - `head, *tail = items`
  - `first, *middle, last = items`
  - Ignoring values with underscore `_`.
- **Function Returns**: Returning multiple values from functions using tuples.
- **Tuple Iteration**: Combining tuples with `zip()`, `enumerate()`, and `dict.items()`.
- **`collections.namedtuple`**:
  - Lightweight, struct-like objects with named fields (`Car.make`, `Car.price`).
  - Helper methods: `_asdict()` and `_replace()`.

---

### 6. Real-World Practical Projects (`06_practical_projects.py`)
1. **Student Academic Grade Manager & Analytics**: Computes averages, assigns letter grades, ranks top students, and filters honor roll using comprehensions.
2. **E-Commerce Shopping Cart & Checkout System**: Cart addition, deletion, promo discount calculations, sales tax, shipping fees, and itemized receipt generation.
3. **Personal Financial Expense Analyzer**: Namedtuple expense tracking, category breakdown, spending percentages, and largest expense detection.
4. **Task Priority Queue Scheduler**: Priority queue simulation (Critical, High, Medium, Low) sorting and task status processing engine.

---

## ⚙️ How to Run the Scripts

Ensure you have **Python 3.8+** installed.

```bash
# Navigate to the Day 5 directory
cd DAY5-PYTHON

# Run individual topic scripts:
python 01_list_basics_and_operations.py
python 02_list_methods_and_manipulation.py
python 03_list_comprehensions_and_advanced.py
python 04_tuple_basics_and_operations.py
python 05_advanced_tuples_and_unpacking.py
python 06_practical_projects.py
```

---

## 🎯 Quick Comparison: Lists vs Tuples

| Feature | Python Lists (`list`) | Python Tuples (`tuple`) |
| :--- | :--- | :--- |
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` |
| **Mutability** | **Mutable** (Can add/remove/modify) | **Immutable** (Cannot change once created) |
| **Size / Memory** | Larger memory overhead (dynamic resizing) | Smaller memory footprint |
| **Performance** | Slightly slower iteration & allocation | Faster iteration & creation |
| **Use as Dict Key** | ❌ No (`TypeError: unhashable type`) | ✅ Yes (If elements are hashable) |
| **Methods Count** | 11+ methods (`append`, `pop`, `sort`...) | 2 methods (`count`, `index`) |
| **Primary Intent** | Homogeneous, dynamic collections | Heterogeneous, fixed data structures |

---

## 🌟 Key Takeaways

- **Mutability**: Use **Lists** when data needs to change dynamically. Use **Tuples** for read-only fixed data structures (coordinates, records).
- **Deepcopy**: Use `copy.deepcopy()` when copying nested lists to avoid unexpected side effects.
- **Generators vs Comprehensions**: Use Generator expressions `(x for x in data)` when working with huge datasets ($10^6+$ items) to keep RAM usage minimal.
- **Namedtuples**: Use `collections.namedtuple` for self-documenting, lightweight data objects without full class overhead.
