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


@pytest.fixture
def book_exercise_a_graph():
    return {
        "start": {"a": 5, "b": 2},
        "a": {"c": 4, "d": 2},
        "b": {"a": 8, "d": 7},
        "c": {"d": 6, "end": 3},
        "d": {"end": 1},
        "end": {},
    }


@pytest.fixture
def book_exercise_a_initial_costs_hash_table():
    return {"a": 5, "b": 2, "c": float("inf"), "d": float("inf"), "end": float("inf")}


@pytest.fixture
def book_exercise_a_initial_parents_hash_table():
    return {"a": "start", "b": "start", "c": None, "d": None, "end": None}


@pytest.fixture
def book_exercise_b_graph():
    return {
        "start": {"a": 10},
        "a": {"b": 20},
        "b": {"c": 1, "end": 30},
        "c": {"a": 1},
        "end": {},
    }


@pytest.fixture
def book_exercise_b_initial_costs_hash_table():
    return {"a": 10, "b": float("inf"), "c": float("inf"), "end": float("inf")}


@pytest.fixture
def book_exercise_b_initial_parents_hash_table():
    return {"a": "start", "b": None, "c": None, "end": None}
