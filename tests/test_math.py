import pytest
import pymorphic.math


def test_add():
    assert pymorphic.math.add(2, 3) == 5
    assert pymorphic.math.add(-1, 1) == 0
    assert pymorphic.math.add(0, 0) == 0
