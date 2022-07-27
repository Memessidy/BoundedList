class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    # Get methods
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    # Set methods
    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        cur_node = self.head

        if cur_node is None:
            self.head = new_node
            return

        while cur_node.get_next():
            cur_node = cur_node.get_next()

        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
        output = ''

        while cur_node:
            output += str(cur_node.get_data()) + ' -> '
            cur_node = cur_node.get_next()

        print(output)

    def length(self):
        cur_node = self.head
        count = 0

        while cur_node:
            count += 1
            cur_node = cur_node.get_next()
        print(count)

    def push_front(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node

    def remove_back(self):
        cur_node = self.head

        while cur_node.get_next().get_next():
            cur_node = cur_node.get_next()
        cur_node.set_next(None)

    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_next()

    def value_at(self, index):
        cur_node = self.head
        count = 0

        while cur_node:
            if count == index:
                return cur_node.get_data()

            count += 1
            cur_node = cur_node.get_next()
        print("Index is out of range")

    def insert(self, index, data):
        new_node = Node(data)
        cur_node = self.head

        count = 0

        while cur_node.get_next():
            if index == 0:
                self.push_front(data)
                return
            elif count + 1 == index:
                the_node_after_curr = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_curr)
                return
            count += 1
            cur_node = cur_node.get_next()
        print("Index is out of range!")

    def remove(self, index):
        cur_node = self.head

        count = 0

        while cur_node.get_next():
            if index == 0:
                self.remove_front()
                return
            elif count + 1 == index:
                the_node_to_remove = cur_node.get_next()
                the_node_after_removed = the_node_to_remove.get_next()
                cur_node.set_next(the_node_after_removed)
                return
            count += 1
            cur_node = cur_node.get_next()
        print("Index is out of range!")

    def reverse(self):
        prev = None
        cur_node = self.head
        next = None

        while cur_node:
            next = cur_node.get_next()
            cur_node.set_next(prev)
            prev = cur_node
            cur_node = next
        self.head = prev