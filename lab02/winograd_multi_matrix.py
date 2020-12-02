from classic_mult_matrix import classic_mult
import exceptions as exc
from vectors import Array, Matrix

def winograd_multi(G, H):
    a, h = G.len_matrix
    b, c = H.len_matrix

    if b != h:
        raise exc.MatrixEqException("Колличество столбцов 1ой матрицы не совпадает с количеством строк в 2ой")
    
    d = b // 2
    row_factor = [0 for i in range(a)]
    col_factor = [0 for i in range(c)]

    # Row Factor calc
    for i in range(a):
        for j in range(d):
            row_factor[i] += G[i][2 * j] * G[i][2 * j + 1]

    for i in range(c):
        for j in range(d):
            col_factor[i] += H[2 * j][i] * H[2 * j + 1][i]

    answer = Matrix.from_list([[0 for i in range(c)] for j in range(a)])
    for i in range(a):
        for j in range(c):
            answer[i][j] = - row_factor[i] - col_factor[j]
            for k in range(d):
                answer[i][j] += ((G[i][2 * k] + H[2 * k + 1][j]) * (G[i][2 * k + 1] + H[2 * k][j]))

    if b % 2:
        for i in range(a):
            for j in range(c):
                answer[i][j] += G[i][b - 1] * H[b - 1][j]

    return answer


def imprv_winograd_multi(G, H):
    a, h = G.len_matrix
    b, c = H.len_matrix

    if b != h:
        raise exc.MatrixEqException("Колличество столбцов 1ой матрицы не совпадает с количеством строк в 2ой")

    d = b // 2

    row_factor = Array(a)
    col_factor = Array(c)

    # Row Factor calc
    for i in range(a):
        row_factor[i] = sum(G[i][2 * j] * G[i][2 * j + 1] for j in range(d))

    # Col Factor calc
    for i in range(c):
        col_factor[i] = sum(H[2 * j][i] * H[2 * j + 1][i] for j in range(d))

    answer = Matrix.from_list([[0 for i in range(c)] for j in range(a)])
    for i in range(a):
        for j in range(c):
            answer[i][j] = sum((G[i][2 * k] + H[2 * k + 1][j]) * (G[i][2 * k + 1] + H[2 * k][j]) for k in range(d))\
                           - row_factor[i] - col_factor[j]

    if b % 2:
        for i in range(a):
            answer[i][j] = sum(G[i][b - 1] * H[b - 1][j] for j in range(c))

    return answer

if __name__ == "__main__":
    A = Matrix.from_list([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
    B = Matrix.from_list([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]])
    print(imprv_winograd_multi(A, B))
    print(classic_mult(A, B))