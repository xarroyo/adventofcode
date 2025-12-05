from infrastructue.files import read_file_to_list
from infrastructue.utils import is_in_range, merge_overlapping_ranges


def is_fresh(value: int, inventory: list) -> bool:
    return any(is_in_range(value, i) for i in inventory)

def clean_inventory(inventory):
    tuples = [tuple(r) if isinstance(r, list) else r for r in inventory]
    return merge_overlapping_ranges(tuples)


def fresh_ingredient_ranges(inventory):
    return sum(r[1] - r[0] + 1 for r in inventory)


if __name__ == "__main__":
    data = read_file_to_list("2025/adventofcode5/input.txt")

    inventory = [ (int(x.split("-")[0]), int(x.split("-")[1])) for x in data if "-" in x]
    ingredients = [int(x) for x in data if x and "-" not in x]

    # Part 1
    print(sum( is_fresh(ingredient, inventory) for ingredient in ingredients))

    # Part 2
    merged_inventory = clean_inventory(inventory)
    print(fresh_ingredient_ranges(merged_inventory))
