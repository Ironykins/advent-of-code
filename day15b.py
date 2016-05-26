#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 konrad <konrad@serenity>
#
# Cookie Recipes
import re

patt = re.compile("([A-Za-z]+): capacity ([-]*[0-9]+), durability ([-]*[0-9]+), flavor ([-]*[0-9]+), texture ([-]*[0-9]+), calories ([-]*[0-9]+)")
ingredientList = {}

# Cookie should be a dict with ingredient names as keys and amounts as values.
def scoreCookie(cookie):
    cap = dur = fla = tex = cal = 0
    for ing in cookie:
        numIng = cookie[ing]
        cap += numIng * ingredientList[ing]['capacity']
        dur += numIng * ingredientList[ing]['durability']
        fla += numIng * ingredientList[ing]['flavor']
        tex += numIng * ingredientList[ing]['texture']
        cal += numIng * ingredientList[ing]['calories']
    if cal != 500:
        return 0

    #Make sure we don't have negatives.
    cap = 0 if cap < 0 else cap
    dur = 0 if dur < 0 else dur
    fla = 0 if fla < 0 else fla
    tex = 0 if tex < 0 else tex

    return cap * dur * fla * tex

with open('day15.txt') as inFile:
    for line in inFile:
        m = patt.match(line)

        if not m:
            print "Could not parse line: %s" % line
            continue

        curIngredient = {'name': m.group(1),
                'capacity': int(m.group(2)),
                'durability': int(m.group(3)),
                'flavor': int(m.group(4)),
                'texture': int(m.group(5)),
                'calories': int(m.group(6))
                }

        ingredientList[m.group(1)] = curIngredient


#HAHA ID ONT GIVE A FUCK
#In all honestly there's probably a generalized way to do this
#Using a dynamic programming type approach.
maxScore = 0
for numF in range(101):
    for numC in range(101):
        for numB in range(101):
            numS = 100 - numF - numC - numB
            if numS < 0:
                continue
            elif numF + numC + numB + numS == 100:
                thisCookie = {'Frosting': numF, 'Candy': numC, 'Butterscotch':numB,'Sugar':numS}
                thisScore = scoreCookie(thisCookie)
                if thisScore > maxScore:
                    print thisCookie
                    maxScore = thisScore

print maxScore
