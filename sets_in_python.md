# Sets in Python (Applied Math for Machine Learning)

Sets are one of the most fundamental concepts in mathematics and are heavily used in
machine learning, probability, data preprocessing, and feature engineering.

In Python, sets provide a direct and efficient way to work with mathematical set operations.

---

## 1. Set Initialization & Basic Operations

### 1.1 Create a Set
```python
A = {1, 2, 3, 4}
B = set([3, 4, 5])
```

### ⚠️ Important:
**Sets automatically remove duplicate values.**
```python
A = {1, 1, 2, 2, 3}
print(A)   # {1, 2, 3}
```

### 1.2 Add Element to a Set
```python
A = {1, 2, 3}
A.add(4)
print(A)   # {1, 2, 3, 4}
```

### 1.3 Remove Element from a Set
```python
A.remove(3)   # Raises error if element does not exist
A.discard(5)  # Safe remove (no error)
```

### 1.4 Update Set (Add Multiple Elements)
```python
A.update([5, 6, 7])
print(A)
```

## 2. Set Operators
### Assume:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

## 2.1 Intersection (Common Elements)
```python
A & B
# or
A.intersection(B)
```

Result: ```{3, 4}```

## 2.2 Union (All Unique Elements)
```python
A | B
# or
A.union(B)
```
Result: ```{1, 2, 3, 4, 5, 6}```

## 2.3 Difference
```python
A - B
# or
A.difference(B)
```
Result: ```{1, 2}```

## 2.4 Symmetric Difference
**Elements that are in either set, but not both.**
```python
A ^ B
# or
A.symmetric_difference(B)
```
Result: ```{1, 2, 5, 6}```

## 2.5 itertools (Advanced Combinations)

**The ```itertools``` library is useful for generating combinations and subsets.**
```python
from itertools import combinations

A = {1, 2, 3}
list(combinations(A, 2))
```
**Result:**
```python
[(1, 2), (1, 3), (2, 3)]
```
**Used heavily in:**

* Feature combinations

* Search spaces

* Power set generation

## 3. Logical Operations on Sets
## 3.1 Membership
```python
3 in A
5 not in A
```
## 3.2 Subset
```python
C = {1, 2}
C.issubset(A)
# or
C <= A
```

## 3.3 Power Set
**The power set is the set of all possible subsets.**
```python
from itertools import chain, combinations

def power_set(s):
    s = list(s)
    return chain.from_iterable(
        combinations(s, r) for r in range(len(s)+1)
    )

list(power_set({1, 2, 3}))
```

## 3.4 Complement

Given a universal set ```U```:
```python
U = {1, 2, 3, 4, 5, 6}
A = {2, 4}

complement = U - A
```
## 4. Finite vs Infinite Sets
**Finite Set**
**Has a limited number of elements.**

```python
A = {1, 2, 3}
```
## Infinite Set

**Cannot be fully stored in memory.**

Example (conceptual):
```python
# Infinite mathematical set
Natural numbers: {1, 2, 3, ...}
```

In practice, infinite sets are handled using:

* Generators

* Lazy evaluation

* Mathematical definitions

## 5. Venn Diagrams (Conceptual Understanding)

**Venn diagrams visually represent relationships between sets:**

* Union

* Intersection

* Difference

**They are essential for:**

* Probability

* Statistics

* Feature overlap analysis

## Inclusion–Exclusion Principle

**Used to calculate the size of a union of multiple sets.**

### Formula:
```r
|F ∪ V ∪ T| = (|F| + |V| + |T|)
             − (|F ∩ V| + |F ∩ T| + |V ∩ T|)
             + |F ∩ V ∩ T|
```
**Example:**
```python
F = {1, 2, 3, 4}
V = {3, 4, 5}
T = {4, 5, 6}

result = (
    len(F) + len(V) + len(T)
    - len(F & V) - len(F & T) - len(V & T)
    + len(F & V & T)
)

print(result)
```
## Why Sets Matter in Machine Learning

* Removing duplicates

* Feature selection

* Dataset overlap analysis

* Probability modeling

* Efficient membership checks (O(1))
