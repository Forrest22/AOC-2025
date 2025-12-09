from typing import List, Tuple
import math


def parse_math_homework(
    inputData: str,
) -> Tuple[List[List[int]], List[str]]:
    """
    Extract the range of fresh ingredients into a dict, then aggregates the ingredient list and returns both.
    """
    lines = inputData.splitlines()

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
    Calculates the grand total from the given columns and operators.
    return: int
    """
    total = 0
    for i, operator in enumerate(operators):
        if operator == "*":
            total += math.prod(columns[i])
        elif operator == "+":
            total += sum(columns[i])
        else:
            print("Unexpected operator.")
    return total


def solve_part1(inputData: str) -> int:
    """
    input_data: full contents of inputs/day06.txt as a string.
    return: (part 1 answer)
    """
    columns, operators = parse_math_homework(inputData)
    return calculate_grand_total(columns, operators)


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day06.txt as a string.
    return: (part 2 answer)
    """
    inputData = inputData.split("\n")
    ops_line = inputData[-1]
    del inputData[-1]
    data = [
        (i, op)
        for i, x in enumerate(ops_line)
        if (op := {"+": sum, "*": math.prod}.get(x))
    ]
    startingIndices, opFunctions = zip(*data)
    endingIndices = [i - 1 for i in startingIndices[1:]] + [None]
    numsWithSpacingOffsets = [
        [line[start:end] for line in inputData]
        for start, end in zip(startingIndices, endingIndices)
    ]
    cephalopodNums = (map("".join, zip(*num)) for num in numsWithSpacingOffsets)
    return sum(op(map(int, col)) for op, col in zip(opFunctions, cephalopodNums))
