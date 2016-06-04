import re

# Finds the shortest path.
# Recursion! Inefficient Recursion!
def longPath(path, totalWeight):
    # Base Case
    if len(path) == len(places):
        return totalWeight

    # Gross ugly multiple recursion calls here.
    # I think this is like O(n!) or comparable.
    # Probably worse with the python overhead.
    curMax = 0
    for place in places:
        if path == []:
            thisPath = longPath([place], 0)
            if thisPath > curMax:
                curMax = thisPath
        elif place not in path:
            linkWeight = graph[(path[len(path)-1], place)]
            newPath = list(path)
            newPath.append(place)
            thisPath = longPath(newPath, totalWeight + linkWeight)
            if thisPath > curMax:
                curMax = thisPath

    return curMax

# Represent it as a graph.
# Or a 2d array
# Or whatever python decides to do with memory I dunno.

graph = {}
places = []

inFile  = open('day9.txt', 'r');
patt = re.compile('([A-Za-z]*) to ([A-Za-z]*) = ([0-9]+)')

# Main program. Go line by line through the file.
# Put stuff in our data structure.
for line in inFile:
    m = patt.match(line)

    if not m:
        print "Could not parse line: %s" % line
        continue

    graph[(m.group(1),m.group(2))] = int(m.group(3))
    graph[(m.group(2),m.group(1))] = int(m.group(3))

    if not m.group(1) in places:
        places.append(m.group(1))
    if not m.group(2) in places:
        places.append(m.group(2))

    print "Source: %s\nDest: %s\nWeight: %s" % (m.group(1), m.group(2), m.group(3))

# Now we can do our pathfinding.
# Start at some arbitrary node. Doesn't matter which.

# TODO: Probably don't hard-code names.
print "Shortest Path Distance is: %d" % longPath([], 0)
