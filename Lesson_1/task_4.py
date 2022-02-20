# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
val = int(input('Please, enter positive value: '))
max_val = val % 10
num = val
while num > 0:
    dgt = num % 10
    if dgt > max_val:
        max_val = dgt
        if max_val == 9:
            break
    num = num // 10
print(f'The largest digit in {val} is = {max_val}')
