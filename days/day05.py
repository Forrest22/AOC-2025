from typing import List, Tuple, Mapping


def ingredient_database(
    inputData: str,
) -> Tuple[List[Tuple[int, int]], List[str]]:
    """
    Extract the range of fresh ingredients into a dict, then aggregates the ingredient list and returns both.
    """
    lines = inputData.splitlines()

    ingredientIdsSection = False
    freshIngredientRanges = []
    ingredientList = []

    for line in lines:
        if line == "":
            ingredientIdsSection = True
        elif ingredientIdsSection:
            ingredientList.append(line)
        else:
            # if we're processing the fresh ingredient ranges, save the ranges into a list
            freshRange = line.split("-")
            freshIngredientRanges.append((int(freshRange[0]), int(freshRange[1])))
    return (freshIngredientRanges, ingredientList)


def count_fresh_ingredients(
    freshIngredientRanges: List[Tuple[int, int]],
    ingredientList: List[str],
) -> int:
    count = 0
    for ingredient in ingredientList:
        for range in freshIngredientRanges:
            if range[0] <= int(ingredient) <= range[1]:
                count += 1
                break
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
