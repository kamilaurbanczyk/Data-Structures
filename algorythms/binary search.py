import timeit


def binary_search(num_list, target):
    min_index = 0
    max_index = len(num_list) - 1
    guess = round((min_index + max_index)/2)
    tries = 1
    while num_list[guess] != target:
        if num_list[guess] > target:
            max_index = guess - 1
        else:
            min_index = guess + 1
        guess = round((min_index + max_index)/2)
        tries += 1
    return (guess, tries)


def linear_search(num_list, target):
    tries = 0
    for i in range(len(num_list)):
        tries += 1
        if num_list[i] == target:
            return (i, tries)


my_list = [n**3 for n in range(100)]
target = 941192

bin_result = binary_search(my_list, target)
lin_result = linear_search(my_list, target)
built_in_result = my_list.index(target)

bin_func_time = timeit.timeit("binary_search(my_list, target )", "from __main__ import binary_search, my_list, target",
                              number = 10000 )
lin_func_time = timeit.timeit("linear_search(my_list, target )", "from __main__ import linear_search, my_list, target",
                              number = 10000 )
built_in_func_time = timeit.timeit('my_list.index(target)',"from __main__ import my_list, target",
                                   number = 10000  )

print('Binary Search:\nIndex of {}: {}. Number of tries: {}'.format(target, bin_result[0], bin_result[1]))
print('Binary func time: {}'.format(bin_func_time))

print('\nLinear Search:\nIndex of {}: {}. Number of tries: {}'.format(target, lin_result[0], lin_result[1]))
print("Linear func time: {}".format(lin_func_time))

print('\nIndex func Search:\nIndex of {}: {}.'.format(target, built_in_result))
print('Index func time: {}'.format(built_in_func_time))