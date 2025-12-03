import pytest

from .adventofcode3 import *

test_data = [
    987654321111111,
    811111111111119,
    234234234234278,
    818181911112111,
]

def test_adventofcode3():
    result = joltage(test_data)
    assert result == 3121910778619

def test_max_joltage_per_battery():
    assert max_batery_joltage(list(str(987654321111111))) == '987654321111'
    assert max_batery_joltage(list(str(811111111111119))) == '811111111119'
    assert max_batery_joltage(list(str(234234234234278))) == '434234234278'
    assert max_batery_joltage(list(str(818181911112111))) == '888911112111'
