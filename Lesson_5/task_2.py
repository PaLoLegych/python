# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

f = open('text.txt', 'r', encoding='utf-8')
print(f.read())

with open('text.txt', 'r', encoding='utf-8') as f:
    lines = 0
    words = 0
    for line in f:
        lines += line.count('\n')
        words += len(line.split())
        print(f'{words} words in each line.')
    print(f'{lines} lines in the text document.')

