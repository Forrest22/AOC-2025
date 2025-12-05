from typing import List, Tuple, Mapping


def ingredient_database(inputData: str) -> Tuple[Mapping[int, bool], List[str]]:
    """
    Extract the range of fresh ingredients into a dict, then aggregates the ingredient list and returns both.
    """
    lines = inputData.splitlines()

    ingredientIdsSection = False
    freshIngredients = {}
    ingredientList = []

    for line in lines:
        if line == "":
            ingredientIdsSection = True
        elif ingredientIdsSection:
            ingredientList.append(line)
        else:
            # if we're processing the fresh ingredient ranges
            freshRange = line.split("-")
            start = int(freshRange[0])
            end = int(freshRange[1])
            for i in range(start, end + 1):
                freshIngredients[i] = True

    return (freshIngredients, ingredientList)


def count_fresh_ingredients(
    freshIngredients: Mapping[str, bool],
    ingredientList: List[str],
) -> int:
    count = 0
    for ingredient in ingredientList:
        if int(ingredient) in freshIngredients:
            count += 1
    return count


def solve_part1(inputData: str) -> int:
    """
    input_data: full contents of inputs/day05.txt as a string.
    return: (part 1 answer)
    """
    freshIngredientRanges, ingredientList = ingredient_database(inputData)

    return count_fresh_ingredients(freshIngredientRanges, ingredientList)


def solve_part2(inputData: str) -> int:
    """
    input_data: full contents of inputs/day05.txt as a string.
    return: (part 2 answer)
    """
    paperRollMap = ingredient_database(inputData)

    return 0
