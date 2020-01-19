#!/usr/bin/env python3

import random

def generateString(stringLen):
    res = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz "

    for i in range(stringLen):
        res += alphabet[random.randrange(27)]

    return res

def score(goal, testString):
    numSame = 0
    
    for i in range(len(goal)):
        if goal[i] == testString[i]:
            numSame += 1
    
    return numSame / len(goal) * 100


def main():
    goal = "methinks it is like a weasel"
    testString = generateString(len(goal))
    newScore = score(goal, testString)
    best = 0
    
    while newScore < 100:
        if newScore >= best:
            best = newScore
            print("%.1f%% => %s" % (newScore, testString))
        testString = generateString(len(goal))
        newScore = score(goal, testString)

main()
