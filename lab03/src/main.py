import random
import time



ASC = False
DESC = True



def deepcopy(src):
    return [elem for elem in src]


def insertion_sort(array):
    for j in range(1, len(array)):
        i = j - 1
        value = array[j]

        while (i >= 0) and (array[i] > value):
            array[i + 1] = array[i]
            i -= 1
        
        array[i + 1] = value


def bubble_sort(array):
    length = len(array)

    for i in range(length - 1):
        for j in range(i + 1, length):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp 


def qsort(array, first, last):
    if first < last:
        f = first
        l = last
        base = array[(first + last) // 2]

        while f <= l:
            elem_f = array[f]
            while (elem_f < base) and (f <= last):
                f += 1
                elem_f = array[f]
            
            elem_l = array[l]
            while (elem_l > base) and (l >= first):
                l -= 1
                elem_l = array[l]
            
            if f <= l:
                temp = array[f]
                array[f] = array[l]
                array[l] = temp
                f += 1
                l -= 1
        qsort(array, first, l)
        qsort(array, f, last)



def get_length():
    correct = False
    while not correct:
        try:
            size = int(input("Введите количество элементов массива: "))
            correct = True
        except:
            print("Ошибка! Недопустимый ввод, попробуйте снова\n")
    return size


def change_limits():
    print("Введите новый диапазон, в котором должны лежать сгенерированные элементы массивов (два числа типа 'int'):")
    correct = False
    while not correct:
        try:
            mini, maxi = list(map(int, input().split()))
            correct = True
        except:
            print("Ошибка! Недопустимый ввод, попробуйте снова\n")
    return (mini, maxi)


# def get_type():
#     types = [int, float, str]
#     correct = False
#     print("Выберете тип элементов массива (1 - int, 2 - float, 3 - str):")
#     while not correct:
#         try:
#             target_type = types[int(input()) + 1]
#             correct = True
#         except:
#             print("Ошибка! Недопустимый ввод, попробуйте снова\n")
#     return target_type


def usr_array(length):        
    print("Введите элементы массива (типа 'int') и нажмите 'Enter':")
    correct = False
    while not correct:
        try:
            array = int(input().split())
            correct = True
        except:
            print("Ошибка! Недопустимый ввод, попробуйте снова\n")
    return array


def random_array(length, *limits):
    print(f"Генерируется массив...\n\tКоличество элементов: {length}, тип элементов: 'int'")
    array = [random.randint(limits[0], limits[1]) for _ in range(length)]
    return array


def ordered_array(length, *limits, key=ASC):
    print(f"Генерируется массив...\n\tКоличество элементов: {length}, тип элементов: 'int'")
    array = [random.randint(limits[0], limits[1]) for _ in range(length)]
    array.sort(reverse=key)
    print(array)
    return array


def print_array(array, copied):
    print(f"Длина массива: {len(array)}\n\tИсходный массив:\t{array}\n\tОтсортированный массив:\t{copied}")


def testing_desc():
    times_insert = []
    times_bubble = []
    times_qsort = []

    epoch = 100

    print("\nТестирование алгоритмов сортировки\nПожалуйста, подождите...\n")    
    for dime in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
        array = sorted([random.randint(0, 1000) for _ in range(dime)], reverse=True)
        print(dime)

        start = time.perf_counter()
        for _ in range(epoch):
            insertion_sort(array)
        times_insert.append((dime, (time.perf_counter() - start) / epoch))

        start = time.perf_counter()
        for _ in range(epoch):
            bubble_sort(array)
        times_bubble.append((dime, (time.perf_counter() - start) / epoch))

        start = time.perf_counter()
        for _ in range(epoch):
            qsort(array, 0, len(array) - 1)
        times_qsort.append((dime, (time.perf_counter() - start) / epoch))



    print(f"Результаты тестирования отсортированных ПО УБЫВАНИЮ массивов (100 итераций, в секундах):")

    print("* Сортировка вставками:\t", end='')
    for i in range(len(times_insert)):
        print("{:.8f}".format(times_insert[i][1]), end='   ')
    print()

    print("* Сортировка пузырьком:\t", end='')
    for i in range(len(times_bubble)):
        print("{:.8f}".format(times_bubble[i][1]), end='   ')
    print()

    print("* Быстрая сортировка:\t", end='')
    for i in range(len(times_qsort)):
        print("{:.8f}".format(times_qsort[i][1]), end='   ')
    print()


def testing_asc():
    times_insert = []
    times_bubble = []
    times_qsort = []

    epoch = 100

    print("\nТестирование алгоритмов сортировки\nПожалуйста, подождите...\n")    
    for dime in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
        array = sorted([random.randint(0, 1000) for _ in range(dime)])
        print(dime)

        # if dime >= 100: 
        #     epoch = 1

        start = time.perf_counter()
        for _ in range(epoch):
            insertion_sort(array)
        times_insert.append((dime, (time.perf_counter() - start) / epoch))

        start = time.perf_counter()
        for _ in range(epoch):
            bubble_sort(array)
        times_bubble.append((dime, (time.perf_counter() - start) / epoch))

        start = time.perf_counter()
        for _ in range(epoch):
            qsort(array, 0, len(array) - 1)
        times_qsort.append((dime, (time.perf_counter() - start) / epoch))



    print(f"Результаты тестирования отсортированных ПО ВОЗРАСТАНИЮ массивов (100 итераций, в секундах):")

    print("* Сортировка вставками:\t", end='')
    for i in range(len(times_insert)):
        print("{:.8f}".format(times_insert[i][1]), end='   ')
    print()

    print("* Сортировка пузырьком:\t", end='')
    for i in range(len(times_bubble)):
        print("{:.8f}".format(times_bubble[i][1]), end='   ')
    print()

    print("* Быстрая сортировка:\t", end='')
    for i in range(len(times_qsort)):
        print("{:.8f}".format(times_qsort[i][1]), end='   ')
    print()


def testing_rnd():
    times_insert = []
    times_bubble = []
    times_qsort = []

    epoch = 100

    print("\nТестирование алгоритмов сортировки\nПожалуйста, подождите...\n")    
    for dime in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
        array = [random.randint(0, 1000) for _ in range(dime)]
        print(dime)

        # if dime >= 1000: 
        #     epoch = 1

        start = time.perf_counter()
        for _ in range(epoch):
            insertion_sort(array)
        times_insert.append((dime, (time.perf_counter() - start) / epoch))

        start = time.perf_counter()
        for _ in range(epoch):
            bubble_sort(array)
        times_bubble.append((dime, (time.perf_counter() - start) / epoch))

        start = time.perf_counter()
        for _ in range(epoch):
            qsort(array, 0, len(array) - 1)
        times_qsort.append((dime, (time.perf_counter() - start) / epoch))



    print(f"Результаты тестирования СЛУЧАЙНЫХ массивов (100 итераций, в секундах):")

    print("* Сортировка вставками:\t", end='')
    for i in range(len(times_insert)):
        print("{:.8f}".format(times_insert[i][1]), end='   ')
    print()

    print("* Сортировка пузырьком:\t", end='')
    for i in range(len(times_bubble)):
        print("{:.8f}".format(times_bubble[i][1]), end='   ')
    print()

    print("* Быстрая сортировка:\t", end='')
    for i in range(len(times_qsort)):
        print("{:.8f}".format(times_qsort[i][1]), end='   ')
    print()


def welcome():
    print("#########################")
    print("#### Лабораторная №3 ####")
    print("###### Сортировки #######")
    print("#########################\n\n")


def print_menu(*limits):
    print("Меню программы:")
    print("\t1. Ручной ввод массива")
    print("\t2. Сгенерировать случайный массив")
    print("\t3. Сгенерировать упорядоченный ПО ВОЗРАСТАНИЮ массив")
    print("\t4. Сгенерировать упорядоченный ПО УБЫВАНИЮ массив")
    print("\t5. Вывести массив")
    print("\t6. Сортировка вставками")
    print("\t7. Сортировка пызурьком")
    print("\t8. Сортировка Хоара ('быстрая')")
    print(f"\t9. Изменить пределы генерации массивов (текущие пределы [{limits[0]}; {limits[1]}])")
    print("\t0. Выход из программы")


def main():
    welcome()

    array = None
    copied = None
    minimum = 0
    maximum = 1000

    menu_key = '-1'
    while menu_key != '0':
        print_menu(minimum, maximum)
        menu_key = input("Введите ключ меню: ")

        if menu_key == '1':
            length = get_length()
            array = usr_array(length)
            copied = deepcopy(array)
        elif menu_key == '2':
            length = get_length()
            array = random_array(length, minimum, maximum)
            copied = deepcopy(array)
        elif menu_key == '3':
            length = get_length()
            array = ordered_array(length, minimum, maximum, key=ASC)
            copied = deepcopy(array)
        elif menu_key == '4':
            length = get_length()
            array = ordered_array(length, minimum, maximum, key=DESC)
            copied = deepcopy(array)
        elif menu_key == '5':
            print_array(array, copied)
        elif menu_key == '6':
            start = time.perf_counter()
            insertion_sort(copied)
            print(f"Время сортировки: {time.perf_counter() - start} секунд\n\n")
        elif menu_key == '7':
            start = time.perf_counter()
            bubble_sort(copied)
            print(f"Время сортировки: {time.perf_counter() - start} секунд\n\n")
        elif menu_key == '8':
            start = time.perf_counter()
            qsort(copied, 0, len(copied) - 1)
            print(f"Время сортировки: {time.perf_counter() - start} секунд\n\n")
        elif menu_key == '9':
            minimum, maximum = change_limits()
        elif menu_key == 'kek':
            testing_asc()
            testing_desc()
            testing_rnd()
        elif menu_key == '0':
            print("\nВсего доброго!\nНе болейте...\n")
        else:
            print("\nНеизвестный ключ\nПопробуйте снова!\n")


if __name__ == "__main__":
    main()

