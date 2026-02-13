from typing import List, Tuple, DefaultDict
from collections import defaultdict


def parse_red_tiles(input_data: str) -> List[Tuple[int, int]]:
    red_tiles: List[Tuple[int, int]] = []
    for line in input_data.splitlines():
        coords = map(int, line.split(","))
        red_tiles.append(tuple(coords))
    return red_tiles


def calculate_result_part1(tile_map: List[Tuple[int, int]]) -> int:
    largest_area = 0
    for i, coordinate_a in enumerate(tile_map):
        for _, coordinate_b in enumerate(tile_map, start=i + 1):
            area = calculate_area(coordinate_a, coordinate_b)
            if area > largest_area:
                largest_area = area

    return largest_area


def calculate_area(coordinate_a: Tuple[int, int], coordinate_b: Tuple[int, int]) -> int:
    x1, y1 = coordinate_a
    x2, y2 = coordinate_b
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day09.txt as a string.
    return: (part 1 answer)
    """
    red_tiles = parse_red_tiles(input_data)
    return calculate_result_part1(red_tiles)


def are_coords_in_red_and_green(
    coordinate_a: Tuple[int, int],
    coordinate_b: Tuple[int, int],
) -> bool:
    # for each coordinate in the square
    return False


green_coordinates: DefaultDict[Tuple[int, int], bool] = defaultdict()


def create_green_tile_map(
    red_tile_coords: List[Tuple[int, int]],
) -> DefaultDict[Tuple[int, int], bool]:
    prev_x, prev_y = (None, None)
    for i in enumerate(red_tile_coords):
        # check what direction the line went
        current_x, current_y = red_tile_coords[i]
        if i == 0:
            pass
        elif current_y != prev_y:
            # move on y axis
            if current_y > prev_y:
                for j in range(prev_y, current_y):
                    green_coordinates[(current_x, current_y + j)] = True
            else:
                for j in range(current_y, prev_y):
                    green_coordinates[(current_x, current_y + j)] = True
        else:
            # move on x axis
            if current_x > prev_x:
                for j in range(prev_x, current_x):
                    green_coordinates[(current_x + j, current_y)] = True
            else:
                for j in range(current_x, prev_x):
                    green_coordinates[(current_x + j, current_y)] = True
        prev_x, prev_y = red_tile_coords[i]
    return green_coordinates


def calculate_result_part2(
    red_coords: List[Tuple[int, int]],
) -> int:
    largest_area = 0
    for i, coordinate_a in enumerate(red_coords):
        for _, coordinate_b in enumerate(red_coords, start=i + 1):
            area = calculate_area(coordinate_a, coordinate_b)
            if area > largest_area and are_coords_in_red_and_green(
                coordinate_a, coordinate_b
            ):
                largest_area = area

    return largest_area


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day09.txt as a string.
    return: (part 2 answer)
    """
    # TODO: Implement
    # red_tile_coords = parse_red_tiles(input_data)
    # green_tile_map = create_green_tile_map(red_tile_coords)
    # return calculate_result_part2(red_tile_coords, green_tile_map)
    return -1
