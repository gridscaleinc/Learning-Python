#!/usr/bin/env python
# -*- coding: utf-8 -*-
# What we learn here: How to print, for loop controls.

class Person(object):
    # constructor
    def __init__(self, relation, name, age):
        self.relation = relation
        self.age = age
        self.name = name

    def description(self):
        print (self.relation, end='    ') ; print (self.name, end='    ') ; print (str(self.age) + "才")

# リストの初期化
family = []
me = Person("本人", "ドム", 45)
daughter = Person("長女", "チェルシー", 12)
dog = Person("愛犬", "ドフィー", 2)
# リストは足し算できるのです
family += [me, daughter, dog]

from datetime import date

#　改行しない　Print句を注目してください。
print ()
print ("出力日:", end='　')
print (date.today())
print ("----------------------------")

for member in family:
    member.description()


''' Memo
１．Print句相関
      （１）.Python3の場合、Printが「Print文」から「Print関数」へと変わり、
      それにあわせて、末尾に追加される文字を　end optionで指定できるようになりました。

      （２）. from 。。。import。。。。の形で一文を宣言すると、print文を上書きする形で　Python３のPrint関数を
      使うことができるようになります。

２．Listの使い方
'''

