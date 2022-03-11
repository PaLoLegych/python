# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:

    def __init__(self, title, pen, pencil, handle):
        self.title = title
        self.pen = pen
        self.pencil = pencil
        self.handle = handle

    def draw(self):
        print('Start the rendering process: ', self.title)


class Pen(Stationary):

    def draw(self):
        if self.pen == True:
            print('The pen tool is ready. The rendering process is started')
        else:
            print('The pen tool is not available. Please, choose a different tool.')


class Pencil(Stationary):

    def draw(self):
        if self.pencil == True:
            print('The pencil tool is ready. The rendering process is started')
        else:
            print('The pencil tool is not available. Please, choose a different tool.')


class Handle(Stationary):

    def draw(self):
        if self.handle == True:
            print('The handle tool is ready. The rendering process is started')
        else:
            print('The handle tool is not available. Please, choose a different tool.')


print('Test option 1:')
title = Stationary('Beginning', False, False, False)
pen = Pen('Beginning', True, False, False)
pencil = Pencil('Beginning', False, True, False)
handle = Handle('Beginning', False, False, True)
title.draw()
pen.draw()
pencil.draw()
handle.draw()

print('Test option 2:')
title = Stationary('Beginning', False, False, False)
pen = Pen('Beginning', True, False, False)
pencil = Pencil('Beginning', True, False, False)
handle = Handle('Beginning', False, False, False)
title.draw()
pen.draw()
pencil.draw()
handle.draw()

print('Test option 3:')
title = Stationary('Beginning', False, False, False)
pen = Pen('Beginning', False, False, False)
pencil = Pencil('Beginning', False, True, False)
handle = Handle('Beginning', True, False, False)
title.draw()
pen.draw()
pencil.draw()
handle.draw()
