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
def book_initial_costs_hash_table_example():
    return {"a": 6, "b": 2, "end": float("inf")}


@pytest.fixture
def book_initial_parents_hash_table_example():
    return {"a": "start", "b": "start", "end": None}
