# Реализовать функцию my_func(), которая принимает
# три позиционных аргумента и возвращает сумму наибольших
# двух аргументов.

def mfunc(arg_1, arg_2, arg_3):
    #    arg_1 = int(input('Please enter the first value: '))
    #    arg_2 = int(input('Please enter the second value: '))
    #    arg_3 = int(input('Please enter the third value: '))

    if arg_1 >= arg_2 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_3 >= arg_2 and arg_2 >= arg_1:
        return arg_2 + arg_3
    else:
        return arg_1 + arg_3


print(f"result {mfunc(int(input('Please enter the first value: ')), int(input('Please enter the second value: ')), int(input('Please enter the third value: ')))}")
