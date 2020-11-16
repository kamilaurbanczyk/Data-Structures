
def selection_sort(array = list):
    sorted_array = []
    while array:
        min_index = 0
        for i in range(0, len(array)):
            if array[i] < array[min_index]:
                min_index = i
        sorted_array.append(array[min_index])
        array.pop(min_index)
    return sorted_array


array = [12, 9, 10, 7, 8, 4]

print(selection_sort(array))

