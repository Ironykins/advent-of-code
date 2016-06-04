import math

targetPresents = 34000000

houseNum = 0
housePresents = 0
while housePresents < targetPresents:
    houseNum += 1
    factors = set()
    
    for i in range(1, int(math.ceil(math.sqrt(houseNum) + 1))):
        if houseNum % i == 0:
            factors.add(i)
            factors.add(houseNum // i)

    relevantFactors = set()
    for n in factors:
        if houseNum // n <= 50:
            relevantFactors.add(n)

    housePresents = sum(relevantFactors) * 11


print houseNum
print "House %d gets %d presents" % (houseNum, housePresents)
