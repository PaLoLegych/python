# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую
# построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

# from googletrans import Translator
#
# with open('text_4.txt', 'r', encoding='utf-8') as f:
#     if f.mode == 'r':
#         content = f.read()
#         print(content)
#
#     translator = Translator()
#     result = translator.translate(content, dest='ru')
#     print(result.text)

mdict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

new_list = []
with open('text_4.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        new_list.append(mdict[i[0]] + ' ' + i[1])
    print(new_list)

with open('text_4_1.txt', 'w') as f_new:
    f_new.writelines(new_list)

# mdict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
#
# new_list = []
# with open('text_4.txt', 'r', encoding='utf-8') as f:
#     with open('text_4_1.txt', 'w', encoding='utf-8') as f2:
#         for line in f:
#             el, *num = line.split()
#             ru = mdict[el]
#             f2.write(' '.join([ru] + num) + '\n')
