import random
import time



def check_dimes(a, b):
    return len(a) == len(b[0])


def enter_matrix():
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбоцов матрицы: "))
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    # print(matrix)

    print("Введите поэлементно матрицу:")
    for row in range(rows):
        tmp = input().split()
        for col in range(cols):
            matrix[row][col] = int(tmp[col])
    return matrix


def random_matrix():
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбоцов матрицы: "))
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = random.randint(0, 1000)
    return matrix


def print_matrix(a):
    for i in range(len(a)):
        print('(', end='')
        for j in range(len(a[0])):
            print(f"{a[i][j]}", end='')
            print(' ', end='') if j != len(a[0]) - 1 else None
        print(')')

# def dot_product(first, second):
#     product = 0
#     for elem_a, elem_b in zip(first, second):
#         product += elem_a * elem_b
#     return product


def dot_product(first, second, i, j):
    product = 0
    for idx in range(len(first[0])):
        product += first[i][idx] * second[idx][j]
    return product


def trivial_m12n(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            # tmp = [b[idx][j] for idx in range(len(b))]   # rotate col into row
            result[i][j] = dot_product(a, b, i, j)
    return result


def winograd_m12n(a, b):
    row_factors = []
    col_factors = []
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        value = 0
        for j in range(len(a[0]) // 2):
            value = value + a[i][j * 2] * a[i][j * 2 + 1]
        row_factors.append(value)
    
    for i in range(len(b[0])):
        value = 0
        for j in range(len(b) // 2):
            value = value + b[j * 2][i] * b[j * 2 + 1][i]
        col_factors.append(value)
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            result[i][j] = -row_factors[i] - col_factors[j]

            for idx in range(len(a[0]) // 2):
                result[i][j] = (a[i][2 * idx + 1] + b[2 * idx][j]) * (a[i][2 * idx] + b[2 * idx + 1][j]) + result[i][j]
    
    if len(a) % 2:
        for i in range(len(a)):
            for j in range(len(b[0])):
                result[i][j] = result[i][j] + a[i][len(a[0]) - 1] * b[len(a[0])- 1][j]

    return result


def better_winograd_m12n(a, b):
    row_factors = []
    col_factors = []
    rows_a = len(a); cols_a = len(a[0]); cols_amod = cols_a // 2
    rows_b = len(b); cols_b = len(b[0]); rows_bmod = rows_b // 2
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        value = 0
        for j in range(cols_amod):
            value += a[i][j * 2] * a[i][j * 2 + 1]
        row_factors.append(value)
    
    for i in range(cols_b):
        value = 0
        for j in range(rows_bmod):
            value = value + b[j * 2][i] * b[j * 2 + 1][i]
        col_factors.append(value)
    
    for i in range(rows_a):
        for j in range(cols_b):
            buffer = -row_factors[i] - col_factors[j]
            for idx in range(cols_amod):
                buffer += (a[i][2 * idx + 1] + b[2 * idx][j]) * (a[i][2 * idx] + b[2 * idx + 1][j])
            result[i][j] = buffer
    
    if len(a) % 2:
        for i in range(rows_a):
            for j in range(cols_b):
                result[i][j] += a[i][cols_a - 1] * b[cols_a - 1][j]

    return result


def trivial(matrix_1, matrix_2):
    if not check_dimes(matrix_1, matrix_2):
        print("\nВведенные матрицы невозможно перемножить!\nНеверные размерности\n")
        return

    result = trivial_m12n(matrix_1, matrix_2) 

    print()
    print_matrix(matrix_1)
    print("Умножить на:")
    print_matrix(matrix_2)
    print("Равно:")
    print_matrix(result)
    print('\n')


def winograd(matrix_1, matrix_2):
    if not check_dimes(matrix_1, matrix_2):
        print("\nВведенные матрицы невозможно перемножить!\nНеверные размерности\n")
        return

    result = winograd_m12n(matrix_1, matrix_2) 

    print()
    print_matrix(matrix_1)
    print("Умножить на:")
    print_matrix(matrix_2)
    print("Равно:")
    print_matrix(result)
    print('\n')


def improved_winograd(matrix_1, matrix_2):
    if not check_dimes(matrix_1, matrix_2):
        print("\nВведенные матрицы невозможно перемножить!\nНеверные размерности\n")
        return

    result = better_winograd_m12n(matrix_1, matrix_2) 

    print()
    print_matrix(matrix_1)
    print("Умножить на:")
    print_matrix(matrix_2)
    print("Равно:")
    print_matrix(result)
    print('\n')


def testing():
    times_trivial = []
    times_winograd = []
    times_optimized = []

    epoch = 100

    print("\nТестирование алгоритмов матричного умножения\nПожалуйста, подождите...\n")    
    for dime in [3, 5, 10, 20, 50, 100, 500]:
        matrix_a = [[random.randint(0, 1000) for _ in range(dime)] for _ in range(dime)]
        matrix_b = [[random.randint(0, 1000) for _ in range(dime)] for _ in range(dime)]

        if dime >= 100: 
            epoch = 1

        start = time.perf_counter()
        for _ in range(epoch):
            trivial_m12n(matrix_a, matrix_b)
        times_trivial.append((dime, (time.perf_counter() - start) / epoch))

        start = time.perf_counter()
        for _ in range(epoch):
            winograd_m12n(matrix_a, matrix_b)
        times_winograd.append((dime, (time.perf_counter() - start) / epoch))

        start = time.perf_counter()
        for _ in range(epoch):
            better_winograd_m12n(matrix_a, matrix_b)
        times_optimized.append((dime, (time.perf_counter() - start) / epoch))



    print(f"Результаты тестирования (100 итераций, в секундах):")

    print("* Стандартный алгоритм:\t\t", end='')
    for i in range(len(times_trivial)):
        print("{:.8f}".format(times_trivial[i][1]), end='   ')
    print()

    print("* Алгоритм Винограда:\t\t", end='')
    for i in range(len(times_winograd)):
        print("{:.8f}".format(times_winograd[i][1]), end='   ')
    print()

    print("* Алгоритм Винограда (улучш.):\t", end='')
    for i in range(len(times_optimized)):
        print("{:.8f}".format(times_optimized[i][1]), end='   ')
    print()


def usr_input():
    print("\nМатрица №1")
    matrix_1 = enter_matrix()
    print("\n\nМатрица №2")
    matrix_2 = enter_matrix()
    return (matrix_1, matrix_2)


def random_input():
    print("\nМатрица №1")
    matrix_1 = random_matrix()
    print("\n\nМатрица №2")
    matrix_2 = random_matrix()
    return (matrix_1, matrix_2)


def welcome():
    print("#### Лабораторная №2 ####")
    print("#### Умножение матриц ####")
    print("########## v1.0 ##########\n\n")


def print_menu():
    print("Меню программы:")
    print("\t1. 'Классическое' умножение матриц")
    print("\t2. Умножение матриц с помощью алгоритма Винограда")
    print("\t3. Умножение матриц с помощью оптимизированного алгоритма Винограда")
    print("\t4. Тестирование алгоритмов")
    print("\t5. Ввести матрицы")
    print("\t6. Сгенерировать матрицы")
    print("\t0. Выход из программы")


if __name__ == "__main__":
    welcome()

    matrix_a = [[]]
    matrix_b = [[]]

    menu_key = '-1'
    while menu_key != '0':
        print_menu()
        menu_key = input("Введите ключ меню: ")

        if menu_key == '1':
            trivial(matrix_a, matrix_b)
        elif menu_key == '2':
            winograd(matrix_a, matrix_b)
        elif menu_key == '3':
            improved_winograd(matrix_a, matrix_b)
        elif menu_key == '4':
            testing()
        elif menu_key == '5':
            matrix_a, matrix_b = usr_input()
        elif menu_key == '6':
            matrix_a, matrix_b = random_input()
        elif menu_key == '0':
            print("\nВсего доброго!\nНе болейте...\n")
        else:
            print("\nНеизвестный ключ\nПопробуйте снова!\n")
