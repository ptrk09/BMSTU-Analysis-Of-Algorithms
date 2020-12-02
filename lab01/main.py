import string
import random
from time import time

OUTPUT_DEFINE = False



def outputTable(table, str1, str2):
    print("\n   ", end=" ")
    for i in str2:
        print(i, end=" ")
 
    for i in range(len(table)):
        if i:
            print("\n" + str1[i - 1], end=" ")
        else:
            print("\n ", end=" ")
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
    print("\n")


def RandomString(strLength=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(strLength))


def levenshtein(s1, s2):
    matrix = [[i + j if not(i * j) else 0 for j in range(len(s2) + 1) ] for i in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
                continue
            matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1

    if OUTPUT_DEFINE:
        outputTable(matrix, s1, s2)
    
    return matrix[len(s1)][len(s2)]


def damerauLevenshtein(s1, s2):
    matrix = [[i + j if not(i * j) else 0 for j in range(len(s2) + 1) ] for i in range(len(s1) + 1)]
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            cost =  0 if s1[i - 1] == s2[j - 1] else 1
            matrix[i][j] = min( matrix[i][j - 1] + 1, matrix[i - 1][j] + 1, matrix[i - 1][j - 1] + cost)
            
            if (i > 1 and j > 1
            and s1[i - 1] == s2[j - 2]
            and s1[i - 2] == s2[j - 1]):
                matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + 1)

    if OUTPUT_DEFINE:
        outputTable(matrix, s1, s2)
    
    return matrix[len(s1)][len(s2)]


def recursiveLevenshtein(s1, s2):
    if not(len(s1)) or not(len(s2)):
        return abs(len(s1) - len(s2))
    
    cost = 0 if s1[-1] == s2[-1] else 1
    return min(
            recursiveLevenshtein(s1, s2[:-1]) + 1,
            recursiveLevenshtein(s1[:-1], s2) + 1,
            recursiveLevenshtein(s1[:-1], s2[:-1]) + cost
        )


def matrixRecursiveLevenshtein(s1, s2, matrix):
    if matrix[len(s1)][len(s2)] != -1:
        return matrix[len(s1)][len(s2)]
    if not(len(s1)) or not(len(s2)):
        matrix[len(s1)][len(s2)] = abs(len(s1) - len(s2))
        return matrix[len(s1)][len(s2)]

    cost = 0 if s1[-1] == s2[-1] else 1
    matrix[len(s1)][len(s2)] = min(
        matrixRecursiveLevenshtein(s1, s2[:-1], matrix) + 1,
        matrixRecursiveLevenshtein(s1[:-1], s2, matrix) + 1,
        matrixRecursiveLevenshtein(s1[:-1], s2[:-1], matrix) + cost
    )

    return matrix[len(s1)][len(s2)]


def getStr():
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    return str1, str2


def getStrAndRun(function,flag=False):
    str1, str2 = getStr()
    matrix = [[-1 for _ in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    if not flag:
        res = function(str1, str2)
    else:
        res = function(str1, str2, matrix)
        outputTable(matrix, str1, str2)
    print("Результат == ", res)
        

def timeAnalysis1(function, nIter, strLen=5):
    t1 = time()
    for i in range(nIter):
        str1 = RandomString(strLen)
        str2 = RandomString(strLen)
        function(str1, str2)
    t2 = time()
    return (t2 - t1) / nIter


def timeAnalysis2(function, nIter, strLen=5, matrix=None):
    t1 = time()
    for i in range(nIter):
        matrix = [[-1 for _ in range(strLen + 1)] for i in range(strLen + 1)]
        str1 = RandomString(strLen)
        str2 = RandomString(strLen)
        function(str1, str2, matrix)
    t2 = time()
    return (t2 - t1) / nIter


def testFunctions():
    nIter = int(input("Введите кол-во итераций: "))
    strLen = int(input("Введите длину строки: "))
    print("Strlen: ", strLen)
    print(" Левенштейна рекурсивно            : ", "{:f}".format(timeAnalysis1(recursiveLevenshtein, nIter, strLen)))
    print(" Левенштейна рекурсивно с матрицей : ", "{:f}".format(timeAnalysis2(matrixRecursiveLevenshtein, nIter, strLen)))
    print(" Левенштейна матрично              : ", "{:f}".format(timeAnalysis1(levenshtein, nIter, strLen)))
    print(" Дамерау - Левенштейн              : ", "{:f}".format(timeAnalysis1(damerauLevenshtein, nIter, strLen)))


def printMenu():
    case = input("\n\n1 - Нахождение расстояния Левенштейна рекурсивно с матрицей\n" +
                 "2 - Нахождение расстояния Левенштейна рекурсивно\n" +
                 "3 - Нахождение расстояния Левенштейна матрично\n" +
                 "4 - Нахождение расстояния Дамерау - Левенштейна\n" +
                 "5 - Сравнение алгоритмов\n" +
                 "0 - Выход\n")
    return case



def mainLoop():
    global OUTPUT_DEFINE
    while True:
        case = int(printMenu())
        if case < 5: 
            OUTPUT_DEFINE = True 
        else:
            OUTPUT_DEFINE = False

        if case == 1:
            getStrAndRun(matrixRecursiveLevenshtein, True)
        elif case == 2:
            getStrAndRun(recursiveLevenshtein)
        elif case == 3:
            getStrAndRun(levenshtein)
        elif case == 4:
            getStrAndRun(damerauLevenshtein)
        elif case == 5:
            testFunctions()
        elif case == 0:
            break
        else:
            print("Неизвестная команда")


mainLoop()