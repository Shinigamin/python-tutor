
class Car(object):

    def __init__(self, doors, max_speed, breaks, color):
        self.doors = doors
        self.max_speed = max_speed
        self.breaks = breaks
        self.color = color

    def move(self):
        print('Move {}Km'.format(self.max_speed))

    def buzz(self):
        print('buzzzz')



class Gol1000(Car):

    def __init__(self, doors, max_speed, breaks, color):
        max_speed = max_speed / 2
        super().__init__(doors, max_speed, breaks, color)


    def move(self):
        super().move()
        print('batery is over')


class Ferrari(Car):
    pass


class AlfaRomeo(Car):
    pass




gol_1000 = Gol1000(4, 2, 'common', 'branco pe de boi')
ferrari = Ferrari(doors=2, max_speed=200, breaks='abs', color='red')
