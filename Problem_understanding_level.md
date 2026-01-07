# Problem: Compatibility Check Using Sets
```
Ali and his fiancée are experiencing emotional conflicts. However, because they deeply care about each other, they decided to consult a psychologist.

The psychologist evaluates **n characteristics** for each of them.  
Each characteristic is represented by an integer.

The **compatibility score** between Ali and his fiancée is defined as the **number of common characteristics** they share.

If their compatibility score is **strictly greater than (n / 2)**, then everything will be fine.

Counting common characteristics manually is difficult for the psychologist, especially because the number of characteristics can be very large.  
Your task is to help by writing an efficient program.

---

## Important Hint

⚠️ **Do not use lists** to solve this problem.  
Use **sets**, because set operations are significantly faster, and the number of characteristics can be as large as **1,000,000**.

---

## Task

Write a program that:
- Reads Ali’s characteristics
- Reads his fiancée’s characteristics
- Prints **YES** if the number of shared characteristics is **greater than (n / 2)**
- Otherwise, prints **NO**

---

## Input Format

1. First line: an integer `n`  
   → number of characteristics for each person

2. Second line: `n` space-separated integers  
   → characteristics of **Ali**

3. Third line: `n` space-separated integers  
   → characteristics of **Ali’s fiancée**

📌 Inputs **must** be space-separated.  

Valid input example:
1 2 3 4

Invalid input example:
1234
```
---

## Output Format

- Print `YES` if compatibility > `n / 2`
- Otherwise, print `NO`

---

## Sample Input 1
```
4
1 2 3 4
3 4 5 6
```
## Sample Output 1

## Explanation

The common characteristics are `{3, 4}`, so the compatibility score is `2`.

Since:
```
n / 2 = 4 / 2 = 2
```

And the compatibility score is **not strictly greater than 2**, the answer is `NO`.

⚠️ **Important:**  
Compatibility must be **greater than (n / 2)**.  
Equality is **not sufficient**.

---

## Additional Examples

### Valid Input Example
```
4
5 25 7 111
3 4 5 6
```
❌ The second person has **4 inputs**, but `n = 3`.

---

## Recommended Approach (High-Level)

1. Read `n`
2. Convert both input lines into **sets**
3. Compute the intersection
4. Compare `len(intersection)` with `n / 2`

This approach ensures:
- **O(n)** time complexity
- Efficient memory usage
- Scalability for large inputs

---

## Key Concept Used

- **Set Intersection**
- **Efficient Membership Checking**
- **Strict Comparison Logic**

This problem is a practical example of how mathematical set theory directly applies to real-world algorithmic problems.
