#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the last row of the triangle
        new_row = [1]  # Start the new row with a 1

        # Compute the values in between the first and last element of the new row
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])

        new_row.append(1)  # End the new row with a 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle




