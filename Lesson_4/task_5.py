# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def mfunc(i_prev, i):
    return i_prev * i

print(f'Multiplication result: {reduce(mfunc, [i for i in range (99,1001) if i%2==0])}')

