def set_costs(graph: dict, initial_vertex: str) -> dict:
    costs = dict()
    for vertex, cost in graph[initial_vertex].items():
        costs[vertex] = cost
    for vertex in graph.keys():
        if vertex not in costs:
            costs[vertex] = float('inf')
    return costs


def set_parents(costs: dict, parent: str) -> dict:
    parents = dict()
    for vertex, cost in costs.items():
        if cost < float("inf"):
            parents[vertex] = parent
        else:
            parents[vertex] = None
    return parents


def get_lowest_cost(costs: dict) -> str:
    lowest_cost = float("inf")
    lowest_vertex = None
    for vertex, cost in costs.items():
        if cost < lowest_cost:
            lowest_cost = cost
            lowest_vertex = vertex
    return lowest_vertex