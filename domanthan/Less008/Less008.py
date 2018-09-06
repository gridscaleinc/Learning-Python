#!/usr/bin/env python
# -*- coding: utf-8 -*-

class AddressInputSupport(object):
    addresses = {
        "124-0022": "東京都葛飾区奥戸",
        "143-0001": "東京都大田区東海",
        "133-0073": "東京都江戸川区鹿骨",
    }

    postsystem = {
        "東京都葛飾区奥戸" : "124-0022",
        "東京都大田区東海" : "143-0001",
        "東京都江戸川区鹿骨" : "133-0073",
    }

    def address(self, postnumber):
        return self.addresses[postnumber]

    def postnum(self, addr):
        return self.postsystem[addr]


addressbook = AddressInputSupport()

def fetch(pn) :
    try:
        address = addressbook.address(pn)
        print ("郵便番号[%s]の住所は[%s]です。" % (pn, address))
    except KeyError :
        print ("郵便番号[%s]は見つかりませんでした" % pn)

def reverse(addr) :
    try:
        postnum = addressbook.postnum(addr)
        print ("[%s]の郵便番号は%sです。" % (addr,postnum))
    except KeyError:
        print ("[%s]の郵便番号を見つかりませんでした" % addr)

test = "124-0022"
test1 = "123-0292"

fetch(test)
print("--")

fetch(test1)

print("--")

reverse("東京都葛飾区奥戸")

print("--")

reverse("東京都葛飾区奥戸1")
