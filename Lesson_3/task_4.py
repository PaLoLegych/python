# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    return x ** y


print(f"{my_func(int(input('Please enter a valid positive number (X): ')), int(input('Enter a negative integer (Y): ')))}")
