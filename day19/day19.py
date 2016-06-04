import re

rulePattern = re.compile("([A-Za-z]+) => ([A-Za-z]+)")
endRules = False
formula = ""
rules = {}
derivations = []

with open('day19.txt') as inFile:
    for line in inFile:
        if not endRules and line == '\n':
            endRules = True

        if endRules:
            formula = line.strip()
        else:
            m = rulePattern.match(line)

            if not m:
                print "Could not parse line: %s" % line
                continue

            if not m.group(1) in rules:
                rules[m.group(1)] = []

            rules[m.group(1)].append(m.group(2))


# Iterate through each rule. Apply it to each part of the substring.
numDerivations = 0
for key in rules:
    for substitute in rules[key]:
        print "%s to %s" % (key, substitute)
        nextInd = formula.find(key,0)
        while nextInd >= 0:
            derivation = formula[:nextInd] + formula[nextInd:].replace(key,substitute,1)
            print derivation + '\n'
            if not derivation in derivations:
                derivations.append(derivation)
                numDerivations += 1

            nextInd = formula.find(key,nextInd+1)

print numDerivations
