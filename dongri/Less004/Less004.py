#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import date

class Family:
  peoples = []
  def add(self, person):
    self.peoples.append(person)
  def print(self):
    print("\n出力日:", date.today())
    print("----------------------------")
    for i, person in enumerate(self.peoples):
      print(person.relation, person.name, str(person.age) + "才")

class Person:
  def __init__(self, relation, name, age):
    self.relation = relation
    self.age = age
    self.name = name

family = Family()
family.add(Person("本人 ", "どんぐり ", 38))
family.add(Person("妻　 ", "ボア　　 ", 38))
family.add(Person("息子 ", "エン　　 ", 8))

family.print()
