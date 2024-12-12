class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data:
            self.data = data
        else:
            self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.data:
            result += ' '.join(map(str, row)) + "\n"
        return result

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add.")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def multiply(self, other):
        if self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for element-wise multiplication.")
        
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result

def initialize_matrix(rows, cols, data):
    return Matrix(rows, cols, data)

# Initialize matrices
matrix1 = initialize_matrix(2, 2, [[1, 2], [3, 4]])
matrix2 = initialize_matrix(2, 2, [[5, 6], [7, 8]])

# Print matrices
print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

# Add matrices
result_add = matrix1.add(matrix2)
print("Addition Result:")
print(result_add)

# Multiply matrices
result_multiply = matrix1.multiply(matrix2)
print("Multiplication Result:")
print(result_multiply)
