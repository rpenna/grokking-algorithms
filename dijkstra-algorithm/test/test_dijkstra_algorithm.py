from dijkstra_algorithm import dijkstra_algorithm


def test_given_a_graph_when_algorithm_is_executed_then_it_should_return_the_shortest_cost_to_the_end_node(
    book_graph_example,
):
    lowest_cost = dijkstra_algorithm(book_graph_example)
    assert lowest_cost == 6
