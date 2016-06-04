"""
Infinite House Grid Problem
"""

inFile  = open('day3.txt', 'r');
luckyHouseCount = 0;

# Keep track of house presents with a dictionary.
grid = {}
x = [ 0,0 ] # Santa's value, Robo Santa's Value
y = [ 0,0 ]
turn = 0

for char in inFile.read():
    idx = turn % 2;
    if char == '>': 
        x[idx] += 1
    elif char == '<':
        x[idx] -= 1
    elif char == '^':
        y[idx] += 1
    elif char == 'v':
        y[idx] -= 1

    if (x[idx],y[idx]) in grid:
        grid[(x[idx],y[idx])] = grid[(x[idx],y[idx])] + 1
    else:
        grid[(x[idx],y[idx])] = 1
        luckyHouseCount+=1

    turn+=1
    

print "Houses that get at least one present: %d" % (luckyHouseCount)

