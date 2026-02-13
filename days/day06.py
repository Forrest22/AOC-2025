from typing import List, Tuple
import math


def parse_math_homework(
    input_data: str,
) -> Tuple[List[List[int]], List[str]]:
    """
    Extracts the math homework, one 2D array and one list of operators
    """
    lines = input_data.splitlines()

    columns = []
    operators = []
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            operators = line.split()
        elif i == 0:
            for num in line.split():
                columns.append([int(num)])
        else:
            for j, num in enumerate(line.split()):
                columns[j].append(int(num))

    return (columns, operators)


def calculate_grand_total(columns: List[List[int]], operators: List[str]) -> int:
    """
    calculates the grand total from the given columns and operators.
    return: int
    """
    total = 0
    for i, operator in enumerate(operators):
        if operator == "*":
            total += math.prod(columns[i])
        elif operator == "+":
            total += sum(columns[i])
        else:
            print("unexpected operator.")
    return total


def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day06.txt as a string.
    return: (part 1 answer)
    """
    columns, operators = parse_math_homework(input_data)
    return calculate_grand_total(columns, operators)


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day06.txt as a string.
    return: (part 2 answer)
    """
    input_data = input_data.split("\n")
    ops_line = input_data[-1]
    del input_data[-1]
    data = [
        (i, op)
        for i, x in enumerate(ops_line)
        if (op := {"+": sum, "*": math.prod}.get(x))
    ]
    starting_indices, op_functions = zip(*data)
    ending_indices = [i - 1 for i in starting_indices[1:]] + [None]
    nums_with_spacing_offsets = [
        [line[start:end] for line in input_data]
        for start, end in zip(starting_indices, ending_indices)
    ]
    cephalopod_nums = (map("".join, zip(*num)) for num in nums_with_spacing_offsets)
    return sum(op(map(int, col)) for op, col in zip(op_functions, cephalopod_nums))
