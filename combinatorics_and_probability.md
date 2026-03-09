# Combinatorics and Probability for Machine Learning

In applied mathematics and machine learning, **combinatorics and probability** help us understand how many possible outcomes exist and how likely each outcome is.

These concepts are fundamental for:
- data science
- probabilistic models
- machine learning algorithms
- statistical reasoning


---

# 1. Principle of Addition

The **Addition Principle** states that:

If one event can occur in **m ways** and another event can occur in **n ways**, and these events **cannot happen at the same time**, then the total number of possible outcomes is:

### m + n

## Example

You can travel from city A to city B using:
- 3 different buses
- 2 different trains

Total possible choices:

### 3 + 2 = 5


---

# 2. Principle of Multiplication

The **Multiplication Principle** states that:

If one event occurs in **m ways** and another independent event occurs in **n ways**, then the total number of outcomes is:

### m × n


## Example

A password consists of:
- 3 letters
- 2 digits

If there are:
- 26 possible letters
- 10 possible digits

Total combinations:

### 26³ × 10²


---

# 3. Complement Principle

Sometimes it is easier to count the **opposite event**.

The complement principle states:

*** Total outcomes - undesired outcomes = desired outcomes ***


### Example

Instead of counting numbers **with repeated digits**, we can count numbers **without repeated digits** and subtract.

---

# Python Example: Detecting Numbers with Repeated Digits

```python
count = 0

for num in range(1000, 10000):
    if len(set(str(num))) != len(str(num)):
        count += 1

print(count)
```

## Explanation

Steps:

1- Convert the number to a string.

2- Convert the string to a set.

3- A set removes duplicates automatically.

4- If the length changes, the number had repeated digits.

## Example:

```txt
1123 → set("1123") → {'1','2','3'} → repeated digit
1234 → set("1234") → {'1','2','3','4'} → unique digits
```

# Python Sets for Digit Analysis
```py
set(str(1234))
```
Output:
```txt
{'1','2','3','4'}
```
You can also convert collections into sets:
```py
set([1,2,2,3,4])
```
Output:
```txt
{1,2,3,4}
```
Sets are very useful for:

* removing duplicates

* membership checking

* combinatorics problems


# 4. Permutations

A Permutation is an arrangement of elements where order matters.

Example:
```txt
A B C
```
Possible permutations:
```txt
ABC
ACB
BAC
BCA
CAB
CBA
```
Total:
```txt
3! = 6
```
Python Example
```py
from itertools import permutations

items = ['A','B','C']

for p in permutations(items):
    print(p)
```


# 5. Permutations with Repetition

Sometimes elements can repeat.

Example:

Password with 2 digits:
```txt
00
01
02
...
99
```
Total possibilities:
```txt
10²
```


# 6. Combinations

A Combination is a selection where order does NOT matter.

Example:

Choosing 2 students from:
```txt
A B C
```
Valid combinations:
```txt
AB
AC
BC
```
Total:
```txt
C(3,2) = 3
```
Python Example
```py
from itertools import combinations

items = ['A','B','C']

for c in combinations(items,2):
    print(c)
```


# 7. Inclusion–Exclusion Principle

Used to count elements in overlapping sets.

Formula:

|A ∪ B| = |A| + |B| − |A ∩ B|

For three sets:

|F ∪ V ∪ T| =
(F + V + T)
− (F∩V + F∩T + V∩T)
+ (F∩V∩T)

This prevents double counting.

Used heavily in:

* probability

* combinatorics

* machine learning feature overlap


# 8. Probability

Probability measures how likely an event is.
```txt
Probability = favorable outcomes / total outcomes
```
Random Experiment

A random experiment is an action with an uncertain result.

Examples:

* flipping a coin

* rolling a dice

* selecting a random data sample


## Kolmogorov's Probability Axioms

Andrey Kolmogorov defined the three fundamental rules of probability.

### 1. Non-Negativity
```
P(A) ≥ 0
```
Probability can never be negative.

### 2. Normalization
```
P(S) = 1
```
The probability of the entire sample space is 1.

### 3. Additivity

If events A and B cannot happen together:
```
P(A ∪ B) = P(A) + P(B)
```

# Frequentist vs Bayesian Probability

### Frequentist Approach

Probability is defined by long-run frequency.

Example:
```
If we flip a coin 10,000 times,
the probability of heads approaches 0.5
```
### Bayesian Approach

Probability represents belief or knowledge.

Uses prior information and updates probability with new data.

Bayes theorem:
```
P(A|B) = (P(B|A) * P(A)) / P(B)
```
Used heavily in:

Bayesian machine learning

spam filtering

medical diagnosis

recommendation systems

# Why This Matters for Machine Learning

These concepts help with:

* feature selection

* probabilistic models

* decision theory

* Bayesian inference

* model uncertainty estimation

They form the **mathematical foundation of machine learning**.
