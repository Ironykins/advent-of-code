#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 konrad <konrad@serenity>
#
# Chemistry
import re

rulePattern = re.compile("([A-Za-z]+) => ([A-Za-z]+)")
endRules = False
rules = {}
derivations = {} # Keyed by chemical formula.
target = ""

with open('day19.txt') as inFile:
    for line in inFile:
        if not endRules and line == '\n':
            endRules = True

        if endRules:
            target = line.strip()
        else:
            m = rulePattern.match(line)

            if not m:
                print "Could not parse line: %s" % line
                continue

            rules[m.group(2)] = m.group(1)

orderedKeys = sorted(rules.keys(), reverse=True, key=len)

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

# Use recursive magic.
def backward_replace(string):
    # print string
    if string == "e":
        return 0

    for key in orderedKeys:
        if key in string:
            replaced = backward_replace(string.replace(key,rules[key],1))
            if replaced >= 0:
                return 1 + replaced
    return -1

print backward_replace(target)
