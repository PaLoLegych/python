# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица. Подсказка: сложение элементов матриц
# выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:

    def __init__(self, my_matrix_1, my_matrix_2):
        self.my_matrix_1 = my_matrix_1
        self.my_matrix_2 = my_matrix_2
        # self.result = result

    def __add__(self):

        result = [[0] * M for i in range(N)]

        # my_matrix_1 = []
        # for i in range(N):
        #     row = input().split()
        #     for i in range(len(row)):
        #         row[i] = int(row[i])
        #     my_matrix_1.append(row)
        #
        # my_matrix_2 = []
        # for i in range(M):
        #     row = input().split()
        #     for i in range(len(row)):
        #         row[i] = int(row[i])
        #     my_matrix_2.append(row)

        for i in range(len(self.my_matrix_1)):

            for j in range(len(self.my_matrix_2[i])):
                result[i][j] = self.my_matrix_1[i][j] + self.my_matrix_2[i][j]

        return '\n'.join('\t'.join(str(j) for j in i) for i in result)

    def __str__(self):
        return '\n'.join('\t'.join(str(j) for j in i) for i in self.result)


N = int(input('N = '))

# first_matrix = Matrix.__add__.my_matrix_1 = []
# print(first_matrix)

M = int(input('M = '))

my_matrix = Matrix([[3, 5, 32],
                    [2, 4, 6],
                    [-1, 64, -8]],
                   [[-8, 64, -1],
                    [6, 4, 2],
                    [32, 5, 3]])

print(my_matrix.__add__())


