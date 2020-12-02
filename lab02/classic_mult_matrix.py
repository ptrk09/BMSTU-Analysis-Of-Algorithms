import exceptions as exc
from vectors import Array, Matrix

def classic_mult(A, B):
    n, m = A.len_matrix
    k, t = B.len_matrix
    if k != m:
        raise exc.MatrixEqException("Колличество столбцов 1ой матрицы не совпадает с количеством строк в 2ой")

    data = Matrix(n, t)
    for i in range(n):
        for j in range(m):
            for k in range(t):
                data[i][k] += A[i][j] * B[j][k]
    return data


def imprv_classic_mult(A, B):
    n, m = A.len_matrix
    k, t = B.len_matrix
    if k != m:
        raise exc.MatrixEqException("Колличество столбцов 1ой матрицы не совпадает с количеством строк в 2ой")
    
    return Matrix.from_list(
        [[sum(x * B[i][col] for i, x in enumerate(row)) for col in range(t)] for row in A]
    )


if __name__ == "__main__":
    A = Matrix.from_list([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
    B = Matrix.from_list([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]])
    print(imprv_classic_mult(A, B))