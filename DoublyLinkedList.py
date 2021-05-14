from Node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def traverse(self, index):
        node = self.head
        for i in range(self.length):
            if(i == index):
                return node
            node = node.next

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

    def append(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def prepend(self, data):
        if(self.head is None):
            print('List has 0 Node')
            return
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        if(self.head is None):
            print('List has 0 Node')
            return
        if(index >= self.length or index < 0):
            print(f'Index out of range.')
            return
        if(index == 0):
            return self.prepend(data)
        if(index == self.length-1):
            return self.append(data)
        n = self.head
        for i in range(1, self.length-1):
            if(i == index):
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                n.next.prev = new_node
                n.next = new_node
                self.length += 1
                return
            n = n.next

    def insert_after(self, x, data):
        n = self.head
        while n is not None:
            if(n.item == x):
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                n.next.prev = new_node
                n.next = new_node
                self.length += 1
                return
            n = n.next

    def remove_at(self, index):
        if(self.head is None):
            print('List has 0 Node.')
            return
        if(index >= self.length):
            print('Index out of range.')
            return
        if(index == 0):
            new_head = self.head.next
            self.head.next.prev = None
            self.head.next = None
            self.head = new_head
            self.length -= 1
            return
        if(index == self.length-1):
            new_tail = self.tail.prev
            self.tail.prev = None
            new_tail.next = None
            self.tail = new_tail
            self.length -= 1
            return
        follower = self.head
        leader = follower.next.next
        for i in range(1, self.length - 1):
            if(i == index):
                leader.prev.prev = None
                follower.next.next = None
                follower.next = leader
                leader.prev = follower
                self.length -= 1
                return
            follower = follower.next
            leader = leader.next