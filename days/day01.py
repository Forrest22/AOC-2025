def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day01.txt as a string.
    return: (part 1 answer)
    """
    lines = input_data.splitlines()

    current_dial_num = 50
    count_of_zeroes = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])

        current_dial_num = calculate_dial_results(current_dial_num, direction, clicks)
        if current_dial_num == 0:
            count_of_zeroes += 1

    return count_of_zeroes


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day01.txt as a string.
    return: (part 2 answer)
    """
    lines = input_data.splitlines()

    current_dial_num = 50
    count_of_zeroes = 0

    for line in lines:
        direction = line[0]
        clicks = int(line[1:])
        count_of_zeroes += calculate_times_passed_zero(current_dial_num, direction, clicks)
        current_dial_num = calculate_dial_results(current_dial_num, direction, clicks)

    return count_of_zeroes


def calculate_dial_results(current_dial_num: int, direction: str, clicks: int) -> int:
    if direction == "l":
        return (current_dial_num - clicks) % 100
    return (current_dial_num + clicks) % 100


def calculate_times_passed_zero(
    current_dial_num: int, direction: str, clicks: int
) -> int:
    start = current_dial_num
    end = current_dial_num
    if direction == "l":
        end = current_dial_num - clicks
    else:
        end = current_dial_num + clicks

    if end < 0:
        if start == 0:
            return end // -100
        return 1 + end // -100
    if end > 99:
        return end // 100
    if end == 0:
        return 1
    return 0
