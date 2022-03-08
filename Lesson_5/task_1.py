# Создать программный файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('text.txt', 'w', encoding='utf-8') as f:
    while True:
        mstr = input('Please enter any text: ')
        if not mstr:
            break
        print(mstr, file=f)
