from typing import list, default_dict
from collections import defaultdict

class machine():
    def __init__(self, light_diagram: List[bool], button_schematics:List[List[int]], joltage_requirements:list[int]):
        self.light_diagram = light_diagram
        self.button_schematics = button_schematics
        self.joltage_requirements = joltage_requirements
    def __str__(self):
        return f"[{self.light_diagram}], {self.button_schematics}, {self.joltage_requirements}"
    def __repr__(self):
        return f"[{self.light_diagram}], {self.button_schematics}, {self.joltage_requirements}"

def get_machine_list(input: str):
    machine_list:list[machine] = []
    for line in input.splitlines():
        line_split = line.split(" ")

        light_diagram = [True if val == "#" else False for val in line_split[0][1:-1]]

        button_wirings_raw = line_split[1:-1]
        button_wirings = []
        for button in button_wirings_raw:
            button_wirings.append([int(num) for num in button[1:-1].replace(","," ").split()])

        joltages = [int(num) for num in line_split[-1][1:-1].replace(","," ").split()]

        m = machine(light_diagram,button_wirings,joltages)
        machine_list.append(m)
    return machine_list     

def dfs_part1( lights: list[bool],
    target_lights: list[bool],
    i: int,
    buttons: list[list[int]],
    cache: default_dict) -> int:
    if lights == target_lights:
        return 0
    
    if i == len(buttons):
        return -1
    
    key = (tuple(lights), i)
    if key in cache:
        return cache[key]
    
    result = 999999999
    for j in range(i,len(buttons)):
        for k in buttons[j]:
            lights[k] = not lights[k]
        r = 1 + dfs_part1(lights, target_lights, j + 1, buttons, cache)
        if r > 0:
            result = min(result, r)
        for k in buttons[j]:
            lights[k] = not lights[k]

    cache[key] = result
    return result

def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day09.txt as a string.
    return: (part 1 answer)
    """
    machine_list = get_machine_list(input_data)
    total = 0
    for machine in machine_list:
        dd = defaultdict()
        starting_lights = [false for light in machine.light_diagram]
        r = dfs_part1(starting_lights, machine.light_diagram, 0, machine.button_schematics, dd)
        total += r
    return total


def count_affected_buttons(index: int, buttons: list[list[int]], mask: int) -> int:
    """count how many available buttons affect the given joltage index."""
    count = 0
    k = mask
    while k > 0:
        # least significant bit
        lsb = (k & -k)
        button_index = (lsb.bit_length() - 1)
        if index in buttons[button_index]:
            count += 1
        k &= k - 1
    return count


def combinations_iterator(n: int, minimum: int, maxima: list[int]):
    """
    generate all possible count combinations:
    each position i ranges from 0..maxima[i]
    the total must reduce the selected joltage value by exactly `minimum`
    """
    counts = [0] * n

    def backtrack(pos, remaining):
        if pos == n:
            if remaining == 0:
                yield counts[:]
            return

        for value in range(min(maxima[pos], remaining) + 1):
            counts[pos] = value
            yield from backtrack(pos + 1, remaining - value)

    yield from backtrack(0, minimum)

def dfs_part2(joltage: list[int],
              available_buttons_mask: int,
              buttons: list[list[int]]) -> int:
    """
    optimized to cut as many corners as possible. focusing on the joltage that is affected by the least number of buttons.
    inspired by https://github.com/michel-kraemer/adventofcode-rust/blob/main/2025/day10/src/main.rs
    """

    if all(j == 0 for j in joltage):
        return 0

    # find the joltage index with:
    #   1) fewest affecting buttons
    #   2) highest joltage value (tie breaker)
    candidates = [
        (i, v)
        for i, v in enumerate(joltage)
        if v > 0
    ]

    if not candidates:
        return 0

    mini, min_val = min(
        candidates,
        key=lambda x: (
            count_affected_buttons(x[0], buttons, available_buttons_mask),
            -x[1]
        )
    )

    # collect matching buttons
    matching_buttons = []
    km = available_buttons_mask
    while km > 0:
        lsb = (km & -km)
        k = lsb.bit_length() - 1
        if mini in buttons[k]:
            matching_buttons.append((k, buttons[k]))
        km &= km - 1

    # determine maxima for each matching button
    maxima = []
    for _, b in matching_buttons:
        min_possible = min(joltage[j] for j in b)
        maxima.append(min_possible)

    if matching_buttons:

        # create new mask removing matching buttons
        new_mask = available_buttons_mask
        for i, _ in matching_buttons:
            new_mask &= ~(1 << i)

        best = 999999999

        # try all valid combinations
        for counts in combinations_iterator(len(matching_buttons), min_val, maxima):

            new_joltage = joltage[:]
            valid = true

            for bi, cnt in enumerate(counts):
                if cnt == 0:
                    continue
                for j in matching_buttons[bi][1]:
                    if new_joltage[j] >= cnt:
                        new_joltage[j] -= cnt
                    else:
                        valid = false
                        break
                if not valid:
                    break

            if not valid:
                continue

            r = dfs_part2(new_joltage, new_mask, buttons)
            if r != 999999999:
                best = min(best, min_val + r)

        return best
    return 999999999


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day09.txt as a string.
    return: (part 2 answer)
    """
    machine_list = get_machine_list(input_data)
    total = 0
    for machine in machine_list:
        r = dfs_part2(machine.joltage_requirements, (1 << len(machine.button_schematics)) - 1, machine.button_schematics)
        total += r
    return total

