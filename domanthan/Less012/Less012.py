#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

def fibonacci():
    an, anext = 0, 1
    while(True):
        yield an
        an, anext = anext, an + anext

print ("Please print Ctrl+c to break!")
for fib in fibonacci():
    print (fib)
    sleep(1)
