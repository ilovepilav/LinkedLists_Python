from Node import Node


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def traverse(self):
        if self.head is None:
            return print('List has 0 Node')
        n = self.head
        while n is not None:
            print(f'{n.item} ')
            n = n.ref

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        if self.length == 0:
            print('Please use append function.')
            return
        if index == 0:
            self.prepend(data)
            return
        if index >= self.length:
            print('Index out of range')
            return
        n = self.head.ref
        for i in range(1, self.length):
            if(i != index):
                n = n.ref
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    def insert_after(self, x, data):
        curr = self.head
        if curr is None:
            print('List is empty')
            return
        while curr is not None:
            if curr.item == x:
                new_node = Node(data)
                new_node.ref = curr.ref
                curr.ref = new_node
                self.length += 1
                return
            curr = curr.ref
        if curr is None:
            print(f'Node {x} is not found.')

    def delete_at_index(self, index):  # maybe need refactoring like below delete func
        if self.head is None:
            print('List is empty')
            return
        if(index >= self.length):
            print('Index out of range')
            return
        if(index == 0):
            self.head = self.head.ref
            self.length -= 1
            return
        n = self.head
        for i in range(self.length):
            if(i+1 == index):
                n.ref = n.ref.ref
                self.length -= 1
                return
            n = n.ref

    def delete(self, x):
        if(self.head.item == x):
            self.head = self.head.ref
            self.length -= 1
            return
        prev = self.head
        curr = prev.ref
        while curr is not None:
            if(curr.item == x):
                prev.ref = curr.ref
                self.length -= 1
                return
            prev = curr
            curr = curr.ref
        print(f'{x} item is not found')

    def reverse(self):
        prev = self.head
        curr = prev.ref
        next = curr.ref
        prev.ref = None
        while curr is not None:
            # Changes pointers
            curr.ref = prev
            # Moves next node
            prev = curr
            curr = next
            next = next.ref if next is not None else None
        self.head = prev
