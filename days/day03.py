from typing import List


def parse_battery_banks(input_data: str) -> List[str]:
    """
    extract integer battery values from each line of input (each bank).
    """
    lines = input_data.splitlines()
    return lines


def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day03.txt as a string.
    return: (part 1 answer)
    """
    battery_banks = parse_battery_banks(input_data)

    total_joltage = 0
    for bank in battery_banks:
        leftmost_joltage, rightmost_joltage = 0, 0
        leftmost_joltage_index = 0
        for i, battery in enumerate(bank):
            battery_joltage = int(battery)
            if (battery_joltage > leftmost_joltage) and i != len(bank) - 1:
                leftmost_joltage = battery_joltage
                leftmost_joltage_index = i
                rightmost_joltage = int(bank[i + 1])
        for j in range(len(bank) - 1, leftmost_joltage_index, -1):
            battery_joltage = int(bank[j])
            if battery_joltage > rightmost_joltage:
                rightmost_joltage = int(bank[j])
        total_joltage += int(str(leftmost_joltage) + str(rightmost_joltage))
    return total_joltage


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day03.txt as a string.
    return: (part 2 answer)
    """
    battery_banks = parse_battery_banks(input_data)

    total_joltage = 0
    for bank in battery_banks:
        remove_count = len(bank) - 12
        stack = []
        for digit in bank:
            # greedy algorithm to fill the stack with the highest number possible
            while remove_count > 0 and stack and stack[-1] < int(digit):
                stack.pop()
                remove_count -= 1
            stack.append(int(digit))
        val = int("".join(map(str, stack[:12])))
        total_joltage += val
    return total_joltage
