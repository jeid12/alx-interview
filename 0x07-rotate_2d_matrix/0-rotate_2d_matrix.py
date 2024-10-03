#!/usr/bin/python3
"""
This module provides a function to rotate an n x n 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list): A 2D matrix of n x n size.
    
    Returns:
        None: The matrix is modified in place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

