# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def extraction(cls, d_m_y):
        my_date = []

        for i in d_m_y.split():
            if i != '/':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def validation(d, m, y):
        # if 1 <= d <= 31:
        #     return f'Date is correct!'
        # else:
        #     f'Incorrect day'
        #
        # if 1 <= m <= 12:
        #     return f'Date is correct!'
        # else:
        #     f'Incorrect month'
        #
        # if 0 <= y <= 2022:
        #     return f'Date is correct!'
        # else:
        #     f'Incorrect year'

        if 1 <= d <= 31:
            if 1 <= m <= 12:
                if 988 <= y <= 2050:
                    return f'The entered date is correct.'
                else:
                    return f'Please enter correct year.'
            else:
                return f'Please enter correct month.'
        else:
            return f'Please enter correct day.'

    def __str__(self):
        return f'The current date is: {Date.extraction(self.d_m_y)}'


day = Date('3 / 4 / 2000')
print(day)

print(Date.validation(16, 6, 2022))
print(Date.validation(3, 15, 2000))
print(day.validation(3, 4, 950))
print(Date.extraction('3 / 4 / 2022'))
print(day.extraction('3 / 4 / 2022'))
