#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 konrad <konrad@serenity>
#
# Accounting Elves

import json

def sumInts(node):
    if type(node) is int:
        return node
    elif type(node) is dict:
        total = 0
        for key in node:
            total += sumInts(node[key])
        return total
    elif type(node) is list:
        total = 0
        for item in node:
            total += sumInts(item)
        return total
    else:
        return 0

with open('day12.txt') as inFile:
    parsed = json.load(inFile)
    totalNums = 0

    print sumInts(parsed)
