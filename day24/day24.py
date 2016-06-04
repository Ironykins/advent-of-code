from itertools import chain, combinations
from functools import reduce
from operator import mul

weights = []
groupWeight = 0 # The number of weights.

with open('day24.txt') as inFile:
    for line in inFile:
        weights.append(int(line.strip()))

# Change this to division by 4 for part b
groupWeight = sum(weights) // 3

# Find all divisions with equal weight.
min_entanglement = 999999999999999
for packageNum in range(2,len(weights)):
    for arrangement in combinations(weights, packageNum):
        if sum(arrangement) == groupWeight:
            min_entanglement = min(min_entanglement, reduce(mul,arrangement))

    if min_entanglement < 999999999999999:
        break

print min_entanglement
