#Better bust out the regexes...
import re;
"""
Logic gates problem.
"""
inFile  = open('day7.txt', 'r');

# Matches <operand> <OP> <operand> -> <var>
# Operands can be vars or literals.
opPattern = re.compile('([0-9a-z]*)[\\s]*(AND|OR|LSHIFT|RSHIFT|NOT)[\\s]*([0-9a-z]+)[\\s]*->[\\s]*([a-z]+)');

# Matches <operand> -> <var>
assignPattern = re.compile('([0-9a-z]+)[\\s]*->[\\s]*([a-z]+)');

# Just holds
class Wire:
    def __init__(self, name):
        self.name = name
        self.op1 = None
        self.op2 = None
        self.operator = None
        self.value = None
        self.dynamicComputedValue = False

    # Only reset the values that we computed on the fly.
    def partBReset(self):
        if self.dynamicComputedValue:
            self.value = None

    # Value can be an operation
    def setExp(self, op1, op2, operator):
        self.op1 = op1
        self.op2 = op2
        self.operator = operator

    # Or an immediate
    def setValue(self, value):
        self.value = value

    # Evaluate the value of self wire.
    # Should always return an integer.
    def getVal(self):
        if self.value:
            # If our value is defined by another wire, get its value.
            # This will spit errors if there's a stray value inserted. That's cool.
            if self.value in wires:
                return wires[self.value].getVal()
            else:
                return int(self.value)
        else: # The interesting bit. Try to compute our value.
            # Get our operands. Number 1 is optional.
            if not self.op1:
                op1Val = 0
            elif self.op1 in wires:
                op1Val = wires[self.op1].getVal()
            else:
                op1Val = int(self.op1)

            if self.op2 in wires:
                op2Val = wires[self.op2].getVal()
            else:
                op2Val = int(self.op2)

            if self.operator == 'NOT':
                retVal = ~op2Val
            elif self.operator == 'AND':
                retVal = op1Val & op2Val
            elif self.operator == 'OR':
                retVal = op1Val | op2Val
            elif self.operator == 'RSHIFT':
                retVal = op1Val >> op2Val
            elif self.operator == 'LSHIFT':
                retVal = op1Val << op2Val

            # Store our value if we find it
            # Sorta like memoization but really shitty.
            if retVal:
                self.dynamicComputedValue = True
                self.value = retVal
                return retVal
            else:
                return 0


# Keep track of all our wires to avoid duplicates.
wires = {'a':Wire('a')}

# Main program. Go line by line through the file.
for line in inFile:
    opp = opPattern.match(line)
    if not opp:
        asp = assignPattern.match(line)

    if opp:
        # print 'Operand 1: %s' % opp.group(1)
        # print 'Operator: %s' % opp.group(2)
        # print 'Operand 2: %s' % opp.group(3)
        # print 'Destination: %s' % opp.group(4)
        wireName = opp.group(4)
        if not wireName in wires:
            wires[wireName] = Wire(wireName)

        # Set the value in terms of the operators and operation.
        wires[wireName].setValue(None)
        wires[wireName].setExp(opp.group(1), opp.group(3), opp.group(2))
    elif asp:
        # print 'Value is: %s' % asp.group(1)
        # print 'Destination: %s' % asp.group(2)
        wireName = asp.group(2)
        if not wireName in wires:
            wires[wireName] = Wire(wireName)

        # Can be an immediate value or another wire name. Don't care.
        wires[wireName].setExp(None,None,None)
        wires[wireName].setValue(asp.group(1))
    else:
        print 'Could Not Parse: \"%s\"' % line

aVal = wires['a'].getVal()
print "\nValue of a: %d" % (aVal)
print "Resetting wire values for part b..."

for key in wires:
    wires[key].partBReset()

wires['b'].setValue(str(aVal))
aVal = wires['a'].getVal()
print "New value of a: %d" % (aVal)
