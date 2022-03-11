# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги
# асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def square(self):
        square = self._length * self._width / 1000000
        print(f'Road surface area is: {square} km\u00B2')

    def mass(self, mass_m2=25, tickness=25):
        mass = self._length * self._width * mass_m2 * tickness / 1000
        print(f'For the construction of a road with length of {self._length} m. and width of {self._width} m.,\n'
              f' {mass} tons of asphalt will be required.')


road = Road(15000, 20)
road.square()
road.mass()
