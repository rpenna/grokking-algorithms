from functions import set_costs, set_parents, get_lowest_cost


def dijkstra_algorithm(graph: dict) -> int:
    costs = set_costs(graph, "start")
    node = get_lowest_cost(costs)
    parents = set_parents(costs, node)
    processed = []
    while node:
        cost = costs[node]
        edges = graph[node]
        for next_node in edges.keys():
            new_cost = cost + edges[next_node]
            if costs[next_node] > new_cost:
                costs[next_node] = new_cost
                parents[next_node] = node
        processed.append(node)
        node = get_lowest_cost(costs, processed)
    return costs["end"]
