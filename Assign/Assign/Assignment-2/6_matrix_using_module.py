

def initialize_matrix(rows, cols, initial_value=0):
    """
    Initialize a matrix with given dimensions and an initial value.
    
    :param rows: Number of rows in the matrix (int)
    :param cols: Number of columns in the matrix (int)
    :param initial_value: Initial value to fill the matrix (default is 0) (int or float)
    :return: A matrix as a list of lists
    """
    return [[initial_value for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    """
    Print the matrix in a readable format.
    
    :param matrix: The matrix to print (list of lists)
    """
    if not matrix:
        print("Matrix is empty.")
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    for row in matrix:
        print(" ".join(f"{elem:5}" for elem in row))
    print()

def add_matrices(matrix1, matrix2):
    """
    Add two matrices.
    
    :param matrix1: The first matrix (list of lists)
    :param matrix2: The second matrix (list of lists)
    :return: The resulting matrix after addition (list of lists)
    :raises ValueError: If the matrices have different dimensions
    """
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if (rows1, cols1) != (rows2, cols2):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    return [[matrix1[i][j] + matrix2[i][j] for j in range(cols1)] for i in range(rows1)]

def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices.
    
    :param matrix1: The first matrix (list of lists)
    :param matrix2: The second matrix (list of lists)
    :return: The resulting matrix after multiplication (list of lists)
    :raises ValueError: If the number of columns in matrix1 is not equal to the number of rows in matrix2
    """
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if cols1 != rows2:
        raise ValueError("Number of columns in matrix1 must be equal to the number of rows in matrix2 for multiplication.")
    
    # Initialize the result matrix with zeros
    result = initialize_matrix(rows1, cols2)
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1))
    
    return result

# Example usage
if __name__ == "__main__":
    # Initialize matrices
    A = initialize_matrix(1, 3, 2)
    B = initialize_matrix(2, 3, 2)
    C = initialize_matrix(3, 2, 1)
    D = initialize_matrix(3, 2, 3)
    
    # Print matrices
    print("Matrix 1:")
    print_matrix(A)
    print("Matrix 1:")
    print_matrix(B)
    
    # Add matrices
    try:
        E = add_matrices(A, B)
        print("Matrix 1 + 2:")
        print_matrix(E)
    except ValueError as e:
        print(e)
    
    # Print matrices for multiplication
    print("Matrix 3:")
    print_matrix(C)
    print("Matrix 4:")
    print_matrix(D)
    
    # Multiply matrices
    try:
        F = multiply_matrices(C, D)
        print("Matrix 3 * 4:")
        print_matrix(F)
    except ValueError as e:
        print(e)
