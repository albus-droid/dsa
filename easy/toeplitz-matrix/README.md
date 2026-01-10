### Toeplitz Matrix
Problem Statement

Given an m x n matrix, determine if a given matrix is a Toeplitz matrix.

A Toeplitz matrix is one in which every diagonal from top-left to bottom-right has the same elements.

In other words, the matrix should have the property that each element is equal to the element diagonally down to its right.

Example 1:

    Input:
```
[[1,2,3],
 [4,1,2],
 [5,4,1]]
```
    Expected Output: true
    Justification: All diagonals have the same elements. Diagonals of the above matrix are [5], [4, 4], [1, 1, 1], [2, 2], and [3].

Example 2:

    Input:
```
[[1,2],
 [3,4]]
```
    Expected Output: false
    Justification: The diagonal are [3], [1, 4], and [2]. A diagonal [1, 4] doesn't have the same elements.

Example 3:

    Input:
```
[[7,7,7],
 [7,7,7],
 [7,7,7]]
```
    Expected Output: true
    Justification: Each diagonal, although containing the same repeated element (7), satisfies the condition of a Toeplitz matrix.
