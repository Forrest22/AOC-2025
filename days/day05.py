from typing import List, Tuple


def ingredient_database(
    input_data: str,
) -> Tuple[List[Tuple[int, int]], List[str]]:
    """
    extract the range of fresh ingredients into a dict,
    then aggregates the ingredient list and returns both
    """
    lines = input_data.splitlines()

    ingredient_ids_section = False
    fresh_ingredient_ranges = []
    ingredient_list = []

    for line in lines:
        if line == "":
            ingredient_ids_section = True
        elif ingredient_ids_section:
            ingredient_list.append(line)
        else:
            # if we're processing the fresh ingredient ranges, save the ranges into a list
            fresh_range = line.split("-")
            fresh_ingredient_ranges.append((int(fresh_range[0]), int(fresh_range[1])))
    return (fresh_ingredient_ranges, ingredient_list)


def count_fresh_ingredients(
    fresh_ingredient_ranges: List[Tuple[int, int]],
    ingredient_list: List[str],
) -> int:
    count = 0
    for ingredient in ingredient_list:
        for ingredient_range in fresh_ingredient_ranges:
            if ingredient_range[0] <= int(ingredient) <= ingredient_range[1]:
                count += 1
                break
    return count


def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day05.txt as a string.
    return: (part 1 answer)
    """
    fresh_ingredient_ranges, ingredient_list = ingredient_database(input_data)

    return count_fresh_ingredients(fresh_ingredient_ranges, ingredient_list)


def count_all_fresh_ingredient_ids(fresh_ingredient_ranges: List[Tuple[int, int]]) -> int:
    sorted_ingredient_ranges = sorted(fresh_ingredient_ranges)

    current = -1
    count = 0
    for start, end in sorted_ingredient_ranges:
        if current >= start:
            start = current + 1
        if start <= end:
            count += end - start + 1
        current = max(current, end)
    return count


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day05.txt as a string.
    return: (part 2 answer)
    """
    fresh_ingredient_ranges, _ = ingredient_database(input_data)

    return count_all_fresh_ingredient_ids(fresh_ingredient_ranges)
