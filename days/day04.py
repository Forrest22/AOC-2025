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


def parse_paper_roll_diagram(inputData: str) -> List[str]:
    """
    Extract the map of paper rolls.
    """
    lines = inputData.splitlines()
    return lines


def solve_part1(inputData: str) -> int:
    """
    input_data: full contents of inputs/day04.txt as a string.
    return: (part 1 answer)
    """
    paperRollMap = parse_paper_roll_diagram(inputData)

    movableRolls = 0
    for i, _ in enumerate(paperRollMap):
        for j, _ in enumerate(paperRollMap[0]):
            adjacentCount = 0
            if paperRollMap[i][j] == "@":
                adjacentCount += count_adjacent_rolls(paperRollMap, i, j)
                if adjacentCount < 4:
                    movableRolls += 1

    return movableRolls


def count_adjacent_rolls(paperRollMap: List[str], rowIndex, colIndex) -> int:
    count = 0
    for adjacentDirection in directions:
        newRowIndex = rowIndex + adjacentDirection[0]
        newColIndex = colIndex + adjacentDirection[1]

        if (
            0 <= newRowIndex
            and newRowIndex < len(paperRollMap)
            and 0 <= newColIndex
            and newColIndex < len(paperRollMap[0])
        ):
            if paperRollMap[newRowIndex][newColIndex] == "@":
                count += 1

    return count


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day04.txt as a string.
    return: (part 2 answer)
    """
    paperRollMap = parse_paper_roll_diagram(inputData)

    movableRolls = 0
    totalRemoved = 0
    movableRolls = find_rolls_indices_to_remove(paperRollMap)
    paperRollMap = remove_rolls_from_map(paperRollMap, movableRolls)
    totalRemoved = len(movableRolls)

    while len(movableRolls) > 0:
        movableRolls = find_rolls_indices_to_remove(paperRollMap)
        paperRollMap = remove_rolls_from_map(paperRollMap, movableRolls)
        totalRemoved += len(movableRolls)

    return totalRemoved


def remove_rolls_from_map(
    paperRollMap: List[str], movableRollIndices: List[int]
) -> List[str]:
    newPaperRollMap = paperRollMap
    for index in movableRollIndices:
        newPaperRollMap[index[0]] = (
            paperRollMap[index[0]][: index[1]]
            + "X"
            + paperRollMap[index[0]][index[1] + 1 :]
        )
    return newPaperRollMap


def find_rolls_indices_to_remove(paperRollMap: List[str]) -> int:
    rollIndicesToRemove = []
    for i, _ in enumerate(paperRollMap):
        for j, _ in enumerate(paperRollMap[0]):
            adjacentCount = 0
            if paperRollMap[i][j] == "@":
                adjacentCount += count_adjacent_rolls(paperRollMap, i, j)
                if adjacentCount < 4:
                    rollIndicesToRemove.append((i, j))

    return rollIndicesToRemove
