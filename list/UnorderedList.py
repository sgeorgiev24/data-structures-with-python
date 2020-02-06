from Node import *


class UnorderedList:
    def __init__(self):
        self.head = None
        self.listSize = 0

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        if self.search(item):
            raise ValueError("The item is already in the list!")

        newItem = Node(item)
        newItem.setNext(self.head)
        self.head = newItem
        self.listSize = self.listSize + 1

    def size(self):
        return self.listSize

    def search(self, item):
        found = False
        current = self.head

        while current is None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        if current is None:
            raise ValueError("The list is empty!")

        while not found:
            if current.getData() == item:
                found = True
            else:
                if current.getNext() is None:
                    raise ValueError("Item not found!")

                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        self.listSize = self.listSize - 1

    def append(self, item):
        if self.search(item):
            raise ValueError("The item is already in the list!")

        if self.size() == 0:
            self.add(item)
            return

        lastItem = self.head
        while lastItem.getNext() is not None:
            lastItem = lastItem.getNext()

        newItem = Node(None)
        newItem.setData(item)
        lastItem.setNext(newItem)

        self.listSize = self.listSize + 1

    def insert(self, position, item):
        if self.search(item):
            raise ValueError("The item is already in the list!")

        if not isinstance(position, int):
            raise TypeError("Position must be integer!")

        if self.size() < position:
            raise IndexError("Index out of range!")

        counter = 0
        previous = Node(None)
        current = self.head

        while counter < position:
            counter = counter + 1
            previous = current
            current = current.getNext()

        newItem = Node(item)
        previous.setNext(newItem)
        newItem.setNext(current)

        self.listSize = self.listSize + 1

    def index(self, item):
        found = False
        current = self.head
        counter = 0

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                counter = counter + 1

        if not found:
            raise IndexError("Index out of range!")

        return counter

    def pop(self, index=None):
        counter = 0
        previous = None
        current = self.head
        index = index or self.size()-1

        if index > self.size()-1:
            raise IndexError("Index out of range!")

        while counter < index:
            previous = current
            current = current.getNext()
            counter = counter + 1

        previous.setNext(current.getNext())

    def __str__(self):
        listString = ""
        current = self.head

        while True:
            listString = listString + str(current.getData()) + " "
            current = current.getNext()

            if current is None:
                break

        return listString
