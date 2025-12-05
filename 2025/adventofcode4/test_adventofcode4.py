import pytest
from adventofcode4 import count_adjacent_rolls, forkliftrolls, has_less_than_4

data = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]

result = [
    "..xx.xx@x.",
    "x@@.@.@.@@",
    "@@@@@.x.@@",
    "@.@@@@..@.",
    "x@.@@@@.@x",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "x.@@@.@@@@",
    ".@@@@@@@@.",
    "x.x.@@@.x.",
]

def test_count_adjacent_rolls():
    matrix = [list(x) for x in data]
    assert count_adjacent_rolls(matrix, 0, 0) == 2
    assert count_adjacent_rolls(matrix, 2, 2) == 6
    assert count_adjacent_rolls(matrix, 9, 9) == 2



def test_forklifttrolls():
    matrix = [list(x) for x in data]
    rolls, new_state = forkliftrolls([list(l) for l in data])
    assert rolls == 43

