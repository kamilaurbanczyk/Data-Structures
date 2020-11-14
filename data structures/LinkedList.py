import random


class Node(object):
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1
        return True

    # Add element at n-th position
    def insert_at(self, data, n):
        this_node = self.head
        prev_node = None

        # Invalid position index
        if 1 > n or n > self.size + 1:
            return False

        if self.size == 0:
            if n == 1:
                new_node = Node(data)
                self.head = new_node
            else:
                return False

        else:
            for i in range(1, self.size + 1):
                if i == n:
                    this_node.set_data(data)
                    return True
                elif i < self.size:
                    this_node = this_node.get_next()
            new_node = Node(data)
            this_node.set_next(new_node)
            return True


    def remove(self, data):
        this_node = self.head
        prev_node = None

        while this_node is not None:
            if this_node.get_data() == data:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node.get_next
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, data):
        this_node = self.head

        while this_node is not None:
            if this_node.get_data() == data:
                return True
            else:
                this_node = this_node.get_next()
        return False


if __name__ == '__main__':

    mylist = LinkedList()
    mylist.add(23)
    mylist.add(3)
    mylist.add(18)
    mylist.add(21)
    mylist.add(7)
    mylist.add(0)
    mylist.add(10)
    print(mylist.get_size())
    this_node = mylist.head
    i = 1
    while this_node is not None:
        print(i, this_node.get_data())
        this_node = this_node.get_next()
        i += 1

    mylist.insert_at(0, 5)

    this_node = mylist.head
    i = 1
    print('\n')
    while this_node is not None:
        print(i, this_node.get_data())
        this_node = this_node.get_next()
        i += 1

    mylist2 = LinkedList()
    mylist2.insert_at(20,1)

    this_node = mylist2.head
    i = 1
    print('\n')
    while this_node is not None:
        print(i, this_node.get_data())
        this_node = this_node.get_next()
        i += 1

    print('\n')
    mylist3 = LinkedList()
    mylist3.add(23)
    mylist3.add(3)
    mylist3.add(18)
    print(mylist3.insert_at(33, -2))

    this_node = mylist3.head
    i = 1
    while this_node is not None:
        print(i, this_node.get_data())
        this_node = this_node.get_next()
        i += 1


