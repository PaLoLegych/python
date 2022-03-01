# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def msum():
    sumres = 0
    exit = False
    while exit == False:
        num = input("Please enter a value or a special symbol '!' to exit: ").split()

        res = 0
        for i in range(len(num)):
            if num[i] == '!':
                exit = True
                break
            else:
                res = res + int(num[i])
        sumres = sumres + res
        print(f'Intermediate sum value is {sumres}')
    print(f'Final value of sum {sumres}')


msum()
