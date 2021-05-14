from Node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def print(self):
        if self.head is None:
            print('List has 0 Node')
            return
        n = self.head
        nodes_text = ''
        while n is not None:
            nodes_text += f' {n.item} -'
            n = n.next
        print(f"[{nodes_text.rstrip(' -')} ]")

    def traverse(self, index):
        node = self.head
        for i in range(self.length):
            if(i == index):
                return node
            node = node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.length += 1
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        if self.length == 0:
            print('Please use append function.')
            return
        if index == 0:
            self.prepend(data)
            return
        if index >= self.length or index < 0:
            print('Index out of range')
            return
        if (index == self.length-1):
            return self.append(data)
        n = self.head
        for i in range(1, self.length-1):
            if(i == index):
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
                self.length += 1

    def insert_after(self, x, data):
        curr = self.head
        if curr is None:
            print('List is empty')
            return
        while curr is not None:
            if curr.item == x:
                new_node = Node(data)
                new_node.next = curr.next
                curr.next = new_node
                self.length += 1
                return
            curr = curr.next
        if curr is None:
            print(f'Node {x} is not found.')

    def remove_at(self, index):  # maybe need nextactoring like below remove func
        if self.head is None:
            print('List is empty')
            return
        if(index >= self.length):
            print('Index out of range')
            return
        if(index == 0):
            self.head = self.head.next
            self.length -= 1
            return
        n = self.head
        for i in range(self.length):
            if(i+1 == index):
                n.next = n.next.next
                self.length -= 1
                return
            n = n.next

    def remove(self, x):
        if(self.head.item == x):
            self.head = self.head.next
            self.length -= 1
            return
        prev = self.head
        curr = prev.next
        while curr is not None:
            if(curr.item == x):
                prev.next = curr.next
                self.length -= 1
                return
            prev = curr
            curr = curr.next
        print(f'{x} item is not found')

    def reverse(self):
        prev = self.head
        curr = prev.next
        prev.next = None
        while curr is not None:
            next = curr.next

            curr.next = prev

            prev = curr
            curr = next
        self.head = prev
