# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

my_str = input('Please enter some text with spaces between words: ')
value = my_str.split()
for i, el in enumerate(value):
    if len(el) > 10:
        el = el[0:10:1]
    print(i, el)

