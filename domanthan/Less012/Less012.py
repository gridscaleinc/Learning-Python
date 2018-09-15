#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

def fibonacci():
    first,next = 0,1
    while(True):
        yield first
        first, next = next , first + next

print ("Please print Ctrl+c to break!")
for fib in fibonacci():
    print (fib)
    sleep(1)
