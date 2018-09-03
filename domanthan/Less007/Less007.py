#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyLife(object):

    history = []

    def addFootMark(self, mark):
        self.history.append(mark)

    def show(self):
        print("私の人生の履歴:")
        print("---------------------------------------------------------------------------")
        for mark in self.history:
            ## Tupleはこの様にアサインできるのです。。。。
            dateInfo, stage, place, latitude, longitude = mark

            print(dateInfo, "   ", stage, "   ", place, "     地理位置: (", latitude, ",", longitude, ")")


life = MyLife()
life.addFootMark(("1969年", "誕生", "中国の小さい村", 111,222))
life.addFootMark(("1976年", "小学校", "XXX小学校", 222,333))
life.addFootMark(("1988年", "大学校", "中国XXX大学", 333,22))
life.addFootMark(("1996年", "来日", "ABC株式会社", 322,23))

life.show()
