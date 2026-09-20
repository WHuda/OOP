import pytest

from minicas.accumulator import Accumulator


def test_mean_and_count():
    acc = Accumulator.from_list([1, 2, 3])
    assert acc.count == 3
    assert acc.mean() == 2
    
def test_two_accumulators_are_independent():
    a, b = Accumulator(), Accumulator()
    a.add(10)
    assert b.count == 0
    
def test_mean_of_empty_raises():
    with pytest.raises(ValueError):
        Accumulator().mean()