from Stack import *

text = "Some string."
reversedText = ""

myStack = Stack()

for i in range(len(text)):
    myStack.push(text[i])

for i in range(myStack.size()):
    reversedText = reversedText + myStack.pop()

print(reversedText)