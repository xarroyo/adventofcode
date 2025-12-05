
def is_in_range(value: int, r: tuple[int, int]) -> bool:
    return r[0] <= value <= r[1]

def is_overlapping(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return not (a[1] < b[0] or b[1] < a[0])

def merge_ranges(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (min(a[0], b[0]), max(a[1], b[1]))

def merge_overlapping_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]
    for current in sorted_ranges[1:]:
        last = merged[-1]
        if is_overlapping(current, last):
            merged[-1] = merge_ranges(current, last)
        else:
            merged.append(current)

    return merged