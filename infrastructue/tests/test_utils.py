from infrastructue.utils import (is_in_range, is_overlapping,
                                 merge_overlapping_ranges, merge_ranges)


def tests_is_in_range():
    assert is_in_range(3, (3, 5))
    assert is_in_range(4, (3, 5))
    assert is_in_range(5, (3, 5))
    assert not is_in_range(2, (3, 5))
    assert not is_in_range(6, (3, 5))

def tests_is_overlapping():
    assert is_overlapping((3, 5), (4, 6))
    assert is_overlapping((4, 6), (3, 5))
    assert is_overlapping((1, 10), (3, 5))
    assert is_overlapping((3, 5), (1, 10))
    assert not is_overlapping((6, 8), (3, 5))
    assert not is_overlapping((3, 5), (6, 8))

def tests_merge_ranges():
    assert merge_ranges((3, 5), (4, 6)) == (3, 6)
    assert merge_ranges((1, 10), (3, 5)) == (1, 10)
    assert merge_ranges((3, 5), (1, 10)) == (1, 10)
    assert merge_ranges((6, 8), (3, 5)) == (3, 8)
    assert merge_ranges((3, 5), (6, 8)) == (3, 8)

def tests_merge_overlapping_ranges():
    assert merge_overlapping_ranges([(3, 5), (4, 6)]) == [(3, 6)]
    assert merge_overlapping_ranges([(5, 8), (4, 6)]) == [(4, 8)]
    assert merge_overlapping_ranges([(3, 5), (1, 10)]) == [(1, 10)]
    assert merge_overlapping_ranges([(3, 5), (6, 8)]) == [(3, 5), (6, 8)]