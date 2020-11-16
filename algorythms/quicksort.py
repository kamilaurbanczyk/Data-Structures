import random


def quicksort(array):
    """

    :type array: list
    """
    if len(array) < 2:
        return array
    else:
        pivot_index = random.randint(0, len(array)-1)
        pivot = array[pivot_index]
        array.pop(pivot_index)
        less = [i for i in array if i <= pivot]
        grater = [i for i in array if i > pivot]
        return quicksort(less) + [pivot] + quicksort(grater)


my_array = [34, 56, 12, 23, 9, 8, 7, 10, 309, 572, 111, 35, 3, 23, 20, 999]

print(quicksort(my_array))