class Array:
    def __init__(self, count):
        self.__array = [0 for _ in range(count)]
        self.__iter_counter = 0

    @classmethod
    def from_list(cls, data_list):
        data = cls(len(data_list))
        for i in range(len(data_list)):
            data.__array[i] = data_list[i]
        return data

    def __str__(self):
        return str(self.__array)

    def __len__(self):
        return len(self.__array)

    def __getitem__(self, index):
        return self.__array[index]

    def __setitem__(self, index, value):
        self.__array[index] = value

    def __iter__(self):
        self.__iter_counter = 0
        return self

    def __next__(self):
        try:
            self.__iter_counter += 1
            return self.__array[self.__iter_counter - 1]
        except IndexError:
            raise StopIteration
    
    def __eq__(self, other):
        return self.__array == other.__array

    def __ne__(self, other):
        return self.__array != other.__array


class Matrix:
    def __init__(self, rows_count, columns_count):
        self.__iter_counter = 0
        self.__rows_count = rows_count
        self.__columns_count = columns_count
        self.__matrix = [[0 for _ in range(columns_count)] for _ in range(rows_count)]
    
    @classmethod
    def from_list(cls, data_list):
        rows_count, columns_count = len(data_list), len(data_list[0])
        data = cls(rows_count, columns_count)
        for i in range(rows_count):
            for j in range(columns_count):
                data.__matrix[i][j] = data_list[i][j]
        return data
    
    def __str__(self):
        data = "\n"
        for line in self.__matrix:
            data += str(line)
            data += "\n"
        return data

    @property
    def len_matrix(self):
        return (self.__rows_count, self.__columns_count)

    def __getitem__(self, index):
        return self.__matrix[index]

    def __iter__(self):
        self.__iter_counter = 0
        return self

    def __next__(self):
        try:
            self.__iter_counter += 1
            return self.__matrix[self.__iter_counter - 1]
        except IndexError:
            raise StopIteration

    def __eq__(self, other):
        return self.__matrix == other.__matrix

    def __ne__(self, other):
        return self.__matrix != other.__matrix