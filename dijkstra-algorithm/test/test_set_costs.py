import pytest
from functions import set_costs


@pytest.mark.parametrize(
    "graph, costs", [("book_graph_example", "book_initial_costs_hash_table_example")]
)
def test_given_book_example_graph_when_building_const_graph_from_starting_vertex_then_it_should_return_expected_costs_graph(
    graph, costs, request
):
    graph_fixture = request.getfixturevalue(graph)
    costs_fixture = request.getfixturevalue(costs)
    costs_graph = set_costs(graph_fixture, "start")
    assert costs_graph["a"] == costs_fixture["a"]
    assert costs_graph["b"] == costs_fixture["b"]
    assert costs_graph["end"] == costs_fixture["end"]
