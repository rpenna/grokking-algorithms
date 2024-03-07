import pytest
from functions import set_costs


@pytest.fixture
def book_graph_example():
    return {
        'start': {
            'a': 6,
            'b': 2
        },
        'a': {
            'end': 1
        },
        'b': {
            'a': 3,
            'end': 5
        },
        'end': {}
    }


@pytest.fixture
def expected_book_example_costs_graph():
    return {
        'a': 6,
        'b': 2,
        'end': float('inf')
    }


def test_given_book_example_graph_when_building_const_graph_from_starting_vertex_then_it_should_return_expected_costs_graph(book_graph_example, expected_book_example_costs_graph):
    costs_graph = set_costs(book_graph_example, 'start')
    assert costs_graph['a'] == expected_book_example_costs_graph['a']
    assert costs_graph['b'] == expected_book_example_costs_graph['b']
    assert costs_graph['end'] == expected_book_example_costs_graph['end']
