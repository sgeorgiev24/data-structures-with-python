class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError("Stack is already empty!")

        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("Stack is empty!")

        return self.items[len(self.items)]