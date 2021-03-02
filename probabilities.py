import functools
import itertools
import operator


def _validate_probabilities(events):
    return all(map(lambda x: x>=0 and x<=1, events))


def _complement(events):
    return list(map(lambda x: 1-x, events))


def no_events(events):
    """Return probability that none of the events occur"""
    return functools.reduce(operator.mul, _complement(events))


def all_events(events):
    """Return probability that all of the events occur"""
    return functools.reduce(operator.mul, events)


def at_least_one(events):
    """Given a list of probabilities, return the probability that at least one event occurred"""
    if _validate_probabilities(events):
        return 1 - no_events(events)
    else:
        raise TypeError(f'Events contains an invalid probability: {events}')


def only_one(events):
    """Given a list of event probabilities, return the probability that only one event occurs"""
    complements = _complement(events)
    complements.reverse()
    complement_products = itertools.starmap(
        operator.mul,
        itertools.combinations(complements, len(events)-1)
    )
    return sum(map(operator.mul, events, complement_products))