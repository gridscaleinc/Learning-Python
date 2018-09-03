#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import array

girlSpeed = 3
girlPosition = array([10, 5000])
girlMove = array([1, 0.5])

mySpeed = 1000
myPosition = array([-1000, -1000])
myMove = array([1, 0.5])

flag = False
for mySpeed in range(1000):
  time = 1
  while True:
    girlStop = girlPosition - girlMove * girlSpeed * time
    myStop = myPosition + myMove * mySpeed * time
    print(girlStop)
    print(myStop)

    if girlStop[0] < myStop[0]:
      break

    if (girlStop == myStop).all():
      flag = True
      break
    time = time+1
  if flag:
    print("会えた！")
    break
