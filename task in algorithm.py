import numpy as np
def split_matrix(matrix):
    n = matrix.shape[0]
    split_point = n // 2
    submatrices = []
    for i in range(2):
        for j in range(2):
            submatrix = matrix[i * split_point:(i + 1) * split_point, j * split_point:(j + 1) * split_point]
            submatrices.append(submatrix)
    return submatrices
def strassen_multiply(A, B):
    n = A.shape[0]
    if n == 1:
        return A * B
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)
    P1 = strassen_multiply(A11 + A22, B11 + B22)
    P2 = strassen_multiply(A21 + A22, B11)
    P3 = strassen_multiply(A11, B12 - B22)
    P4 = strassen_multiply(A22, B21 - B11)
    P5 = strassen_multiply(A11 + A12, B22)
    P6 = strassen_multiply(A21 - A11, B11 + B12)
    P7 = strassen_multiply(A12 - A22, B21 + B22)
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6
    result = np.empty((n, n))
    result[:n//2, :n//2] = C11
    result[:n//2, n//2:] = C12
    result[n//2:, :n//2] = C21
    result[n//2:, n//2:] = C22
    return result
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
B = np.array([[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]])
C = strassen_multiply(A, B)
print(C)