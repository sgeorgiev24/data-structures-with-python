from Dequeue import *


def palChecker(text):
    isEqual = True
    palDequeue = Dequeue()

    for ch in text:
        palDequeue.addFront(ch)

    while palDequeue.size() > 1 and isEqual:
        first = palDequeue.removeFront()
        last = palDequeue.removeRear()

        if first != last:
            isEqual = False

    return isEqual


print(palChecker("asesa"))
print(palChecker("asesa1"))
