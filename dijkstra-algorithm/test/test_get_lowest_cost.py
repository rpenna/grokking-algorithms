from functions import get_lowest_cost


def test_given_a_costs_hash_table_when_the_function_is_executed_then_it_should_return_the_lowest_cost_on_the_hash_table(
    book_initial_costs_hash_table_example,
):
    lowest_cost_vertex = get_lowest_cost(book_initial_costs_hash_table_example)
    assert lowest_cost_vertex == "b"
