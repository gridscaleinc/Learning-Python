#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyLife(object):

  history = []

  def mark(self, mark):
    self.history.append(mark)

  def show(self):
    for mark in self.history:
      print('  '.join(mark), end='')
      print()

life = MyLife()
life.mark(("1980年", "誕生", "中国の小さい村"))
life.mark(("2018年", "出世", "宝くじあたった"))

life.show()
