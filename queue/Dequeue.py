class Dequeue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def removeFront(self):
        if len(self.items) == 0:
            raise IndexError("Dequeue is already empty!")

        return self.items.pop()

    def addRear(self, item):
        self.items.insert(0, item)

    def removeRear(self):
        if len(self.items) == 0:
            raise IndexError("Dequeue is already empty!")

        return self.items.pop(0)
