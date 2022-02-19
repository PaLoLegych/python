# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
val = int(input('Please, enter positive value: '))
max_val = val % 10
while val > 0:
    val = val // 10
    if val > max_val:
        max_val = val % 10
        print('The largest digit in %d ' % val + 'is = %d' % max_val)
        break
