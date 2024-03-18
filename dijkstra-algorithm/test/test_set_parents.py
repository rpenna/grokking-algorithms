import pytest
from functions import set_parents


@pytest.mark.parametrize(
    "costs, parents",
    [
        (
            "book_initial_costs_hash_table_example",
            "book_initial_parents_hash_table_example",
        ),
        (
            "book_exercise_a_initial_costs_hash_table",
            "book_exercise_a_initial_parents_hash_table",
        ),
    ],
)
def test_given_book_initial_costs_hash_table_example_when_creating_initial_parents_hash_table_then_it_should_return_the_expected_values(
    costs, parents, request
):
    costs_fixture = request.getfixturevalue(costs)
    parents_fixture = request.getfixturevalue(parents)
    parents = set_parents(costs_fixture, "start")
    for vertex in parents_fixture.keys():
        assert parents[vertex] == parents_fixture.get(vertex)
