from typing import List, Tuple


def parse_red_tiles(inputData: str) -> List:
    redTiles: List[Tuple[int, int]] = []
    for line in inputData.splitlines():
        coords = map(int, line.split(","))
        redTiles.append(tuple(coords))
    return redTiles


def calculate_result_part1(input: List[Tuple[int, int]]) -> int:
    largestArea = 0
    for i, coordinateA in enumerate(input):
        for j, coordinateB in enumerate(input, start=(i + 1)):
            area = calculate_area(coordinateA, coordinateB)
            if area > largestArea:
                largestArea = area

    return largestArea


def calculate_area(coordinateA: Tuple[int, int], coordinateB: Tuple[int, int]) -> int:
    x1, y1 = coordinateA
    x2, y2 = coordinateB
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def calculate_result_part1(input: List[Tuple[int, int]]) -> int:
    largestArea = 0
    for i, coordinateA in enumerate(input):
        for j, coordinateB in enumerate(input, start=(i + 1)):
            area = calculate_area(coordinateA, coordinateB)
            if area > largestArea:
                largestArea = area

    return largestArea


def solve_part1(inputData: str) -> int:
    """
    input_data: full contents of inputs/day09.txt as a string.
    return: (part 1 answer)
    """
    redTiles = parse_red_tiles(inputData)
    return calculate_result_part1(redTiles)


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day09.txt as a string.
    return: (part 2 answer)
    """
    boxes = parse_red_tiles(inputData)
    return calculate_result_part2(boxes)
