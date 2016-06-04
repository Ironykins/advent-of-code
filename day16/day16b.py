import re

patt = re.compile("Sue ([0-9]+): ([A-Za-z]+): ([0-9]+), ([A-Za-z]+): ([0-9]+), ([A-Za-z]+): ([0-9]+)")
sueList = []
targetSue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1 }

with open('day16.txt') as inFile:
    for line in inFile:
        m = patt.match(line)

        if not m:
            print "Could not parse line: %s" % line
            continue

        curSue = {'number': int(m.group(1))}
        curSue[m.group(2)] = int(m.group(3))
        curSue[m.group(4)] = int(m.group(5))
        curSue[m.group(6)] = int(m.group(7))
        sueList.append(curSue)

for sue in sueList:
    candidate = True
    for targetAttr in targetSue:
        if targetAttr in sue:
            if targetAttr in ['cats','trees']:
                candidate = False if sue[targetAttr] <= targetSue[targetAttr] else candidate
            elif targetAttr in ['pomeranians','goldfish']:
            
                candidate = False if sue[targetAttr] >= targetSue[targetAttr] else candidate
            elif sue[targetAttr] != targetSue[targetAttr]:
                candidate = False

    if candidate:
        print sue['number']
