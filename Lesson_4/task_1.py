# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчёта заработной платы сотрудника. Используйте в нём формулу:
# (выработка в часах*ставка в час) + премия. Во время выполнения расчёта
# для конкретных значений необходимо запускать скрипт с параметрами.

def salary():
    try:
        hours = int(input('Please enter hours worked: '))
        hrate = int(input('Please enter hourly rate: '))
        bonus = int(input('Please enter bonus: '))
        result = (hours * hrate) + bonus
        print(f'Employee salary is: {result}')
    except ValueError:
        return print('Error. You must enter a numeric value!')


salary()
