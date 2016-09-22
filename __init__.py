# -*- coding: utf-8 -*-

from __future__ import division
def isSame(numerator, denominator):
    actualSol = numerator/denominator
    numOnes = numerator%10
    numTens = (numerator - numOnes)/10
    denOnes = denominator%10
    denTens = (denominator - denOnes)/10
    if numOnes == 0 or denOnes == 0:
        return 0
    if numOnes == denOnes:
        return numTens/denTens == actualSol
    if numOnes == denTens:
        return numTens/denOnes == actualSol
    if numTens == denOnes:
        return numOnes/denTens == actualSol
    if numTens == denTens:
        return numOnes/denOnes == actualSol
    return 0

print isSame(49, 98)
result = 1
for i in range(11,99):
    for j in range(10,i):
        if isSame(j,i):
            print str(j) + "/" + str(i)
            result *= j/i
print result
