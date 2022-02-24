# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list_init = input('Please, enter the values separated by spaces: ').split()
print(list_init)
if len(list_init) % 2 == 0:
    i = 0
    while i < len(list_init):
        el = list_init[i]
        list_init[i] = list_init[i + 1]
        list_init[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(list_init) - 1:
        el = list_init[i]
        list_init[i] = list_init[i + 1]
        list_init[i + 1] = el
        i += 2
print(list_init)
