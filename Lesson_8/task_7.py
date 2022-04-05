# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexValue:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = 'a + j * b'

    def __add__(self, other):
        print('The result of the addition is: ')
        return f'val = {self.a + other.a} + {self.b + other.b}*j'

    def __mul__(self, other):
        print('The result of the multiplication is: ')
        return f'val = ({self.a * other.a - self.b * other.b}) + ' \
               f'({self.a * other.b + self.b * other.a})*j'


val_1 = ComplexValue(2, 5)
val_2 = ComplexValue(1, -3)
print(val_1 + val_2)
print(val_1 * val_2)
