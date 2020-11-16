from collections import deque

# Ex. 1 - Find a person in a group of people.
graph = {}
graph['ty'] = ['bartek', 'cecylia', 'alicja']
graph['bartek'] = ['janusz', 'patrycja']
graph['alicja'] = ['patrycja']
graph['cecylia'] = ['tamara', 'jarek']
graph['janusz'] = []
graph['patrycja'] = []
graph['tamara'] = []
graph['jarek'] = []


def find_person(name):
    return name[-2] == 'e'


def breadth_first_search(graph, start):
    processed = []
    search_deque = deque()
    search_deque += graph[start]
    while search_deque:
        person = search_deque.popleft()
        if person not in processed:
            if find_person(person):
                return person
            else:
                search_deque += graph[person]
                processed.append(person)
    return False


result = breadth_first_search(graph, 'ty')
print(result)


# Ex.2 - Find the quickest route

