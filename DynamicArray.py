import ctypes
import random


class DynamicArray(object):
    def __init__(self):
        self.n = 0  # number of elements in array, default = 0
        self.capacity = 1  # default = 1
        self.array = self.make_array(self.capacity)

    def __len__(self):
        """
        Returns number of elements in array
        """
        return self.n

    def __getitem__(self, index):
        """
        Returns element at index 'index'.
        """
        if 0 <= index < self.n:
            return self.array[index]
        else:
            return IndexError('Index is out of range!')

    def make_array(self, capacity):
        """
        Returns a new array with new capacity
        """
        return (capacity * ctypes.py_object)()

    def _resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, element):
        """
        Adds element at the end of an array
        """
        if len(self.array) == self.capacity:
            self._resize(self.capacity * 2)
        self.array[self.n] = element
        self.n += 1

    def delete(self):
        """
        Removes element from the end of an array.
        """
        if self.n == 0:
            return 'Deletion not possible, no elements in array.'
        self.array[self.n-1] = 0
        self.n -= 1
        return ''

    def insert_at(self, element, index):
        """
        Inserts element at specified index.
        """
        if 0 > index or index> self.n:
            return IndexError('Index is out of range!')

        if self.n == self.capacity:
            self.capacity = self.capacity * 2

        new_array = self.make_array(self.capacity)
        self.n += 1
        for i in range(0, index):
            new_array[i] = self.array[i]
        new_array[index] = element
        for i in range(index+1, self.n):
            new_array[i] = self.array[i-1]

        self.array = new_array

    def remove_at(self, index):
        """
        Deletes element from a specifies index.
        """
        new_array = self.make_array(self.capacity)
        for i in range(0, index):
            new_array[i] = self.array[i]
        for i in range(index, self.n-1):
            new_array[i]= self.array[i+1]

        self.n -= 1
        self.array = new_array


A = DynamicArray()

for i in range(20):
    A.append(random.randint(0, 345))

len(A)
for i in range(A.n):
    print(i, A[i])
A.insert_at(666, 14)

print(A[14])
print(A.n)

for i in range(A.n):
    print(i, A[i])

A.remove_at(17)

for i in range(A.n):
    print(i, A[i])



