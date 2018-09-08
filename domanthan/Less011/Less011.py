#!/usr/bin/env python
# -*- coding: utf-8 -*-

aiueo = "あいうえお"
katakana = "アイウエオ"

print ("左から右へ:")
for i in aiueo:
    print(i, end=', ')
print ("")


print ("真ん中から:")
for i in aiueo:
    idx = aiueo.index(i)
    newlist=aiueo[idx+1:] + aiueo[0:idx+1]
    for c in newlist:
        print(c, end=', ')
    print ("")

print ("random:")
import random
for i in range(5):
    newlist = list(aiueo)
    random.shuffle(newlist)
    for a in newlist:
        print(a, end=', ')
    print ("")

print ("Reversed:")
newlist=reversed(aiueo)
for c in newlist:
    print(c, end=', ')
print ("")

print ("カタカナ変換:")
for i in "えおいうあ":
    idx = aiueo.index(i)
    print(katakana[idx], end=', ')

print("")

