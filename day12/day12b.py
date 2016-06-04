import json

def sumInts(node):
    if type(node) is int:
        return node
    elif type(node) is dict:
        total = 0
        for key in node:
            if node[key] == "red": # Ingore things with 'red' in them.
                return 0
            total += sumInts(node[key])
        return total
    elif type(node) is list:
        total = 0
        for item in node:
            total += sumInts(item)
        return total
    else:
        return 0

with open('day12.txt') as inFile:
    parsed = json.load(inFile)
    totalNums = 0

    print sumInts(parsed)
