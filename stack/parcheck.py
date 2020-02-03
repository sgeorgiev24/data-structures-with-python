# Check if parentheses are balanced. Balanced parentheses means that each
# opening symbol has a corresponding closing symbol and the pairs of
# parentheses are properly nested.

from Stack import *


def parChecker(text):
    myStack = Stack()
    balanced = True

    for i in range(len(text)):
        if text[i] == '(':
            myStack.push(text[i])
        else:
            if myStack.isEmpty():
                balanced = False
                break

            myStack.pop()

    if not myStack.isEmpty():
        balanced = False

    return balanced

print(parChecker("()()((())))"))
print(parChecker("()()((()))"))