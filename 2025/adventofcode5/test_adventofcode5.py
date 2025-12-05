import pytest
from adventofcode5 import clean_inventory, fresh_ingredient_ranges, is_fresh

data = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
]
inventory = [ (int(x.split("-")[0]), int(x.split("-")[1])) for x in data]

def test_is_fresh():
    assert not is_fresh(1, inventory)[0]
    assert is_fresh(5, inventory)[0]
    assert not is_fresh(8, inventory)[0]
    assert is_fresh(11, inventory)[0]
    assert is_fresh(17, inventory)[0]
    assert not is_fresh(32, inventory)[0]

def test_fresh_ingredient_ranges():
    new_inventory = clean_inventory(inventory)
    assert fresh_ingredient_ranges(new_inventory) == 14

def test_unify_ranges():
    assert clean_inventory(inventory) == [(3, 5), (10, 20)]