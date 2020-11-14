graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['meta'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['meta'] = 5
graph['meta'] = {}

for element in zip(graph.keys(), graph.values()):
    print(element)