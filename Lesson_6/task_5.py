# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title, pen, pencil, handle):
        self.title = title
        self.pen = bool(pen)
        self.pencil = bool(pencil)
        self.handle = bool(handle)

    def draw(self):
        print('Start the rendering process: ', self.title)


class Pen(Stationary):
    # def __init__(self, title, pen, pencil, handle):
    #     super().__init__(title, pen, pencil, handle)

    def draw(self):
        if self.pen == True:
            print('Pen drawing started')
        else:
            print('Pen is not available')


class Pencil(Stationary):
    def draw(self):

        if self.pencil == True:
            print('Pencil drawing started')
        else:
            print('Pencil is not available')


class Handle(Stationary):
    def draw(self):

        if self.handle == True:
            print('Handle drawing started')
        else:
            print('Handle is not available')


title = Stationary('Beginning', False, False, False)
pen = Pen('Beginning', True, False, False)
pencil = Pencil('Beginning', False, True, False)
handle = Handle('Beginning', False, False, True)
title.draw()
pen.draw()
pencil.draw()
handle.draw()
