# Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить её на экран.

def msum():
    try:
        with open('file_5.txt', 'w') as f:
            line = input('Please enter numbers via space: ')
            f.writelines(line)
            my_numb = line.split()
            print(sum(map(int, my_numb)))
    except IOError:
        print('I/O Error')
    except ValueError:
        print('Incorrect value. I/O Error')


msum()
