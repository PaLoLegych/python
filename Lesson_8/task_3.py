#  Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
#  Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список
#  необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.

class MyOwnErr:
    def __init__(self, value):
        self.value = value
        self.my_list = []

    def content(self, value):
        while True:
            try:
                value = int(input(f'Please enter a number: '))
                self.my_list.append(value)
                print(f'The current list is: {self.my_list} \n')
            except:
                if type(value) != int():
                    print(f'This value is not allowed!')
            else:
                choice = input(f'Would you like to try again? (Y/N)? - ')

                if choice == 'Y' or choice == 'y':
                    print(my_exception.content(value))
                elif choice == 'N' or choice == 'n':
                    print(f'Exit done.')


my_exception = MyOwnErr(1)
print(my_exception.content(0))
