#  Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
#  Проверьте его работу на данных, вводимых пользователем.
#  При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
#  и не завершиться с ошибкой.

class Division:
    def __init__(self, divident, divider):
        self.divident = divident
        self.divider = divider

    @staticmethod
    def division_by_null(divident, divider):
        try:
            return (divident / divider)
        except:
            return (f'Division by null is not allowed!')


div = Division(25, 5)
print(Division.division_by_null(25, 0))
print(Division.division_by_null(45, 5))
print(div.division_by_null(25, 0))
