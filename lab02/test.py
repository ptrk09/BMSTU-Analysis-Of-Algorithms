# test_python.py
import unittest
from vectors import Matrix
import classic_mult_matrix as std
import winograd_multi_matrix as cast
import time
import random

SIZE = 50
TIMES = 10

def getRandomMatrix(n):
    matrix = Matrix.from_list([[random.randint(0, 10) for _ in range(n)] for _ in range(n)])
    return matrix

class TestPython(unittest.TestCase):
    def setUp(self):
        self.real_resalt = None
        self.need_resalt = None
        self.matrix1 = Matrix.from_list([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
        self.matrix2 = Matrix.from_list([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]])
        self.stop_time = 0
        self.start_time = 0

    def test_classic_mult(self):
        self.need_resalt = Matrix.from_list([[30, 40, 50, 60, 70], [40, 54, 68, 82, 96], [50, 68, 86, 104, 122]])
        self.start_time = time.time()
        self.real_resalt = std.classic_mult(self.matrix1, self.matrix2)
        self.stop_time = time.time()
        self.assertEqual(self.real_resalt, self.need_resalt)
        
    
    def test_imprv_classic_mult(self):
        self.need_resalt = Matrix.from_list([[30, 40, 50, 60, 70], [40, 54, 68, 82, 96], [50, 68, 86, 104, 122]])
        self.start_time = time.time()
        self.real_resalt = std.imprv_classic_mult(self.matrix1, self.matrix2)
        self.stop_time = time.time()
        self.assertEqual(self.real_resalt, self.need_resalt)

    def test_vinograd_mult(self):
        self.need_resalt = Matrix.from_list([[30, 40, 50, 60, 70], [40, 54, 68, 82, 96], [50, 68, 86, 104, 122]])
        self.start_time = time.time()
        self.real_resalt = cast.winograd_multi(self.matrix1, self.matrix2)
        self.stop_time = time.time()
        self.assertEqual(self.real_resalt, self.need_resalt)
        
    
    def test_imprv_vinograd_mult(self):
        self.need_resalt = Matrix.from_list([[30, 40, 50, 60, 70], [40, 54, 68, 82, 96], [50, 68, 86, 104, 122]])
        self.start_time = time.time()
        self.real_resalt = cast.imprv_winograd_multi(self.matrix1, self.matrix2)
        self.stop_time = time.time()
        self.assertEqual(self.real_resalt, self.need_resalt)
        
    
    def tearDown(self):
        print("\nВходные данные:")
        print("Матрица №1:", self.matrix1)
        print("Матрица №2:", self.matrix2)
        print("Ожидаемый результат:", self.need_resalt)
        print("Фактический результат:", self.real_resalt)
        print("Время умножения: {0:.6f} тиков".format(self.stop_time - self.start_time))


class TestPython2(unittest.TestCase):
    def setUp(self):
        self.metod = ""
        self.time = 0
        self.sizeBite = 0

    def test_classic_mult_time(self):
        self.metod = "классическое умножение"
        for _ in range(TIMES):
            self.matrix1 = getRandomMatrix(SIZE)
            self.matrix2 = getRandomMatrix(SIZE)
            t1 = time.time()
            res = std.classic_mult(self.matrix1, self.matrix2)
            t2 = time.time()
            self.time += t2 - t1
        self.sizeBite = self.matrix1.len_matrix[0] * self.matrix1.len_matrix[1] * 4 +\
            self.matrix2.len_matrix[0] * self.matrix2.len_matrix[1] * 4 +\
                self.matrix1.len_matrix[0] * self.matrix2.len_matrix[1] * 4

    def test_impr_classic_mult_time(self):
        self.metod = "улучшенное классическое умножение"
        for _ in range(TIMES):
            self.matrix1 = getRandomMatrix(SIZE)
            self.matrix2 = getRandomMatrix(SIZE)
            t1 = time.time()
            res = std.imprv_classic_mult(self.matrix1, self.matrix2)
            t2 = time.time()
            self.time += t2 - t1
            self.sizeBite = self.matrix1.len_matrix[0] * self.matrix1.len_matrix[1] * 4 +\
            self.matrix2.len_matrix[0] * self.matrix2.len_matrix[1] * 4 +\
                    self.matrix1.len_matrix[0] * self.matrix2.len_matrix[1] * 4

    def test_win_mult_time(self):
        self.metod = "умножение Виноградова"
        for _ in range(TIMES):
            self.matrix1 = getRandomMatrix(SIZE)
            self.matrix2 = getRandomMatrix(SIZE)
            t1 = time.time()
            res = cast.winograd_multi(self.matrix1, self.matrix2)
            t2 = time.time()
            self.time += t2 - t1
        self.sizeBite = self.matrix1.len_matrix[0] * self.matrix1.len_matrix[1] * 4 +\
            self.matrix2.len_matrix[0] * self.matrix2.len_matrix[1] * 4 +\
                self.matrix1.len_matrix[0] * self.matrix2.len_matrix[1] * 4 +\
                   (self.matrix1.len_matrix[0]+ self.matrix2.len_matrix[1]) * 4

    def test_impr_win_mult_time(self):
        self.metod = "улучшенное умножение Виноградова"
        for _ in range(TIMES):
            self.matrix1 = getRandomMatrix(SIZE)
            self.matrix2 = getRandomMatrix(SIZE)
            t1 = time.time()
            res = cast.imprv_winograd_multi(self.matrix1, self.matrix2)
            t2 = time.time()
            self.time += t2 - t1
        self.sizeBite = self.matrix1.len_matrix[0] * self.matrix1.len_matrix[1] * 4 +\
            self.matrix2.len_matrix[0] * self.matrix2.len_matrix[1] * 4 +\
                self.matrix1.len_matrix[0] * self.matrix2.len_matrix[1] * 4 +\
                   (self.matrix1.len_matrix[0]+ self.matrix2.len_matrix[1]) * 4

    def tearDown(self):
        print("\n\nМетод:", self.metod)
        print("Размерность:", SIZE)
        print("Кол-во проведённых умножений:", self.metod)
        print("Среднее время умножения за кол-во проведённых оппераций: {0:.6f} тиков".format(self.time / TIMES))
        print("Замер памяти:", self.sizeBite, "байт")