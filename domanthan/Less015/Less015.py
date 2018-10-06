#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Circle:
    radius = 0

    # コンストラクタ
    def __init__(self, radius):
        self.radius = radius

    def circumLength(self):
        return 3.14 * 2 * self.radius

class Planet:
    revolutionPeriod = 0

    # コンストラクタ
    def __init__(self, revolutionPeriod):
        self.revolutionPeriod = revolutionPeriod

## 多重継承を注目
class Globe(Circle, Planet):
    rotationPeriod = 24*60*60
    myRadius = 6371

    # コンストラクタ
    def __init__(self):
        p = 365*24*60*60

        ## 親クラスのコンストラクタの呼び出し方を注目。
        Circle.__init__(self, 149600000)
        Planet.__init__(self, p)

    # 自転速度。
    def rotationSpeed(self):
        globeCircle = Circle(6371)
        return round(globeCircle.circumLength() / self.rotationPeriod, 2)

    # 公転速度
    def revolutionSpeed(self):
        return round(self.circumLength() / self.revolutionPeriod, 2)


globe = Globe()

print("地球の公転速度は : {0} km/s".format(globe.revolutionSpeed()))
print("地球の自伝速度は : {0} km/s".format(globe.rotationSpeed()))
