class UnorderedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        newItem = Node(item)
        newItem.setNext(self.head)
        self.head = newItem
        self.size = self.size + 1

    def size(self):
        return self.size

    def search(self, item):
        found = False
        current = self.head

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
