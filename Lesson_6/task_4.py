# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля; для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'start moving with the speed {self.speed} km/h'

    def stop(self):
        return f'slowdown and stop moving'

    def turn_left(self):
        return f'turn left'

    def turn_right(self):
        return f'turn right'

    def show_speed(self):
        return f'Current car speed is: {self.speed}'


class TownCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Exceeding the speed limit for moving around the city in 60 km/h. Current speed of', self.name, 'is',
                  self.speed, 'km/h')
        else:
            print('No over-speed detected. The current speed of', self.name, 'is', self.speed, 'km/h')


class SportCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def sport_car(self):
        pass


class WorkCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Exceeding the speed limit for special vehicles for moving around the city in 40 km/h. '
                  'Current speed of', self.name, 'is', self.speed, 'km/h')
        else:
            print('No over-speed detected. The current speed of', self.name, 'is', self.speed, 'km/h')


class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def police(self):
        if self.is_police:
            print('This', self.name, 'belongs to the police office')
        else:
            print('This', self.name, 'is civilian')


car_a = TownCar('Mercedes', 'White', 60, False)
car_b = SportCar('McLaren', 'Dark-red', 240, False)
car_c = WorkCar('Kamaz', 'Orange', 60, False)
car_d = PoliceCar('BMW', 'Unknown', 100, True)
print(f'Car {car_a.name} {car_a.go()} then {car_a.turn_left()}, {car_a.stop()}')
print(f'Car {car_b.name} {car_b.go()} then {car_b.turn_right()}, {car_b.stop()}')
print(f'Car {car_c.name} {car_c.go()} then {car_c.turn_left()}, {car_c.stop()}')
print(f'Car {car_d.name} {car_d.go()} then {car_d.turn_left()}, {car_d.stop()}')
car_a.show_speed()
car_b.sport_car()
car_c.show_speed()
car_d.police()
print(f'Is {car_a.name} belong to police office?:  {car_a.is_police}')
