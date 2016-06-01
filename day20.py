#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 konrad <konrad@serenity>
#
# Elf House Delivery
import math

targetPresents = 34000000

houseNum = 0
housePresents = 0
while housePresents < targetPresents:
    houseNum += 1
    factors = set()
    
    for i in range(1, int(math.ceil(math.sqrt(houseNum) + 1))):
        if houseNum % i == 0:
            factors.add(i)
            factors.add(houseNum // i)

    housePresents = sum(factors) * 10

    # print "House %d gets %d presents" % (houseNum, housePresents)


print houseNum
print "House %d gets %d presents" % (houseNum, housePresents)
