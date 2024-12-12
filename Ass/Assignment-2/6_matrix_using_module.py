def initialize_matrix(rows, cols, initial_value=0):
 
    return [[initial_value for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):    
    if not matrix:
        print("Matrix is empty.")
        return
    rows = len(matrix)
    cols = len(matrix[0])
    
    for row in matrix:
        print(" ".join(f"{elem:5}" for elem in row))
    print()

def add_matrices(matrix1, matrix2):
   
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if (rows1, cols1) != (rows2, cols2):
        raise ValueError("Matrices must have the same dimensions for addition.")
    
    return [[matrix1[i][j] + matrix2[i][j] for j in range(cols1)] for i in range(rows1)]

def multiply_matrices(matrix1, matrix2):
   
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    if cols1 != rows2:
        raise ValueError("Number of columns in matrix1 must be equal to the number of rows in matrix2 for multiplication.")

    result = initialize_matrix(rows1, cols2)

    for i in range(rows1):
        for j in range(cols2):
            result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1))
    
    return result

if __name__ == "__main__":

    A = initialize_matrix(1, 3, 2)
    B = initialize_matrix(2, 3, 2)
    C = initialize_matrix(3, 2, 1)
    D = initialize_matrix(3, 2, 3)

    print("Matrix 1:")
    print_matrix(A)
    print("Matrix 1:")
    print_matrix(B)

    try:
        E = add_matrices(A, B)
        print("Matrix 1 + 2:")
        print_matrix(E)
    except ValueError as e:
        print(e)
    
    print("Matrix 3:")
    print_matrix(C)
    print("Matrix 4:")
    print_matrix(D)

    try:
        F = multiply_matrices(C, D)
        print("Matrix 3 * 4:")
        print_matrix(F)
    except ValueError as e:
        print(e)
