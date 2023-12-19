# Karatsuba Multiplication

This repository contains Python implementations of the classic multiplication algorithm and the Karatsuba multiplication algorithm. The purpose is to compare the performance of these two algorithms for large integer multiplication.

## Contents

- `classic(a, b)`: Classic multiplication function that multiplies two large integers represented as arrays.

- `karatsuba(x, y)`: Karatsuba multiplication function that leverages a divide-and-conquer approach for faster integer multiplication.

- `main`: Example usage of the algorithms with a set of large integers and timing measurements.

## Usage

1. Import the required libraries and functions:

```python
import numpy as np
import timeit
```

2. Define your large integers as arrays:

```python
x = [9, 9, ...]  # Array representing a large integer
y = [9, 9, ...]  # Array representing another large integer
```

3. Measure the execution time of the classic multiplication algorithm:

```python
classic_time = timeit.timeit("classic(x, y)", globals=globals(), number=1)
print("Classic multiplication time:", classic_time)
```

4. Measure the execution time of the Karatsuba multiplication algorithm:

```python
karatsuba_time = timeit.timeit("karatsuba(x, y)", globals=globals(), number=1)
print("Karatsuba multiplication time:", karatsuba_time)
```

## Results

The provided example demonstrates the execution times for both algorithms using a set of large integers.

Feel free to experiment with different input values and analyze the performance of classic multiplication versus Karatsuba multiplication.
