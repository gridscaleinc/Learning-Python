#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Magnifier:
    def observe(self, obj):
        print("id:", id(obj))
        print("type:", type(obj))
        print("str:", str(obj))
        print("is function?:", callable(obj))
        print()

class Python:
     name = "Python"
     age = 27
     version = "3.7.0"
     author = "グイド・ヴァンロッサム"
     def say(self):
           print(self.name, self.age, self.version, self.author)

magnifier = Magnifier()

# integer
magnifier.observe(100)
# string
magnifier.observe("abc")
# list
abc = ["a", "b", "c"]
magnifier.observe(abc)
# dict
codes = {"a": 1, "b": 2, "c": 3}
magnifier.observe(codes)
# set
codeset = {1, 2, 'A'}
magnifier.observe(codeset)
# method
magnifier.observe(magnifier.observe)
# class
obj = Python()
magnifier.observe(obj)
