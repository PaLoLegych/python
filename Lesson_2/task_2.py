# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

list_init = int(input('Please, enter the elements number '))
my_list1 = []
i = 0
# el = 0
while i < list_init:
    my_list1.extend(input('Please, enter the element value '))
    i += 1

print(my_list1)

my_list2 = my_list1

for el in range(int(len(my_list2) / 2)):
    my_list2[el + 1], my_list2[el] = my_list2[el], my_list2[el + 1]
    el += 2
print(my_list2)
