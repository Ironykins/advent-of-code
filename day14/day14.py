import re

targetTicks = 2503
patt = re.compile("([A-Za-z]*) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.")
reindeerlist = {}

with open('day14.txt') as inFile:
    for line in inFile:
        m = patt.match(line)

        if not m:
            print "Could not parse line: %s" % line
            continue

        curDeer = {'name': m.group(1), 
                'speed': int(m.group(2)),
                'runtime': int(m.group(3)),
                'resttime': int(m.group(4)),
                'dist': 0, # Total Distance Travelled
                'rested': 0, # Time rested.
                'run': 0, # Time run
                'stopped': False, # If we're stopped.
                }

        reindeerlist[m.group(1)] = curDeer
        
#Run the simulation
for ticks in range(targetTicks):
    for name in reindeerlist:
        deer = reindeerlist[name]
        if deer['stopped'] == False:
            deer['dist'] += deer['speed']
            deer['run'] += 1
        else:
            deer['rested'] += 1

        # Done running? Switch to rest.
        if deer['run'] >= deer['runtime']:
            deer['stopped'] = True
            deer['run'] = 0

        # Done resting? Switch to run.
        if deer['rested'] >= deer['resttime']:
            deer['stopped'] = False
            deer['rested'] = 0


# Get results
maxDist = 0
for name in reindeerlist:
    if reindeerlist[name]['dist'] > maxDist:
        maxDist = reindeerlist[name]['dist']

print maxDist

