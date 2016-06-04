import re
from itertools import chain, combinations

patt = re.compile("([0-9]+)")
containers = []
liters = 150

#Stolen from itertools page
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

with open('day17.txt') as inFile:
    for line in inFile:
        m = patt.match(line)

        if not m:
            print "Could not parse line: %s" % line
            continue

        containers.append(int(m.group(1)))

numSolutions = 0
minSize = 99999
for sol in powerset(containers):
    if sum(sol) == liters:
        numSolutions += 1
        if len(sol) < minSize:
            minSize = len(sol)

print "Number of Solutions: %d\nMinimum Solution Size: %d\n" % (numSolutions, minSize)

minSizeNumSol = 0
for sol in powerset(containers):
    if len(sol) != minSize:
        continue
    if sum(sol) == liters:
        minSizeNumSol += 1

print "Number of Solutions as minimum size: %d" % minSizeNumSol
