# Создать текстовый файл (не программно). Построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла: Иванов 23543.12, Петров 13749.32.

with open('text_3.txt', 'r') as f:
    salary = []
    min_sal = []
    mlist = f.read().split('\n')
    for i in mlist:
        i = i.split()
        if float(i[1]) < 20000:
            min_sal.append(i[0])
        salary.append(i[1])
print(f'The salary less than 20000 have: {min_sal}')
print(f'The average salary is: {sum(map(float, salary)) / len(salary)}')
