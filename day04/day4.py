import md5


inStuff = "yzbqklnj"
curNum = 0;
found = False;

while not found:
    curNum += 1
    m = md5.new()
    m.update(inStuff);
    m.update(str(curNum));
    
    if m.hexdigest()[:5] == "00000": 
        found = True

    # print m.hexdigest()


print "Final Number is: %d" % curNum
print "Final Hash: " + m.hexdigest()

