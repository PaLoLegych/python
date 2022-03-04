# Реализовать два небольших скрипта: итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо предусмотреть условие,
# при котором повторение элементов списка прекратится.

from itertools import count, cycle


def count_func(start_num, stop_num):
    for i in count(start_num):
        if i > stop_num:
            break
        else:
            print(i)


def cycle_func(mlist, output):
    i = 0
    output_num = cycle(mlist)
    while i < output:
        print(next(output_num))
        i += 1


count_func(start_num=int(input('Please enter start value: ')),
           stop_num=int(input('Please enter stop value: ')))
cycle_func(mlist=[4, 10, 44, 7, 23, 99, 152, 3.14, 6.022, True, 'ABC', 'abc'],
           output=int(input('Please enter the number of parameters to display: ')))
