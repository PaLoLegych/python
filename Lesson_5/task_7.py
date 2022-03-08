# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней
# прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

result = dict()
aver_profit = 0
i = 0

with open('file_7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, type, income, expenses = line.split()
        # print(line)
        profit = int(income) - int(expenses)
        if profit >= 0:
            aver_profit += profit
            i += 1
        result[name] = profit
aver_profit /= i
print(f'Results of the companies: \n'
      f'{result}')
print(f'Average profit is: \n'
      f'{aver_profit}')

with open('file_7.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)
json_str = json.dumps(result)
print(f'The json file has been created with the following content: \n '
      f' {json_str}')
