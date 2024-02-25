# 0. Rotate 2D Matrix

In this project, we delve into the world of matrix manipulation by implementing an algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise, in-place. This task not only enhances our understanding of matrices in Python but also challenges us to optimize space complexity through in-place operations.

## Concepts

To successfully complete this project, you need to be familiar with the following concepts:

1. **Matrix Representation in Python:**
   - Understanding how 2D matrices are represented using lists of lists.
   - Accessing and modifying elements in a 2D matrix.

2. **In-place Operations:**
   - Performing operations on data without creating a copy.
   - Importance of minimizing space complexity.

3. **Matrix Transposition:**
   - Concept of transposing a matrix (swapping rows and columns).
   - Implementing transposition in the rotation process.

4. **Reversing Rows in a Matrix:**
   - Manipulating matrix rows by reversing their order.

5. **Nested Loops:**
   - Utilizing nested loops for iterating through 2D structures.
   - Modifying elements within these loops for rotation.

## Resources

To aid in understanding and implementation, here are some valuable resources:

- Python Official Documentation:
  - [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
  - [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
  
- GeeksforGeeks Articles:
  - [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
  - [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

- TutorialsPoint:
  - [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

## Additional Resources

- Mock Technical Interview

## Requirements

- **General:**
  - Allowed editors: vi, vim, emacs.
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10).
  - All files should end with a new line.
  - The first line of all your files should be exactly `#!/usr/bin/python3`.
  - A `README.md` file, at the root of the folder of the project, is mandatory.
  - Your code should use the pycodestyle style (version 2.8.0).
  - You are not allowed to import any module.
  - All modules and functions must be documented.
  - All your files must be executable.

## Tasks

### 0. Rotate 2D Matrix


Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.

- **Prototype:** `def rotate_2d_matrix(matrix):`
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

**Example Usage:**

```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
