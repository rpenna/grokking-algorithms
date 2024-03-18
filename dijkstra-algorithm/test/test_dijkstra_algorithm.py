import pytest
from dijkstra_algorithm import dijkstra_algorithm


@pytest.mark.parametrize(
    "graph, expected", [("book_graph_example", 6), ("book_exercise_a_graph", 8)]
)
def test_given_a_graph_when_algorithm_is_executed_then_it_should_return_the_shortest_cost_to_the_end_node(
    graph, expected, request
):
    lowest_cost = dijkstra_algorithm(request.getfixturevalue(graph))
    assert lowest_cost == expected
