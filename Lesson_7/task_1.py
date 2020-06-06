# class Matrix:
#
#     def mtrx_dimension(self, mtrx1, mtrx2):
#         row_count = len(mtrx1) if len(mtrx1) > len(mtrx2) else len(mtrx2)
#         max_len = 0
#         for row in mtrx1:
#             max_len = len(row) if len(row) > max_len else max_len
#         for row in mtrx2:
#             max_len = len(row) if len(row) > max_len else max_len
#         return (row_count, max_len)
#
#     def __init__(self, list_of_lists):
#         self.data = list_of_lists
#
#     def __str__(self):
#         view = ''
#         for row in self.data:
#             for el in row:
#                 view += f'{el} '
#             view += '\n'
#         return view
#
#     def get_el(self, mtrx, i, j):
#         try:
#             result = mtrx[i][j]
#         except:
#             result = 0
#         return result
#
#     def __add__(self, other):
#         new_data = []
#         dim  = self.mtrx_dimension(self.data, other.data)
#         for i in range(dim[0]):
#             new_row = []
#             for j in range(dim[1]):
#                 new_row.append(self.get_el(self.data, i, j) + self.get_el(other.data, i, j))
#             new_data.append(new_row)
#
#         new_matrix = Matrix(new_data)
#         return new_matrix
#
#
#
# my_matrix = Matrix([[1,1,1],[1,1,1],[1,1,1]])
# my_matrix_2 = Matrix([[2,2,2],[3,3,3],[4,4,4],[5,5,5,5]])
#
# my_matrix_3 = my_matrix + my_matrix_2
#
# print(my_matrix)
# print(my_matrix_2)
#
# print(my_matrix_3)

#Решение преподавателя

from copy import deepcopy

class Matrix:
    def __init__(self, data:list):
        self.__data = deepcopy(data)
        self.__shape = (len(max(self.__data, key=len)), len(self.__data))
        if len(min(self.__data, key=len)) != self.__shape[0]:
            self.__reshape()

    @property
    def shape(self):
        return self.__shape

    def __reshape(self):
        for itm in self.__data:
            tmp = self.__shape[0] - len(itm)
            if tmp:
                itm.extend([0 for _ in range(tmp)])

    def __getitem__(self, item):
        return self.__data[item]

    def __iter__(self):
        return self.__data.__iter__()

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'This is not Matrix this is {type(other).__name__}')
        if self.shape != other.shape:
            raise ValueError(f'Not equal shape matrix {self.shape} and {other.shape}')

        return Matrix(list(map(lambda y: list(map(sum, y)),
                               map(lambda x: list(zip(*x)), zip(self, other))
                               )
                           )
                      )

    def __str__(self):
        max_len_itm = len(str(max(map(lambda item: max(item, key=lambda x: len(str(x))), self.__data))))
        if not max_len_itm & 1:
            max_len_itm += 1

        result = ''
        for line in self.__data:
            result += ''.join([f'{itm:<{max_len_itm}}' for itm in line]) + '\n' # выравнивание по левому краю. каждый элемент приводится к ширине самого длинного
        return result

a = Matrix([[1,2], [4,5], [3,9,12]])
print(a)

