#!/usr/bin/env python3
from collections import Counter
def anagram(s,t):
    s = s.replace(' ','')
    t = t.replace(' ','')

    if len(s) != len(t):
        return False

    counter1 = Counter(s)
    counter2 = Counter(t)

    counter3 = counter1 - counter2
    for val in counter3.values():
        if val != 0:
            return False

    return True

print(anagram('dog','god'))
print(anagram('clint eastwood','old west action'))
print(anagram('aa','bb'))

def isAnagram(s,t):
	#to understand if both the strings have same letters or not 
	#First thing we can do is sort letter from those string
    ss = ','.join(sorted(s))
    tt = ','.join(sorted(t))
    #And the compare those letters with each other
    if ss == tt:
    #if they have same letters, after sorting they will match so answer will be True
        return(True)
    else:
    #otherwise false
        return(False)

print(anagram('dog','god'))
print(anagram('clint eastwood','old west action'))
print(anagram('aa','bb'))
