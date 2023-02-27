# Mid-Module-Assignment
## Floyd's Algorithm Rewritten Using Recursion
A Python program that implements Floyd Warshall's algorithm to find the shortest path between any two supplied vertices.

## Python version

  * Python 3.9.13

> Please, make sure that you have updated the python version.

## Project structure
- index.py
- samply.py
- test_cases.py
- test_performance.py
- test_unittest.py

## Execution & Output

The index.py contains the recursive version of Floyd Warshall's algorithm.
By running the index file:

```
python3 index.py
```

it will run the floydNew() function with the standard graph:

```
input = [[0, 7, NO_PATH, 8],
          [NO_PATH, 0, 5, NO_PATH],
          [NO_PATH, NO_PATH, 0, 2],
          [NO_PATH, NO_PATH, NO_PATH, 0]]
```

The output needs to be:

```
[[0, 7, 12, 8],
[9223372036854775807, 0, 5, 7],
[9223372036854775807, 9223372036854775807, 0, 2],
[9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]
```

The samples available on the PDF and the [Geeksforgeeks](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/) are in the sample file.

```
python3 samply.py
```


## Unit and Performance tests

Different test cases can be founded in the following file:
- test_cases.py

**Unit tests** are checking with the test cases will have the same output from the function described on the PDF of the assignment.


To run the **unit tests** is necessary to run the following command:

```
python3 test_unittest.py
```

To run the **performance tests** is necessary to run the following command:

```
python3 test_performance.py
```

## Dependencies

- cProfile
- unittest
- sys
- itertools