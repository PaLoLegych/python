# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_div(*args):
    try:
        arg_1 = int(input('Please enter a number (greater than 0): '))
        arg_2 = int(input('Please enter a divider (not 0): '))
        result = arg_1 / arg_2
    except ValueError:
        return 'Wrong value. Try again. Value should be a digit'
    except ZeroDivisionError:
        return 'Incorrect divider! Divider cannot be 0'

    return result


print(f'result {my_div()}')
