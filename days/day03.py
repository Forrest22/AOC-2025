from typing import List


def parse_battery_banks(inputData: str) -> List[str]:
    """
    Extract integer battery values from each line of input (each bank).
    """
    lines = inputData.splitlines()
    return [line for line in lines]


def solve_part1(inputData: str) -> int:
    """
    input_data: full contents of inputs/day03.txt as a string.
    return: (part 1 answer)
    """
    batteryBanks = parse_battery_banks(inputData)

    totalJoltage = 0
    for bank in batteryBanks:
        leftmostJoltage, rightmostJoltage = 0, 0
        leftmostJoltageIndex = 0
        print(bank)
        for i, battery in enumerate(bank):
            batteryJoltage = int(battery)
            if (batteryJoltage > leftmostJoltage) and i != len(bank) - 1:
                leftmostJoltage = batteryJoltage
                leftmostJoltageIndex = i
                rightmostJoltage = int(bank[i + 1])
        for j in range(len(bank) - 1, leftmostJoltageIndex, -1):
            batteryJoltage = int(bank[j])
            if batteryJoltage > rightmostJoltage:
                rightmostJoltage = int(bank[j])
        totalJoltage += int(str(leftmostJoltage) + str(rightmostJoltage))
    return totalJoltage


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day03.txt as a string.
    return: (part 2 answer)
    """
    batteryBanks = parse_battery_banks(inputData)

    totalJoltage = 0
    for bank in batteryBanks:
        remove = len(bank) - 12
        stack = []
        for digit in bank:
            while remove > 0 and stack and stack[-1] < int(digit):
                stack.pop()
                remove -= 1
            stack.append(int(digit))
        val = int("".join(map(str, stack[:12])))
        totalJoltage += val
    return totalJoltage


def get_max(batteryBank: List[str]) -> int:
    maxIndex = 0
    for i, value in enumerate(batteryBank):
        if value > maxValue:
            maxValue = value
            maxIndex = i
    return maxIndex
