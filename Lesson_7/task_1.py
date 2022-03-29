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
    def __init__(self, MyMatrix_1, MyMatrix_2, result):
        self.MyMatrix_1 = MyMatrix_1
        self.MyMatrix_2 = MyMatrix_2
        self.result = result

    def __add__(self, MyMatrix_1, MyMatrix_2, result):
        self.result = []
        self.MyMatrix_1 = []
        for i in range(n):
            row = input().split()
            for i in range(len(row)):
                row[i] = int(row[i])
            self.MyMatrix_1.append(row)

            self.MyMatrix_2 = []
            for i in range(m):
                row = input().split()
                for i in range(len(row)):
                    row[i] = int(row[i])
                self.MyMatrix_2.append(row)

            self.result = [[MyMatrix_1[i][j] + MyMatrix_2[i][j] for j in range(len(MyMatrix_1[0]))] for i in
                    range(len(MyMatrix_1))]

    def __str__(self):
        pass
        # result = [[MyMatrix_1[i][j] + MyMatrix_2[i][j] for j in range(len(MyMatrix_1[0]))] for i in range(len(MyMatrix_1))]


result = n = int(input('Enter a number of row for MyMatrix_1: '))
m = int(input('Enter a number of row for MyMatrix_2: '))

print(result.__add__)

# for r in result:
#     print(r)
