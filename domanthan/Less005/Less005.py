#!/usr/bin/env python
# -*- coding: utf-8 -*-
# What we learn here: How to print, for loop controls.


class Magnifier :
    def observe(self, obj):
        print("-----------  Start Observing.......")
        print("-----------     type:", type(obj))
        print("-----------     id:", id(obj))
        print("-----------     is function?:", callable(obj))
        print("-----------     vars:", vars(type(obj)))
        print("<<<<<<<<<<<   End  Observing")
        print()

class Abc:
     name = "Abc"
     age = 12
     country = "ジオン公国"
     def say() :
           print(country, name)

magnifier = Magnifier()
magnifier.observe("abc")
magnifier.observe(magnifier.observe)
obj = Abc()
magnifier.observe(obj)

## Listを観察
abc = ["a","b","c"]
magnifier.observe(abc)

## Mapを観察
codes = {"a":1, "b":2, "c":3}
magnifier.observe(codes)

## 集合を観察
codeset  = {1,2,'A'}
magnifier.observe(codeset)
