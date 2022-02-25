# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
Interval = int(input('Please, enter the time interval in seconds: '))
H = Interval // 3600
M = (Interval - H * 3600) // 60
S = Interval - (H * 3600 + M * 60)
input('If your time interval is equal to %d than the current time is: ' % (Interval) + '%02d:%02d:%02d' % (H, M, S))
