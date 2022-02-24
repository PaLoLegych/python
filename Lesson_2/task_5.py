# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

num = int(input('Please enter a number: '))
my_list = [8, 8, 7, 5, 3, 3, 2]
value = my_list.count(num)
for el in my_list:
    if value > 0:
        i = my_list.index(num)
        my_list.insert(i + 1, num)
    # break
    else:
        if num > el:
            j = my_list.index(el)
            my_list.insert(j, num)
            # break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)

    exit = input('Is the value inout complete? (Y/N) ')
    if exit == 'y' or exit == 'Y':
        break
    else:
        if exit == 'n' or exit == 'N':
            num = int(input('Please enter a number: '))

print(my_list)
