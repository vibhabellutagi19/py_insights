## Time complexity

Time complexity != Time taken because it is dependent on the machine and the configuration of the machine.

**Definition**: The rate at which the time taken increases with respect to the input size.

TC is denoted by Big O notation. every piece of code takes time in terms of big O notation - `O(_)`. `_` is the time complexity of the code and the number of steps taken by the code to execute is the time complexity of the code - `O(_)` is written inside O().

**Rules of time complexity**:
- Constants are ignored.
- Time complexity of a code is always measured in the worst case scenario.
- Avoid lower values.

**Different cases to compute time complexity**:

- Worst case: The maximum time taken by the code to execute.
- Best case: The minimum time taken by the code to execute.
- Average case: The average time taken by the code to execute.

```python

marks = 40

if marks < 25:
    print("grade D")
elif marks < 50:
    print("grade C")
elif marks < 75:
    print("grade B")
else:
    print("grade A")

```

Best case: When the marks are less than 25. We have only 2 operations. Time complexity: O(2)

Worst case: When the marks are greater than 75. We have 4 operations. Time complexity: O(4)

Average case: When the marks are between 25 and 75. We have 3 operations. Time complexity: O(3)

> Always compute the TC in the worst case scenario.

**Types of time complexity**:

1. The Big O notation: 
   - Worst case complexity.
   - Upper bound of the time taken by the code to execute.

2. The Omega notation:
    - Best case complexity.
    - Lower bound of the time taken by the code to execute.

3. The Theta notation:
    - Average case complexity.
    - Average time taken by the code to execute.

## Space complexity

Memory space taken by the code to execute.

Big O notation is always used.

Definition: Auxilary space + input space.
Auxilary space: The space taken by the code to execute.
Input space: The space taken to store the input.

```python
c = a + b

# C is the auxilary space, a and b are the input space.
# The extra space taken by the code to exceute is the auxilary space.
```

Avoid the below approach: Never do anything to the input.

```python

int a # input
int b # input

b = a + b

```
