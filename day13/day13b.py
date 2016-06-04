import re
from itertools import permutations

inFile  = open('day13.txt', 'r');
patt = re.compile('([A-Za-z]*) would (gain|lose) ([0-9]+) happiness units by sitting next to ([A-Za-z]*).')
pairs = {}
people = set()

#Evaluates a solution.
def eval(sol):
    happiness = 0
    for i,person1 in enumerate(sol):
        person2 = sol[(i+1) % len(sol)]
        happiness += pairs[(person1,person2)]
        happiness += pairs[(person2,person1)]
    return happiness

# Main program. Go line by line through the file.
# Put stuff in our data structure.
for line in inFile:
    m = patt.match(line)

    if not m:
        print "Could not parse line: %s" % line
        continue

    mult = 1
    if m.group(2) == 'lose':
        mult = -1

    happiness = int(m.group(3)) * mult
    pairs[(m.group(1),m.group(4))] = happiness
    people.add(m.group(1))

    print "Person 1: %s\nPerson 2: %s\nHappiness: %d" % (m.group(1), m.group(4), happiness)

# Add ourselves.
for person in people:
    pairs[(person,'User')] = 0
    pairs[('User',person)] = 0
people.add("User")

bestSol = -99999
for soln in permutations(people):
    evaluated = eval(soln)
    if evaluated > bestSol:
        bestSol = evaluated

print bestSol
