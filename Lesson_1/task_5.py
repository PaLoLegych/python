# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек,
# или убыток — издержки больше выручки. Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки. Э
# то отношение прибыли к выручке. Далее запросите численность сотрудников
# фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

rev = float(input('Please enter revenue of the company: '))
cos = float(input('Please enter costs of the company: '))
inc = rev - cos
if inc > 0:
    print('The company is profitable.')
    print(f'Return on revenue is:  {inc / rev: .2f}')
    staff = int(input('Please enter the number of employees:'))
    print(f'Profit per employee is: {rev / staff: .2f}')
else:
    print('The company is unprofitable.')
