#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 konrad <konrad@serenity>
#
# Copy Protection on the Weather Machine

initial_code = 20151125
target_row = 2947
target_col = 3029

def next_code(num):
    return (num * 252533) % 33554393

row = 1
col = 1
num = initial_code
while row != target_row or col != target_col:
    num = next_code(num)

    if row == 1:
        row += col
        col = 1
    else:
        row -= 1
        col += 1

    # print "(%d,%d) -> %d" % (row,col,num)
print "(%d,%d) -> %d" % (row,col,num)

