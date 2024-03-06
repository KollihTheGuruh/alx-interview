# 0x09. Island Perimeter

## Introduction

This project is part of the curriculum of Holberton School. It challenges students to apply their knowledge of algorithms, Python programming, and specifically working with 2D arrays (matrices) to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid.

**By:** Alexa Orrico, Software Engineer at Holberton School

**Weight:** 1

**Project start:** Mar 3, 2024 10:00 PM

**Deadline:** Mar 7, 2024 10:00 PM

**Checker release:** Mar 4, 2024 10:00 PM

An auto review will be launched at the deadline.

## Objectives

For the "0. Island Perimeter" task, you will need to:

- Navigate and analyze 2D arrays.
- Apply logical operations to determine conditions for perimeter calculation.
- Develop a method to count the edges contributing to the island's perimeter.

## Concepts Needed

- **2D Arrays (Matrices):** Accessing, iterating over elements, and navigating through adjacent cells.
- **Conditional Logic:** Applying conditions to determine cell contributions to the perimeter.
- **Counting Techniques:** Counting edges contributing to the perimeter.
- **Problem-Solving Strategies:** Breaking down the problem and calculating perimeter contributions.
- **Python Programming:** Utilizing nested loops and conditional statements.

## Resources

- Python Official Documentation (Nested Lists)
- GeeksforGeeks: Python Multi-dimensional Arrays
- TutorialsPoint: Python Lists
- YouTube Tutorials on Python 2D arrays and lists

## Additional Resources

- Mock Technical Interviews

## Requirements

- Allowed editors: vi, vim, emacs
- Your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the PEP 8 style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

## Tasks

### 0. Island Perimeter

**File:** `0-island_perimeter.py`

**Description:** Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers where 0 represents water and 1 represents land.
- Each cell is square, with a side length of 1.
- Cells are connected horizontally/vertically (not diagonally).
- `grid` is rectangular, width and height not exceeding 100.
- The grid is completely surrounded by water, contains one island or nothing, and doesn’t have "lakes".
- The function should return the perimeter of the island.

**Example Usage:**

```python
guillaume@ubuntu:~/0x09$ ./0-main.py
12
