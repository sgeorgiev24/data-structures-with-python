from Stack import *


def decToBin(decNum):
    binString = ""
    remStack = Stack()

    while decNum > 0:
        rem = decNum % 2
        remStack.push(rem)
        decNum = decNum // 2

    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())

    return binString


print(decToBin(2))
