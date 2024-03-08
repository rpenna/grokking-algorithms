from functions import set_costs


def test_given_book_example_graph_when_building_const_graph_from_starting_vertex_then_it_should_return_expected_costs_graph(
    book_graph_example, book_initial_costs_hash_table_example
):
    costs_graph = set_costs(book_graph_example, "start")
    assert costs_graph["a"] == book_initial_costs_hash_table_example["a"]
    assert costs_graph["b"] == book_initial_costs_hash_table_example["b"]
    assert costs_graph["end"] == book_initial_costs_hash_table_example["end"]
