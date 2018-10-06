
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

## Immutable
class Vector:
    x,y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def sub(self, v):
        return self.add(v.multiply(-1))

    def multiply(self, a):
        return Vector(self.x*a, self.y*a)

    def normalized(self):
        if self.x == 0 and self.y == 0 :
            raise "0 Vector can not be normalized"

        r = math.sqrt(math.pow(self.x,2) + math.pow(self.y,2))
        return Vector(self.x / r, self.y/r)

    ## 2d Corss product
    def cross(self, v):
        return self.x*v.y - v.x*self.y

    def __str__(self):
        return "(x,y) = (" + str(self.x) + "," + str(self.y) + ")"

## 光線クラス
def Ray:

    ## 初期化
    def __init__(startPoint, direction):
        self.start = startPoint
        self.direction = direction

    ## 日本の光が交わる点を計算。
    ## 平行の場合はNoneを返す。
    ## 交点求める式：
　　## p + t r = q + u s
　　
　　## t = (q − p) × s / (r × s)
　　## u = (p − q) × r / (s × r)
    def intersect(self, anotherRay) :
        rCrossS = self.direction.cross(anotherRay.direction)
        if (rCrossS == 0) :
            return None

        qSubP = anotherRay.start.sub(self.start)
        qSubPCrossS = qSubP.cross(anotherRay.direction)

        t = qSubPCrossS / rCrossS
        intersectionPoint = self.start.add(self.direction.multiply(t))
        

### __main__
girlPosition = Vector(10, 5000)
girlVelocity = Vector(1, -0.5).normalized().multiply(3)

print("Girl's position:", str(girlPosition))
print("girl's velocity:", str(girlVelocity))

myPosition = Vector(-1000, -1000)
myDirection = Vector(1, 0.5).normalized()

print("My position:", str(myPosition))
print("My direction:", str(myDirection))

distance = girlPosition.sub(myPosition)
print("Distance Between twos:", str(distance))

## 出会う条件
## myPosition + myDirection * s * t = girlPosition + girlVelocity * t
