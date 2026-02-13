from typing import List


def parse_tachyon_manifold(input_data: str) -> List[str]:
    return input_data.splitlines()


def process_manifold_splits(tachyon_manifold: List[str]) -> int:
    beams = [tachyon_manifold[0].find("s")]
    count = 0
    for line in tachyon_manifold[1:]:
        for i, location in enumerate(line):
            if location == "^" and i in beams:
                if i + 1 not in beams:
                    beams.append(i + 1)
                if i - 1 not in beams:
                    beams.append(i - 1)
                beams.remove(i)
                count += 1

    return count


def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day07.txt as a string.
    return: (part 1 answer)
    """
    tachyon_manifold = parse_tachyon_manifold(input_data)
    return process_manifold_splits(tachyon_manifold)


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day07.txt as a string.
    reference: https://old.reddit.com/r/adventofcode/comments/1pg9w66/2025_day_7_solutions/nsq17au/
    because my recursive solution, while right was incredibly slow.
    return: (part 2 answer)
    """
    splitters = [
        col for line in input_data.splitlines() for col, x in enumerate(line) if x == "^"
    ]
    entering = [1] + [0 for _ in range(0, len(splitters) - 1)]

    # for each splitter, compare with each other after it
    for i, si in enumerate(splitters):
        for j, sj in enumerate(splitters[:i][::-1]):
            # if the columns are the same then they won't carry split beam
            if si == sj:
                break
            # if the difference of columns is one, increase the beam count for that col
            if abs(si - sj) == 1:
                entering[i] += entering[i - j - 1]
    return sum(entering) + 1
