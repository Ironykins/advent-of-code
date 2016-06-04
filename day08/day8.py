import re

inFile  = open('day8.txt', 'r');
escChars = 0
codeChars = 0
memChars = 0

# HANG ON I GOTTA ESCAPE EACH SEQUENCE THREE TIMES
# (This pattern matches each escape sequence)
patt = re.compile('(\\\\\\\\|\\\\"|\\\\x[0-9a-f]{2})')

# Main program. Go line by line through the file.
for line in inFile:
    workingLine = line.strip() # Strip the newline.

    # Number of characters in code is easy.
    codeChars += len(workingLine)

    # For the memory characters, discount the surrounding quotes.
    # Replace all escape sequences with a single character
    # Count what remains.
    memoryLine = workingLine.strip("\"") #strip the quotes
    memoryLine = patt.sub("!", memoryLine)
    memChars += len(memoryLine)

    # For the extra escaped characters, find all things that need to be escaped
    # Add an extra character for each one we find.
    # Don't forget to add extra surrounding quotes.
    escChars += 2
    for chara in workingLine:
        escChars += 1
        if chara == '\"' or chara == '\\':
            escChars += 1

print "Chars in Code: %d\nChars in Memory: %d" % (codeChars, memChars)
print "Part A Answer: %d" % (codeChars - memChars)
print "Chars in Escaped Code: %d\nChars in Code: %d" % (escChars, codeChars)
print "Part B Answer: %d" % (escChars - codeChars)
