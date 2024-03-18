import pytest
from functions import set_costs


@pytest.mark.parametrize(
    "graph, costs",
    [
        ("book_graph_example", "book_initial_costs_hash_table_example"),
        ("book_exercise_a_graph", "book_exercise_a_initial_costs_hash_table"),
        ("book_exercise_b_graph", "book_exercise_b_initial_costs_hash_table"),
    ],
)
def test_given_book_example_graph_when_building_const_graph_from_starting_vertex_then_it_should_return_expected_costs_graph(
    graph, costs, request
):
    graph_fixture = request.getfixturevalue(graph)
    costs_fixture = request.getfixturevalue(costs)
    costs_graph = set_costs(graph_fixture, "start")
    for vertex in costs_fixture.keys():
        assert costs_graph[vertex] == costs_fixture[vertex]
