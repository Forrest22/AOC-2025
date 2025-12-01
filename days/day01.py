def solve_part1(input_data: str):
    """
    input_data: full contents of inputs/day01.txt as a string.
    return: (part1_answer, part2_answer)
    """

    # Example parsing:
    lines = input_data.splitlines()

    # TODO: implement real puzzle logic here
    part1 = len(lines)
    return part1


def solve_part2(input_data: str):
    """
    input_data: full contents of inputs/day01.txt as a string.
    return: (part1_answer, part2_answer)
    """

    # Example parsing:
    lines = input_data.splitlines()

    part2 = sum(len(x) for x in lines)

    return part2
