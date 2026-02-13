from typing import List

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def parse_paper_roll_diagram(input_data: str) -> List[str]:
    """
    extract the map of paper rolls.
    """
    lines = input_data.splitlines()
    return lines


def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day04.txt as a string.
    return: (part 1 answer)
    """
    paper_roll_map = parse_paper_roll_diagram(input_data)

    movable_rolls = 0
    for i, _ in enumerate(paper_roll_map):
        for j, _ in enumerate(paper_roll_map[0]):
            adjacent_count = 0
            if paper_roll_map[i][j] == "@":
                adjacent_count += count_adjacent_rolls(paper_roll_map, i, j)
                if adjacent_count < 4:
                    movable_rolls += 1

    return movable_rolls


def count_adjacent_rolls(paper_roll_map: List[str], row_index, col_index) -> int:
    count = 0
    for adjacent_direction in directions:
        new_row_index = row_index + adjacent_direction[0]
        new_col_index = col_index + adjacent_direction[1]

        if (
            0 <= new_row_index < len(paper_roll_map)
            and 0 <= new_col_index < len(paper_roll_map[0])
        ):
            if paper_roll_map[new_row_index][new_col_index] == "@":
                count += 1

    return count


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day04.txt as a string.
    return: (part 2 answer)
    """
    paper_roll_map = parse_paper_roll_diagram(input_data)

    movable_rolls = 0
    total_removed = 0
    movable_rolls = find_rolls_indices_to_remove(paper_roll_map)
    paper_roll_map = remove_rolls_from_map(paper_roll_map, movable_rolls)
    total_removed = len(movable_rolls)

    while len(movable_rolls) > 0:
        movable_rolls = find_rolls_indices_to_remove(paper_roll_map)
        paper_roll_map = remove_rolls_from_map(paper_roll_map, movable_rolls)
        total_removed += len(movable_rolls)

    return total_removed


def remove_rolls_from_map(
    paper_roll_map: List[str], movable_roll_indices: List[int]
) -> List[str]:
    new_paper_roll_map = paper_roll_map
    for index in movable_roll_indices:
        new_paper_roll_map[index[0]] = (
            paper_roll_map[index[0]][: index[1]]
            + "x"
            + paper_roll_map[index[0]][index[1] + 1 :]
        )
    return new_paper_roll_map


def find_rolls_indices_to_remove(paper_roll_map: List[str]) -> int:
    roll_indices_to_remove = []
    for i, _ in enumerate(paper_roll_map):
        for j, _ in enumerate(paper_roll_map[0]):
            adjacent_count = 0
            if paper_roll_map[i][j] == "@":
                adjacent_count += count_adjacent_rolls(paper_roll_map, i, j)
                if adjacent_count < 4:
                    roll_indices_to_remove.append((i, j))

    return roll_indices_to_remove
