# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат
# на 10% относительно предыдущего. Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.

a = int(input('Please enter the current distance value '))
b = int(input('Please enter the distance you would like to run '))
ad = 1  # ad = amount of the days
while a < b:
    a = 1.1 * a
    ad += 1
print(f'If you increase your distance by 10% you will be able to run2 {b} km in {ad} days')