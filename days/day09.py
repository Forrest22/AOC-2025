from typing import List, Tuple, DefaultDict
from collections import defaultdict


def parse_red_tiles(inputData: str) -> List[Tuple[int, int]]:
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


def are_coords_in_red_and_green(
    coordinateA: Tuple[int, int],
    coordinateB: Tuple[int, int],
) -> bool:
    # print(coordinateA, coordinateB)
    # for each coordinate in the square
    return False


greenCoordinates: DefaultDict[Tuple[int, int], bool] = defaultdict()


def create_green_tile_map(
    redTileCoords: List[Tuple[int, int]],
) -> DefaultDict[Tuple[int, int], bool]:
    prevX, prevY = (None, None)
    for i in range(len(redTileCoords)):
        # check what direction the line went
        currentX, currentY = redTileCoords[i]
        if i == 0:
            pass
        elif currentY != prevY:
            # move on y axis
            if currentY > prevY:
                for j in range(prevY, currentY):
                    greenCoordinates[(currentX, currentY + j)] = True
            else:
                for j in range(currentY, prevY):
                    greenCoordinates[(currentX, currentY + j)] = True
        else:
            # move on x axis
            if currentX > prevX:
                for j in range(prevX, currentX):
                    greenCoordinates[(currentX + j, currentY)] = True
            else:
                for j in range(currentX, prevX):
                    greenCoordinates[(currentX + j, currentY)] = True
        prevX, prevY = redTileCoords[i]
    return greenCoordinates


def calculate_result_part2(
    redCoords: List[Tuple[int, int]],
) -> int:
    largestArea = 0
    for i, coordinateA in enumerate(redCoords):
        for j, coordinateB in enumerate(redCoords, start=(i + 1)):
            area = calculate_area(coordinateA, coordinateB)
            if area > largestArea and are_coords_in_red_and_green(
                coordinateA, coordinateB
            ):
                largestArea = area

    return largestArea


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day09.txt as a string.
    return: (part 2 answer)
    """
    redTileCoords = parse_red_tiles(inputData)
    greenTileMap = create_green_tile_map(redTileCoords)
    return calculate_result_part2(redTileCoords, greenTileMap)
