s is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
    matrix (list): A list of lists of integers or floats.
    div (int/float): The number by which to divide the matrix elements.

    Returns:
    list: A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats, 
               if each row of the matrix does not have the same size,
               or if div is not a number.
    ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(el / div, 2) for el in row] for row in matrix]

# Example Usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    # Output: [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

