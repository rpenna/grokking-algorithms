import pytest


@pytest.fixture
def book_graph_example():
    return {
        "start": {"a": 6, "b": 2},
        "a": {"end": 1},
        "b": {"a": 3, "end": 5},
        "end": {},
    }


@pytest.fixture
def expected_book_example_costs_graph():
    return {"a": 6, "b": 2, "end": float("inf")}
