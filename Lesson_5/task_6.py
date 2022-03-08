# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий
# по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и
# общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# d = dict()
#
# with open('file_6.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         name, rest = line.split(':')
#         rest = rest.split()
#         num = 0
#         for part in rest:
#             if "-" in part:
#                 continue
#             nums, type = part.split('(')
#             num += int(nums)
#         d[name] = num
# print(d)

subj = {}
with open('file_6.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # print(lines)
for line in lines:
    data = line.replace('(', ' ').split()
    # print(data)
    subj[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
print(subj)
