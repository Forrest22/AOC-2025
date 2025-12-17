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


def parse_junction_boxes(inputData: str) -> Circuit:
    junctionBoxes: Circuit = []
    for line in inputData.splitlines():
        coords = map(int, line.split(","))
        junctionBoxes.append(JunctionBox(*coords))
    return junctionBoxes


def calculate_result_part1(boxes: Circuit) -> int:
    _, firstCircuit = get_shortest_distance_box(boxes)
    del distances[firstCircuit]
    circuits = [Circuit([firstCircuit[0], firstCircuit[1]])]
    for box in firstCircuit:
        boxes.remove(box)
    connectionsMade = 1

    while len(boxes) > 0 and connectionsMade < 1000:
        connectionsMade += 1
        lowest = 99999999999999
        lowestBoxPair = None
        for boxPair in distances.keys():
            if distances[boxPair] < lowest:
                lowest = distances[boxPair]
                lowestBoxPair = boxPair
        del distances[lowestBoxPair]
        if lowestBoxPair[0] in boxes and lowestBoxPair[1] in boxes:
            for box in lowestBoxPair:
                boxes.remove(box)
            circuits.append([lowestBoxPair[0], lowestBoxPair[1]])
        elif lowestBoxPair[0] in boxes:
            boxes.remove(lowestBoxPair[0])
            circuits = find_circuit_and_add_box(
                inCircuitBox=lowestBoxPair[1],
                freeBox=lowestBoxPair[0],
                circuits=circuits,
            )
        elif lowestBoxPair[1] in boxes:
            boxes.remove(lowestBoxPair[1])
            circuits = find_circuit_and_add_box(
                inCircuitBox=lowestBoxPair[0],
                freeBox=lowestBoxPair[1],
                circuits=circuits,
            )
        else:
            circ0Index, circ1Index = -1, -1
            for i, circ in enumerate(circuits):
                if lowestBoxPair[0] in circ and lowestBoxPair[1] in circ:
                    # ignore this case
                    pass
                elif lowestBoxPair[0] in circ:
                    # found one
                    circ0Index = i
                elif lowestBoxPair[1] in circ:
                    # found two
                    circ1Index = i
                else:
                    # do nothing
                    pass

            if circ0Index != -1 and circ1Index != -1:
                # combine
                newCircs: List[Circuit] = []
                for i, circ in enumerate(circuits):
                    if i == circ0Index:
                        newCircs.append(circuits[circ0Index] + circuits[circ1Index])
                    elif i == circ1Index:
                        pass
                    else:
                        newCircs.append(circ)
                circuits = newCircs
            else:
                pass

    # return the three largest numbers
    sizes = [len(circ) for circ in circuits]
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


def concat_existing_circuits_with_boxes(
    box1: JunctionBox, box2: JunctionBox, circuits: List[Circuit]
) -> List[Circuit]:
    circ0Index, circ1Index = 0, 0
    for i, circ in enumerate(circuits):
        if box1 in circ:
            circ0Index = i
        elif box2 in circ:
            circ1Index = i

    res: List[Circuit] = []
    for i, circ in enumerate(circuits):
        if i == circ0Index:
            res.append(circ + circuits[circ1Index])
        elif i == circ1Index:
            pass
        else:
            res.append(circ)
    return []


def find_circuit_and_add_box(
    inCircuitBox: JunctionBox, freeBox: JunctionBox, circuits: List[Circuit]
) -> List[Circuit]:
    for i, circ in enumerate(circuits):
        if inCircuitBox in circ:
            circuits[i].append(freeBox)
            return circuits
    return RuntimeError("Ba humbug the box couldn't be added")


distances: DefaultDict[Tuple[JunctionBox, JunctionBox], float] = defaultdict()


def get_shortest_distance_box(
    boxes: Circuit,
) -> Tuple[float, tuple[JunctionBox, JunctionBox]]:
    shortestDistanceInBoxes = 99999999999999
    shortestDistBoxesInBoxes: Tuple[JunctionBox, JunctionBox] = None

    # get the shortest distance in boxes
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            if (boxes[i], boxes[j]) not in distances.keys() and (
                boxes[j],
                boxes[i],
            ) not in distances.keys():
                dist = straight_line_distance(boxes[i], boxes[j])
                distances[(boxes[i], boxes[j])] = dist
                if shortestDistanceInBoxes > dist:
                    shortestDistanceInBoxes = dist
                    shortestDistBoxesInBoxes = (boxes[i], boxes[j])

    return shortestDistanceInBoxes, shortestDistBoxesInBoxes


def straight_line_distance(a: JunctionBox, b: JunctionBox) -> float:
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2 + (b.z - a.z) ** 2)


def solve_part1(inputData: str) -> int:
    """
    input_data: full contents of inputs/day08.txt as a string.
    return: (part 1 answer)
    """
    boxes = parse_junction_boxes(inputData)
    return calculate_result_part1(boxes)


def calculate_result_part2(boxes: Circuit) -> int:
    _, firstCircuit = get_shortest_distance_box(boxes)
    del distances[firstCircuit]
    circuits = [Circuit([firstCircuit[0], firstCircuit[1]])]
    for box in firstCircuit:
        boxes.remove(box)

    lowest = 99999999999999
    lowestBoxPair = None
    while len(boxes) > 0:
        lowest = 99999999999999
        lowestBoxPair = None
        for boxPair in distances.keys():
            if distances[boxPair] < lowest:
                lowest = distances[boxPair]
                lowestBoxPair = boxPair
        del distances[lowestBoxPair]
        if lowestBoxPair[0] in boxes and lowestBoxPair[1] in boxes:
            for box in lowestBoxPair:
                boxes.remove(box)
            circuits.append([lowestBoxPair[0], lowestBoxPair[1]])
        elif lowestBoxPair[0] in boxes:
            boxes.remove(lowestBoxPair[0])
            circuits = find_circuit_and_add_box(
                inCircuitBox=lowestBoxPair[1],
                freeBox=lowestBoxPair[0],
                circuits=circuits,
            )
        elif lowestBoxPair[1] in boxes:
            boxes.remove(lowestBoxPair[1])
            circuits = find_circuit_and_add_box(
                inCircuitBox=lowestBoxPair[0],
                freeBox=lowestBoxPair[1],
                circuits=circuits,
            )
        else:
            circ0Index, circ1Index = -1, -1
            for i, circ in enumerate(circuits):
                if lowestBoxPair[0] in circ and lowestBoxPair[1] in circ:
                    # ignore this case
                    pass
                elif lowestBoxPair[0] in circ:
                    # found one
                    circ0Index = i
                elif lowestBoxPair[1] in circ:
                    # found two
                    circ1Index = i
                else:
                    # do nothing
                    pass

            if circ0Index != -1 and circ1Index != -1:
                # combine
                newCircs: List[Circuit] = []
                for i, circ in enumerate(circuits):
                    if i == circ0Index:
                        newCircs.append(circuits[circ0Index] + circuits[circ1Index])
                    elif i == circ1Index:
                        pass
                    else:
                        newCircs.append(circ)
                circuits = newCircs
            else:
                pass

    # return the three largest numbers
    return (lowestBoxPair[0]).x * (lowestBoxPair[1]).x


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day08.txt as a string.
    return: (part 2 answer)
    """
    boxes = parse_junction_boxes(inputData)
    return calculate_result_part2(boxes)
