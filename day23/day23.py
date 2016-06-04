instructions = []

with open('day23.txt') as inFile:
    for line in inFile:
        words = line.split(' ')
        instructions.append(map(str.strip,words))

reg = {'a': 0, 'b': 0}
ip_reg = 0 #Instruction Pointer
while ip_reg < len(instructions):
    curInst = instructions[ip_reg]
    if curInst[0] == 'hlf': # Half the register
        reg[curInst[1]] /= 2
        ip_reg += 1
    elif curInst[0] == 'tpl':
        reg[curInst[1]] *= 3
        ip_reg += 1
    elif curInst[0] == 'inc':
        reg[curInst[1]] += 1
        ip_reg += 1
    elif curInst[0] == 'jmp':
        ip_reg += int(curInst[1])
    elif curInst[0] == 'jie':
        if reg[curInst[1].strip(",")] % 2 == 0:
            ip_reg += int(curInst[2])
        else:
            ip_reg += 1
    elif curInst[0] == 'jio':
        if reg[curInst[1].strip(",")] == 1:
            ip_reg += int(curInst[2])
        else:
            ip_reg += 1
    else:
        print "invalid syntax %s" % curInst

print "Value of A: %d\nValue of B: %d" % (reg['a'],reg['b'])
