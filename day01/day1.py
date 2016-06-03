#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 konrad <konrad@bebop>
#
# Distributed under terms of the MIT license.

"""
First problem in the advent of Code!
Let's learn some Python
"""

f = open('day1.txt', 'r')
floor = 0
position = 0
enteredBasement = False

for charThing in f.read():
    position += 1
    if charThing == '(':
        floor += 1
    elif charThing == ')' :
        floor -= 1

    if floor == -1 and not enteredBasement:
        enteredBasement = True
        print "Entered Basement at: %d" % (position, )

print "Ended at floor: %d" % (floor, )
