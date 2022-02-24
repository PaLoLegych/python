# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

m_dict = {'1': 'January', '2': 'February', '3': 'March',
          '4': 'April', '5': 'May', '6': 'June',
          '7': 'July', '8': 'August', '9': 'September',
          '10': 'October', '11': 'November', '12': 'December'}
num_m = int(input('Please enter a month number from 1 to 12: '))
a = num_m
if a == 1 or a == 2 or a == 12:
    print("Your choiсe is the Winter season")
elif a == 3 or a == 4 or a == 5:
    print("Your choiсe is the Spring season")
elif a == 6 or a == 7 or a == 8:
    print("Your choiсe is the Summer season")
elif a == 9 or a == 10 or a == 11:
    print("Your choiсe is the Autumn season")
else:
    print("You made a mistake. Try again!")
