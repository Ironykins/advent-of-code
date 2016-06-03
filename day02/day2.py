#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 konrad <konrad@serenity>
#
# Distributed under terms of the MIT license.

"""
Wrapping paper problem.
"""

inFile  = open('day2.txt', 'r');
totalArea = 0
totalRibbon = 0

for line in inFile:
    splitz = line.split('x');
    l = int(splitz[0])
    w = int(splitz[1])
    h = int(splitz[2])

    longMeasure = max(l, w, h)
    sideRibbon=2*l+2*w+2*h-2*longMeasure

    side1 = l * w;
    side2 = w * h;
    side3 = h * l;

    bowRibbon = l * w * h
    smallSide = min(side1, side2, side3)

    area = 2 * side1 + 2*side2 + 2*side3 + smallSide;
    totalArea += area;
    totalRibbon += bowRibbon
    totalRibbon += sideRibbon

    
print "Total Area: %d" % (totalArea)
print "Total Ribbon: %d" % (totalRibbon)

