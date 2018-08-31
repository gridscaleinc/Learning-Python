#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b

print([fib(i) for i in range(10)]) 
