#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 konrad <konrad@serenity>
#
# Santa's Password

oldPass = "vzbxkghb"
banned = "iol"

# "increments" the password. No other checks.
def increment(password):
    passList = list(password)
    i = len(password) - 1

    while i >= 0:
        newChar = ord(password[i]) + 1
        if newChar > 122: # Lowercase z
            newChar = 97 # lowercase a
            passList[i] = chr(newChar)
            i -= 1
        else:
            passList[i] = chr(newChar)
            break

    return "".join(passList)

# Passes requirements? Returns boolean
def verify(password):
    #Check our blacklist
    for item in banned:
        if item in password:
            return False

    #Verify that there's a sequence of 3 incrementing letters
    good = False
    for i in range(len(password) - 3):
        if ord(password[i+1]) - ord(password[i]) == 1 and ord(password[i+2]) - ord(password[i+1]) == 1:
               good = True
    if not good:
        return False

    #Verify Duplicate Letter Requirement
    dupes = 0
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i+1]:
            dupes += 1
            i += 1
        i += 1

    if dupes < 2:
        return False

    return True

def newPass(password):
    ret = increment(password)
    while not verify(ret):
        ret = increment(ret)
    return ret

new1 = newPass(oldPass)
new2 = newPass(new1)
print "New Password: %s\nNew New Password: %s" % (new1, new2)
