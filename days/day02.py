from typing import List, Tuple


def parse_ranges(input_data: str) -> List[Tuple[int, int]]:
    """
    extract (start, end) integer tuples from the first line of input.
    """
    line = input_data.splitlines()[0]
    return [
        (int(start), int(end)) for start, end in (r.split("-") for r in line.split(","))
    ]


def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day02.txt as a string.
    return: (part 1 answer)
    """
    id_ranges = parse_ranges(input_data)

    list_of_invalid_ids = []
    for pid_range_tuple in id_ranges:
        for product_id in range(pid_range_tuple[0], pid_range_tuple[1] + 1):
            if is_invalid_id_part1(product_id):
                list_of_invalid_ids.append(product_id)

    return sum(list_of_invalid_ids)


def is_invalid_id_part1(product_id: int) -> bool:
    """
    determines if a string is invalid for part 1.
    if a number is two repeated strings, its invalid.
    """
    id_string = str(product_id)
    first_part, second_part = (
        id_string[: len(id_string) // 2],
        id_string[len(id_string) // 2 :],
    )
    if first_part != second_part:
        return False
    return True


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day02.txt as a string.
    return: (part 2 answer)
    """
    id_ranges = parse_ranges(input_data)

    list_of_invalid_ids = []
    for pid_range_tuple in id_ranges:
        for i in range(pid_range_tuple[0], pid_range_tuple[1] + 1):
            if is_invalid_id_part_2(i):
                list_of_invalid_ids.append(i)

    return sum(list_of_invalid_ids)


def is_invalid_id_part_2(product_id: int) -> bool:
    """
    determines if a string is invalid for part 2.
    if a number is any number of repeated strings, its invalid.
    """
    id_string = str(product_id)

    # removing the first element in the array
    # (it will always be the integer `1`, which we can ignore)
    factors = find_factors(len(id_string))[1:]

    for factor in factors:
        part_size = len(id_string) // factor
        parts = [id_string[i * part_size : (i + 1) * part_size] for i in range(factor)]

        # if all the items in the list are equal (repeated digits)
        if len(set(parts)) == 1:
            return True

    return False


def find_factors(number) -> List[int]:
    """
    finds the factors of a number,
    helpful for finding how many repeating string segments a number can be split into
    """
    if not isinstance(number, int) or number <= 0:
        return []

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
