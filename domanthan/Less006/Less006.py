#!/usr/bin/env python
# -*- coding: utf-8 -*-

print ("１g＝１円での税込値段：")

pricelist1 = [int(i*1.08) for i in [98,105, 201,455,333,253,309]]
print (pricelist1)
sum1 = sum(pricelist1)
print ("売り上げ:", sum1)

print ("Premium付き税込値段：")

import math
pricelist2 = [int(int(i+math.sqrt(i))*1.08) for i in [98,105, 201,455,333,253,309]]
sum2 = sum(pricelist2)
print (pricelist2)

print ("売り上げ:", sum2)

print ("両者の売り上げ差:", (sum2 - sum1), "　増益率%:", int((sum2 - sum1)*100/sum1), "%")
