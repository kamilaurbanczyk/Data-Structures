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




