def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day01.txt as a string.
    return: (part 1 answer)
    """
    lines = input_data.splitlines()

    currentDialNum = 50
    countOfZeroes = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])

        currentDialNum = calculateDialResult(currentDialNum, direction, clicks)
        if currentDialNum == 0:
            countOfZeroes += 1

    return countOfZeroes


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day01.txt as a string.
    return: (part1_answer, part2_answer)
    """
    lines = input_data.splitlines()

    currentDialNum = 50
    countOfZeroes = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])
        countOfZeroes += calculateTimesPassedZero(currentDialNum, direction, clicks)
        currentDialNum = calculateDialResult(currentDialNum, direction, clicks)

    return countOfZeroes


def calculateDialResult(currentDialNum: int, direction: str, clicks: int) -> int:
    if direction == "L":
        return (currentDialNum - clicks) % 100
    else:
        return (currentDialNum + clicks) % 100


def calculateTimesPassedZero(currentDialNum: int, direction: str, clicks: int) -> int:
    if direction == "L":
        return abs((currentDialNum - clicks) // 100)
    else:
        return abs((currentDialNum + clicks) // 100)
