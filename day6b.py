#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 konrad <konrad@serenity>
#
# Distributed under terms of the MIT license.

"""
Light Grid Problem
"""
inFile  = open('day6.txt', 'r');

# As good a way as any to represent a grid of lights.
grid = [[0 for x in range(1000)] for x in range(1000)] 
brightness = 0;

# Performs a turn on, turn off, or toggle operation.
def operate(op, x, y):
    global brightness
    global grid
    if op == "toggle":
        grid[x][y] += 2
        brightness += 2
    elif op == "off":
        if grid[x][y] > 0:
            grid[x][y] -= 1
            brightness -= 1
    elif op == "on":
        grid[x][y] += 1
        brightness += 1
    else:
        raise "WHAT DID YOU DO"

# Main program. Go line by line through the file.
for line in inFile:
    splitz = line.split(' ');
    op = splitz[0]
    if op != "toggle":
        op = splitz[1]
        pair1 = splitz[2]
        pair2 = splitz[4]
    else:
        arg = ""
        pair1 = splitz[1]
        pair2 = splitz[3]

    p1split = pair1.split(',');
    p1x = int(p1split[0])
    p1y = int(p1split[1])

    p2split = pair2.split(',');
    p2x = int(p2split[0])
    p2y = int(p2split[1])

    for x in range(p1x, p2x+1):
        for y in range(p1y, p2y+1):
            operate(op, x, y)

    print "Operation: " + op
    print "Pair1: %d, %d" % (p1x, p1y)
    print "Pair2: %d, %d" % (p2x, p2y)

    
print "Brightness: %d" % (brightness)

