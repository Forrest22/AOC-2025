from typing import List, Tuple


def parse_ranges(inputData: str) -> List[Tuple[int, int]]:
    """
    Extract (start, end) integer tuples from the first line of input.
    """
    line = inputData.splitlines()[0]
    return [
        (int(start), int(end)) for start, end in (r.split("-") for r in line.split(","))
    ]


def solve_part1(inputData: str) -> int:
    """
    input_data: full contents of inputs/day02.txt as a string.
    return: (part 1 answer)
    """
    IdRanges = parse_ranges(inputData)

    listOfInvalidIDs = []
    for pidRangeTuple in IdRanges:
        for productID in range(pidRangeTuple[0], pidRangeTuple[1] + 1):
            if is_invalid_id_part1(productID):
                listOfInvalidIDs.append(productID)

    return sum(listOfInvalidIDs)


def is_invalid_id_part1(id: int) -> bool:
    """
    Determines if a string is invalid for part 1.
    If a number is two repeated strings, its invalid.
    """
    idString = str(id)
    firstPart, secondPart = (
        idString[: len(idString) // 2],
        idString[len(idString) // 2 :],
    )
    if firstPart != secondPart:
        return False
    return True


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day02.txt as a string.
    return: (part 2 answer)
    """
    IdRanges = parse_ranges(inputData)

    listOfInvalidIDs = []
    for pidRangeTuple in IdRanges:
        for i in range(pidRangeTuple[0], pidRangeTuple[1] + 1):
            if is_invalid_id_part_2(i):
                listOfInvalidIDs.append(i)

    return sum(listOfInvalidIDs)


def is_invalid_id_part_2(id: int) -> bool:
    """
    Determines if a string is invalid for part 2.
    If a number is any number of repeated strings, its invalid.
    """
    idString = str(id)

    # Removing the first element in the array (it will always be the integer `1`, which we can ignore)
    factors = find_factors(len(idString))[1:]

    for factor in factors:
        partSize = len(idString) // factor
        parts = [idString[i * partSize : (i + 1) * partSize] for i in range(factor)]

        # If all the items in the list are equal (repeated digits)
        if len(set(parts)) == 1:
            return True

    return False


def find_factors(number) -> list[int]:
    """
    Finds the factors of a number, helpful for finding how many repeating string segments a number can be split into
    """
    if not isinstance(number, int) or number <= 0:
        return

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
