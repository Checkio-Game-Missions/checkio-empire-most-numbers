To check sieves for ore we use various sample sets and find the smallest and the biggest stones.
The difference between these values can be used to decide is this sample good for checking.


You are given an array of positive numbers. 
Find the difference between the maximum and minimum element.
Your function should be able to handle an undefined amount of arguments. 
For an empty argument list, the function should return 0.

Floating-point numbers are represented in computer hardware as base 2 (binary) fractions.
So we should check the result with 0.001 precision.

**Input:** An arbitrary number of arguments as numbers (int, float).

**Output:** The difference between maximum and minimum as a number (int, float).

**Example:**

```python
most_difference(1, 2, 3) == 2
most_difference(5, -5) == 10
most_difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4
most_difference() == 0
```

**How it is used:**

Here you will learn about passing an undefined amount of arguments to functions.

**Precondition:**

```python
0 <= len(args) <= 20
all(x > 0 for x in args)
```

