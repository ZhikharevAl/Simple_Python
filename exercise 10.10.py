"""
Определите три класса: Laser, Claw и SmartPhone. Каждый из них имеет только
один метод — does(). Он возвращает значения 'disintegrate' (для Laser),
'crush' (для Claw) или 'ring' (для SmartPhone). Далее определите класс Robot,
который содержит по одному объекту каждого из этих классов. Определите
метод does() для класса Robot, который выводит на экран все, что делают его
компоненты
"""


class Laser:
    def does(self, desintegrate='desintegrate'):
        return desintegrate


class Claw:
    def does(self, crush='crush'):
        return crush


class SmartPhone:
    def does(self, ring='ring'):
        return ring


class Robot(Laser, Claw, SmartPhone):
    def does(self, **kwargs):
        return Laser().does() + ' ' + Claw().does()+ ' ' + Smartphone().does()


laser = Laser()
claw = Claw()
smartphone = SmartPhone()
robot = Robot()

print(laser.does(), claw.does(), smartphone.does())
