#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 konrad <konrad@serenity>
#
# Distributed under terms of the MIT license.

import md5


inStuff = "yzbqklnj"
curNum = 0;
found = False;

while not found:
    curNum += 1
    m = md5.new()
    m.update(inStuff);
    m.update(str(curNum));
    
    if m.hexdigest()[:5] == "000000": 
        found = True

    # print m.hexdigest()


print "Final Number is: %d" % curNum
print "Final Hash: " + m.hexdigest()

