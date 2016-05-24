#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 konrad <konrad@serenity>
#
# Look and Say Algorithm

def looksay(numstr):
    ret = ""
    curCount = 0
    curChar = numstr[0]
    for char in numstr: # Iterate each character
        if char == curChar: # Count number of consecutive chars
            curCount += 1
        else:
            ret += str(curCount)
            ret += str(curChar)
            curChar = char
            curCount = 1

    ret += str(curCount)
    ret += str(curChar)
    return ret

number = "1321131112"

for i in range(50):
    number = looksay(number)

print "Total Length: %d" % (len(number))
