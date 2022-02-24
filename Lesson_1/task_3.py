# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = int(input('Please, enter a random value = '))
x = str(n)
nn = x + x
nnn = x + x + x
cal = n + int(nn) + int(nnn)
print('Based on your value: %d ' % n + 'the result of the calculation is = %d' % cal)
