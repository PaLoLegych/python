# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.

class Cloth:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_cloth_amount_coat(self):
        return self.size / 6.5 + 0.5

    def get_cloth_amount_suit(self):
        return self.height * 2 + 0.3

    @property
    def get_cloth_amount_total(self):
        return str(f'The total amount of cloth needed for sewing products: \n'
                   f'{round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}')


class Coat(Cloth):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.cloth_amount_coat = round(self.size / 6.5 + 0.5, 2)

    def __str__(self):
        return f'The amount of cloth for sewing a coat is:\n'\
               f' {self.cloth_amount_coat}'


class Suit(Cloth):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.cloth_amount_suit = round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'The amount of fabric for sewing a suit is:\n' \
               f'{self.cloth_amount_suit}'


# coat = Coat(4, 7)
coat = Coat(int(input('Please enter your size: ')), int(input('Please enter your height: ')))
print(coat)
# print(coat.get_cloth_amount_coat)
# print(coat.get_cloth_amount_total)

# suit = Suit(4, 7)
suit = Suit(int(input('Please enter your size: ')), int(input('Please enter your height: ')))
print(suit)
# print(suit.get_cloth_amount_suit)
print(suit.get_cloth_amount_total)
