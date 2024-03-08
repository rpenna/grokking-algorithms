from functions import set_parents


def test_given_book_initial_costs_hash_table_example_when_creating_initial_parents_hash_table_then_it_should_return_the_expected_values(
    book_initial_costs_hash_table_example, book_initial_parents_hash_table_example
):
    parents = set_parents(book_initial_costs_hash_table_example, "start")
    for vertex in ["a", "b", "end"]:
        assert parents[vertex] == book_initial_parents_hash_table_example[vertex]
