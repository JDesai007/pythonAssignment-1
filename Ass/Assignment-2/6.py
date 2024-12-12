class Matrix:
    def __init__(self, rows, cols):
       
        self.rows = rows
        self.cols = cols
        self.matrix = []
        print(f"Enter elements for a {rows}x{cols} matrix row by row:")
        for i in range(rows):
            row = list(map(int, input(f"Row {i + 1}: ").split()))
            if len(row) != cols:
                raise ValueError(f"Each row must have exactly {cols} elements.")
            self.matrix.append(row)

    def __str__(self):
       
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def add(self, other):
     
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = Matrix.zeros(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    def multiply(self, other):
    
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")
        result = Matrix.zeros(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.matrix[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols))
        return result

    @staticmethod
    def zeros(rows, cols):
        matrix = Matrix.__new__(Matrix)  # Bypass __init__ for static method
        matrix.rows = rows
        matrix.cols = cols
        matrix.matrix = [[0] * cols for _ in range(rows)]
        return matrix

print("Initialize Matrix 1:")
matrix1 = Matrix(2, 2)

print("\nInitialize Matrix 2:")
matrix2 = Matrix(2, 2)

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

try:
    print("\nMatrix 1 + Matrix 2:")
    result_add = matrix1.add(matrix2)
    print(result_add)
except ValueError as e:
    print(f"Error: {e}")
    
try:
    print("\nMatrix 1 x Matrix 2:")
    result_mul = matrix1.multiply(matrix2)
    print(result_mul)
except ValueError as e:
    print(f"Error: {e}")

