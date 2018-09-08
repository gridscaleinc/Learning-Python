#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class ClassRoom:
    groups = [
        ["A1","A2","A3","A4","A5","A6","A7","A8"],
        ["B1","B2","B3","B4","B5","B6","B7","B8"],
        ["C1","C2","C3","C4","C5","C6","C7","C8"],
        ["D1","D2","D3","D4","D5","D6","D7"]]

    def reSortGroups(self):
        allmembers = []
        for g in self.groups:
            allmembers.extend(g)

        ## Randomに列を並び替える
        random.shuffle(allmembers)
        
        ## Where is B3?
        positionOfB3 = allmembers.index("B3")
        positionOfA8 = allmembers.index("A8")

        if positionOfB3 % 8 == 0:
            ## B3の前にA8を置く
            allmembers.remove("A8")
            allmembers.insert(allmembers.index("B3"), "A8")
        elif positionOfB3 % 8 > 0 and  positionOfB3 % 8 < 7:
            ## B3の後ろにA8を置く
            allmembers.remove("A8")
            allmembers.insert(allmembers.index("B3") + 1, "A8")
        else :
            ## B3の前人とA8を入れ替え
            prefer = allmembers[positionOfB3 - 1]
            a8 = allmembers[positionOfA8]
            allmembers[positionOfB3 - 1], allmembers[positionOfA8] = a8, prefer

        positionOfC3 = allmembers.index("C3")
        if positionOfB3 > 15:
            first = allmembers[0]
            c3 = allmembers[positionOfC3]
            allmembers[0], allmembers[positionOfC3] = c3, first
        else :
            ## B3の前にA8を置く
            last = allmembers[30]
            c3 = allmembers[positionOfC3]
            allmembers[30], allmembers[positionOfC3] = c3, last


        group1 = allmembers[0:8]
        group2 = allmembers[8:16]
        group3 = allmembers[16:24]
        group4 = allmembers[24:]

        self.groups[0] = group1
        self.groups[1] = group2
        self.groups[2] = group3
        self.groups[3] = group4

        for g in self.groups:
            print(g)

cr = ClassRoom()

cr.reSortGroups()




        


