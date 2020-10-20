# -*- coding: UTF-8 -*-
class Car:
    color = "red"

    def __init__(self, color=""):
        if color != "":
            self.color = color

    def drive(self):
        s1 = self.color+" car are going"
        print(s1)


car = Car()
car.drive()

car2 = Car("orange")
car2.drive()


class BlueCar(Car):
    color = "blue"


blueCar = BlueCar()
blueCar.drive()


class FlyCar(Car):
    def fly(self):
        print "%s flycar are flighting" % (self.color)


FlyCar().fly()
