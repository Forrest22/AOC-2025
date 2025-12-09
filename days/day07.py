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


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day07.txt as a string.
    return: (part 2 answer)
    """
    tachyonManifold = parse_tachyon_manifold(inputData)

    return 0
