# Graph implementation
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

# Costs
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['meta'] = float('inf')

# Parents
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['meta'] = None

# Processed
processed = {}

# Dijkstra algorythm implementation


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


for element in zip(graph.keys(), graph.values()):
    print(element)
for element in zip(costs.keys(), costs.values()):
    print(element)
for element in zip(parents.keys(), parents.values()):
    print(element)


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed[node] = True
    node = find_lowest_cost_node(costs)
print('FINISHED')


for element in zip(graph.keys(), graph.values()):
    print(element)
for element in zip(costs.keys(), costs.values()):
    print(element)
for element in zip(parents.keys(), parents.values()):
    print(element)
for element in zip(processed.keys(), processed.values()):
    print(element)


