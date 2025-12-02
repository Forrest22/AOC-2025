def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day02.txt as a string.
    return: (part 1 answer)
    """
    line = input_data.splitlines()[0]

    ranges = line.split(",")
    rangeTuples = list()

    for productIDRange in ranges:
        start, end = productIDRange.split("-")
        rangeTuples.append((int(start), int(end)))

    listOfInvalidIDs = []
    for pidRangeTuple in rangeTuples:
        for i in range(pidRangeTuple[0], pidRangeTuple[1] + 1):
            if isInvalidIDPart1(i):
                listOfInvalidIDs.append(i)

    return sum(listOfInvalidIDs)


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day02.txt as a string.
    return: (part 2 answer)
    """
    line = input_data.splitlines()[0]

    ranges = line.split(",")
    rangeTuples = list()

    for productIDRange in ranges:
        start, end = productIDRange.split("-")
        rangeTuples.append((int(start), int(end)))

    listOfInvalidIDs = []
    for pidRangeTuple in rangeTuples:
        for i in range(pidRangeTuple[0], pidRangeTuple[1] + 1):
            if isInvalidIDPart2(i):
                listOfInvalidIDs.append(i)

    return sum(listOfInvalidIDs)


def isInvalidIDPart1(i: int) -> bool:
    iStr = str(i)
    firstpart, secondpart = iStr[: len(iStr) // 2], iStr[len(iStr) // 2 :]
    if firstpart == secondpart:
        return True
    return False


def isInvalidIDPart2(i: int) -> bool:
    iStr = str(i)
    factors = find_factors(len(iStr))[1:]

    for factor in factors:
        if factor == 1:
            break
        else:
            part_size = len(iStr) // factor
            parts = [iStr[i * part_size : (i + 1) * part_size] for i in range(factor)]

            if len(set(parts)) == 1:
                return True

    return False


def find_factors(number) -> list[int]:
    if not isinstance(number, int) or number <= 0:
        return

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
