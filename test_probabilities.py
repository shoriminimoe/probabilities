import probabilities as p

import pytest


def test_validate_probabilities_false():
    events = [-0.1, 1.7, 0.6]
    assert p._validate_probabilities(events) is False

def test_validate_probabilities_true():
    events = [0.5] * 3
    assert p._validate_probabilities(events) is True

def test_at_least_one():
    events = [0.5] * 3
    assert p.at_least_one(events) == 0.875

def test_at_least_one_exception():
    events = [-0.1, 1.7, 0.6]
    assert pytest.raises(TypeError, p.at_least_one, events)

@pytest.mark.parametrize(
    "events,expectation",
    [
        ([0.5] * 3, 0.375),
        ([0.1, 0.2, 0.3], 0.398),
    ]
)
def test_only_one(events, expectation):
    assert p.only_one(events) == expectation