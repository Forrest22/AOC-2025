from collections import defaultdict
import math
from typing import DefaultDict, List, Tuple


class JunctionBox:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


class Circuit(list):
    def __str__(self):
        return "Circuit[" + ", ".join(map(str, self)) + "]"


def parse_junction_boxes(input_data: str) -> Circuit:
    junction_boxes: Circuit = []
    for line in input_data.splitlines():
        coords = map(int, line.split(","))
        junction_boxes.append(JunctionBox(*coords))
    return junction_boxes


def calculate_result_part1(boxes: Circuit) -> int:
    _, first_circuit = get_shortest_distance_box(boxes)
    del distances[first_circuit]
    circuits = [Circuit([first_circuit[0], first_circuit[1]])]
    for box in first_circuit:
        boxes.remove(box)
    connections_made = 1

    while len(boxes) > 0 and connections_made < 1000:
        connections_made += 1
        lowest = 99999999999999
        lowest_box_pair = None
        for box_pair in distances.keys():
            if distances[box_pair] < lowest:
                lowest = distances[box_pair]
                lowest_box_pair = box_pair
        del distances[lowest_box_pair]
        if lowest_box_pair[0] in boxes and lowest_box_pair[1] in boxes:
            for box in lowest_box_pair:
                boxes.remove(box)
            circuits.append([lowest_box_pair[0], lowest_box_pair[1]])
        elif lowest_box_pair[0] in boxes:
            boxes.remove(lowest_box_pair[0])
            circuits = find_circuit_and_add_box(
                in_circuit_box=lowest_box_pair[1],
                free_box=lowest_box_pair[0],
                circuits=circuits,
            )
        elif lowest_box_pair[1] in boxes:
            boxes.remove(lowest_box_pair[1])
            circuits = find_circuit_and_add_box(
                in_circuit_box=lowest_box_pair[0],
                free_box=lowest_box_pair[1],
                circuits=circuits,
            )
        else:
            circ0_index, circ1_index = -1, -1
            for i, circ in enumerate(circuits):
                if lowest_box_pair[0] in circ and lowest_box_pair[1] in circ:
                    # ignore this case
                    pass
                elif lowest_box_pair[0] in circ:
                    # found one
                    circ0_index = i
                elif lowest_box_pair[1] in circ:
                    # found two
                    circ1_index = i
                else:
                    # do nothing
                    pass

            if circ0_index != -1 and circ1_index != -1:
                # combine
                new_circs: List[Circuit] = []
                for i, circ in enumerate(circuits):
                    if i == circ0_index:
                        new_circs.append(circuits[circ0_index] + circuits[circ1_index])
                    elif i == circ1_index:
                        pass
                    else:
                        new_circs.append(circ)
                circuits = new_circs
            else:
                pass

    # return the three largest numbers
    sizes = [len(circ) for circ in circuits]
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


def concat_existing_circuits_with_boxes(
    box1: JunctionBox, box2: JunctionBox, circuits: List[Circuit]
) -> List[Circuit]:
    circ0_index, circ1_index = 0, 0
    for i, circ in enumerate(circuits):
        if box1 in circ:
            circ0_index = i
        elif box2 in circ:
            circ1_index = i

    res: List[Circuit] = []
    for i, circ in enumerate(circuits):
        if i == circ0_index:
            res.append(circ + circuits[circ1_index])
        elif i == circ1_index:
            pass
        else:
            res.append(circ)
    return []


def find_circuit_and_add_box(
    in_circuit_box: JunctionBox, free_box: JunctionBox, circuits: List[Circuit]
) -> List[Circuit]:
    for i, circ in enumerate(circuits):
        if in_circuit_box in circ:
            circuits[i].append(free_box)
            return circuits
    return RuntimeError("ba humbug the box couldn't be added")


distances: DefaultDict[Tuple[JunctionBox, JunctionBox], float] = defaultdict()


def get_shortest_distance_box(
    boxes: Circuit,
) -> Tuple[float, Tuple[JunctionBox, JunctionBox]]:
    shortest_distance_in_boxes = 99999999999999
    shortest_dist_boxes_in_boxes: Tuple[JunctionBox, JunctionBox] = None

    # get the shortest distance in boxes
    for i, _ in enumerate(boxes):
        for j in range(i + 1, len(boxes)):
            if (boxes[i], boxes[j]) not in distances.keys() and (
                boxes[j],
                boxes[i],
            ) not in distances.keys():
                dist = straight_line_distance(boxes[i], boxes[j])
                distances[(boxes[i], boxes[j])] = dist
                if shortest_distance_in_boxes > dist:
                    shortest_distance_in_boxes = dist
                    shortest_dist_boxes_in_boxes = (boxes[i], boxes[j])

    return shortest_distance_in_boxes, shortest_dist_boxes_in_boxes


def straight_line_distance(a: JunctionBox, b: JunctionBox) -> float:
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2)


def solve_part1(input_data: str) -> int:
    """
    input_data: full contents of inputs/day08.txt as a string.
    return: (part 1 answer)
    """
    boxes = parse_junction_boxes(input_data)
    return calculate_result_part1(boxes)


def calculate_result_part2(boxes: Circuit) -> int:
    _, first_circuit = get_shortest_distance_box(boxes)
    del distances[first_circuit]
    circuits = [Circuit([first_circuit[0], first_circuit[1]])]
    for box in first_circuit:
        boxes.remove(box)

    lowest = 99999999999999
    lowest_box_pair = None
    while len(boxes) > 0:
        lowest = 99999999999999
        lowest_box_pair = None
        for box_pair in distances.keys():
            if distances[box_pair] < lowest:
                lowest = distances[box_pair]
                lowest_box_pair = box_pair
        del distances[lowest_box_pair]
        if lowest_box_pair[0] in boxes and lowest_box_pair[1] in boxes:
            for box in lowest_box_pair:
                boxes.remove(box)
            circuits.append([lowest_box_pair[0], lowest_box_pair[1]])
        elif lowest_box_pair[0] in boxes:
            boxes.remove(lowest_box_pair[0])
            circuits = find_circuit_and_add_box(
                in_circuit_box=lowest_box_pair[1],
                free_box=lowest_box_pair[0],
                circuits=circuits,
            )
        elif lowest_box_pair[1] in boxes:
            boxes.remove(lowest_box_pair[1])
            circuits = find_circuit_and_add_box(
                in_circuit_box=lowest_box_pair[0],
                free_box=lowest_box_pair[1],
                circuits=circuits,
            )
        else:
            circ0_index, circ1_index = -1, -1
            for i, circ in enumerate(circuits):
                if lowest_box_pair[0] in circ and lowest_box_pair[1] in circ:
                    # ignore this case
                    pass
                elif lowest_box_pair[0] in circ:
                    # found one
                    circ0_index = i
                elif lowest_box_pair[1] in circ:
                    # found two
                    circ1_index = i
                else:
                    # do nothing
                    pass

            if circ0_index != -1 and circ1_index != -1:
                # combine
                new_circs: List[Circuit] = []
                for i, circ in enumerate(circuits):
                    if i == circ0_index:
                        new_circs.append(circuits[circ0_index] + circuits[circ1_index])
                    elif i == circ1_index:
                        pass
                    else:
                        new_circs.append(circ)
                circuits = new_circs
            else:
                pass

    # return the three largest numbers
    return (lowest_box_pair[0]).x * (lowest_box_pair[1]).x


def solve_part2(input_data: str) -> int:
    """
    input_data: full contents of inputs/day08.txt as a string.
    return: (part 2 answer)
    """
    boxes = parse_junction_boxes(input_data)
    return calculate_result_part2(boxes)
