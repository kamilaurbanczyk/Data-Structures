class Stack:
    def __init__(self):
        self.top_index = -1
        self.array = []
        self.size = 0

    def get_size(self):
        return self.size

    def get_top(self):
        if self.top_index < 0:
            return None
        return self.array[self.top_index]

    def push(self, data):
        self.array.append(data)
        self.top_index += 1
        self.size += 1
        return True

    def pop(self):
        if self.top_index < 0:
            return False
        popped = self.array[self.top_index]
        self.top_index -= 1
        self.size -= 1
        return popped


stack = Stack()
print(stack.get_size())
print(stack.get_top())
print(stack.push(2))
print(stack.push(13))
print(stack.push(7))
print(stack.push(20))
print(stack.get_size())
print(stack.get_top())
print(stack.pop())
print(stack.get_size())
print(stack.get_top())

