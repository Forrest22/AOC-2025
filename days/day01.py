def solve_part1(inputData: str) -> int:
    """
    input_data: full contents of inputs/day01.txt as a string.
    return: (part 1 answer)
    """
    lines = inputData.splitlines()

    currentDialNum = 50
    countOfZeroes = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])

        currentDialNum = calculate_dial_results(currentDialNum, direction, clicks)
        if currentDialNum == 0:
            countOfZeroes += 1

    return countOfZeroes


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day01.txt as a string.
    return: (part 2 answer)
    """
    lines = inputData.splitlines()

    currentDialNum = 50
    countOfZeroes = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])
        countOfZeroes += calculate_times_passed_zero(currentDialNum, direction, clicks)
        currentDialNum = calculate_dial_results(currentDialNum, direction, clicks)

    return countOfZeroes


def calculate_dial_results(currentDialNum: int, direction: str, clicks: int) -> int:
    if direction == "L":
        return (currentDialNum - clicks) % 100
    else:
        return (currentDialNum + clicks) % 100


def calculate_times_passed_zero(
    currentDialNum: int, direction: str, clicks: int
) -> int:
    start = currentDialNum
    end = currentDialNum
    if direction == "L":
        end = currentDialNum - clicks
    else:
        end = currentDialNum + clicks

    if end < 0:
        if start == 0:
            return end // -100
        else:
            return 1 + end // -100
    elif end > 99:
        return end // 100
    elif end == 0:
        return 1
    return 0
