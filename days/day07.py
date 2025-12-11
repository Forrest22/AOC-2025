from typing import List


def parse_tachyon_manifold(inputData: str) -> List[str]:
    return inputData.splitlines()


def process_manifold_splits(tachyonManifold: List[str]) -> int:
    beams = [tachyonManifold[0].find("S")]
    count = 0
    for line in tachyonManifold[1:]:
        for i, location in enumerate(line):
            if location == "^" and i in beams:
                if i + 1 not in beams:
                    beams.append(i + 1)
                if i - 1 not in beams:
                    beams.append(i - 1)
                beams.remove(i)
                count += 1

    return count


def solve_part1(inputData: str) -> int:
    """
    input_data: full contents of inputs/day07.txt as a string.
    return: (part 1 answer)
    """
    tachyonManifold = parse_tachyon_manifold(inputData)
    return process_manifold_splits(tachyonManifold)


def find_number_of_timelines(position: int, diagram: List[str], row: int) -> int:
    """
    Ok so this isn't optimized and takes forever to so if I have more time I'll
    circle back and maybe approach with a DP solution instead of a recursive solution?
    """
    if 0 > row or row >= len(diagram):
        return 0
    elif 0 > position or position >= len(diagram[0]):
        return 0
    elif diagram[row][position] == "^":
        return 0
    elif diagram[row][position] == "S":
        return 1
    elif (0 <= position - 1 and position - 1 < len(diagram[0])) or (
        0 <= position + 1 and position + 1 < len(diagram[0])
    ):
        if (0 <= position - 1 and position - 1 < len(diagram[0])) and (
            0 <= position + 1 and position + 1 < len(diagram[0])
        ):
            if diagram[row][position - 1] == "^" and diagram[row][position + 1] == "^":
                return (
                    find_number_of_timelines(position - 1, diagram, row - 1)
                    + find_number_of_timelines(position + 1, diagram, row - 1)
                    + find_number_of_timelines(position, diagram, row - 1)
                )
        if 0 <= position - 1 < len(diagram[0]):
            if diagram[row][position - 1] == "^":
                return find_number_of_timelines(
                    position - 1, diagram, row - 1
                ) + find_number_of_timelines(position, diagram, row - 1)
        if 0 <= position + 1 < len(diagram[0]):
            if diagram[row][position + 1] == "^":
                return find_number_of_timelines(
                    position + 1, diagram, row - 1
                ) + find_number_of_timelines(position, diagram, row - 1)
    return find_number_of_timelines(position, diagram, row - 1)


def process_quantum_manifold_splits(tachyonManifold: List[str]) -> int:
    beams = [tachyonManifold[0].find("S")]
    for line in tachyonManifold[1:]:
        for j, location in enumerate(line):
            if location == "^" and j in beams:
                beams = [beam for beam in beams if j != beam]
                beams.append(j + 1)
                beams.append(j - 1)

    count = 0
    for beam in set(beams):
        count += find_number_of_timelines(
            beam, tachyonManifold, len(tachyonManifold) - 1
        )

    return count


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day07.txt as a string.
    return: (part 2 answer)
    """
    tachyonManifold = parse_tachyon_manifold(inputData)
    return process_quantum_manifold_splits(tachyonManifold)
