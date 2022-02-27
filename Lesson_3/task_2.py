# Выполнить функцию, которая принимает несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

name = input('Please enter your name: ')
surname = input('Please enter your surname: ')
birthday = int(input('Please enter your birth year: '))
location = input('Please enter your city of residence: ')
email = input('Please enter your email address: ')
phone = int(input('Please enter your phone number: '))


def mfunc(name, surname, birthday, location, email, phone):
    return ' '.join([name, surname, birthday, location, email, phone])


print(mfunc(name=' ', surname=' ', birthday=' ', location=' ', email=' ', phone=' '))
