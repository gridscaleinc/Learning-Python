#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

TAX=1.08
weightList = [98, 105, 201, 455, 333, 253, 309]

print()
print("1g＝1円での税込値段:")
priceNormal = [int(i*TAX) for i in weightList]
print(priceNormal)
sumNormal = sum(priceNormal)
print("通常売り上げ:", sumNormal)

print()
print("Premium付き税込値段:")
pricePremium = [int(int(i+math.sqrt(i))*TAX) for i in weightList]
print(pricePremium)
sumPremium = sum(pricePremium)
print("プレミアム売り上げ:", sumPremium)

print()
sub = sumPremium - sumNormal
print("両者の売り上げ差:{} \n増益率: {:0.2f}%".format(sub, sub*100/sumNormal))
