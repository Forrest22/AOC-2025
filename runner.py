import importlib
import os
import pkgutil
from concurrent.futures import ProcessPoolExecutor, as_completed


def load_input(day: int) -> str:
    path = os.path.join("inputs", f"day{day:02d}.txt")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing input file: {path}")
    with open(path, "r") as f:
        return f.read().rstrip("\n")


def run_day(day: int, part: int | None = None) -> None:
    """
    Loads the function for the specific day, the input data, and runs the solver
    input: 1) day, an integer indicating which day to run and 2) part (optional, will run both if left empty), which part to run
    """
    module_name = f"days.day{day:02d}"

    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Module for day {day} not found ({module_name}).")
        return

    missing = [p for p in ("solve_part1", "solve_part2") if not hasattr(module, p)]
    if missing:
        print(f"Module {module_name} is missing: {', '.join(missing)}")
        return

    input_data = load_input(day)

    print(f"--- Day {day:02d} ---")

    if part in (None, 1):
        part1 = module.solve_part1(input_data)
        print(f"Part 1: {part1}")

    if part in (None, 2):
        part2 = module.solve_part2(input_data)
        print(f"Part 2: {part2}")


def _run_single_day_for_pool(day: int) -> tuple[int, str, str]:
    """
    This helper runs inside a separate process for each day.
    It returns results in a structured form.
    TODO: Make each part run in parallel.
    """
    module_name = f"days.day{day:02d}"
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        return day, None, None  # Day missing

    input_data = load_input(day)

    part1 = module.solve_part1(input_data)
    part2 = module.solve_part2(input_data)

    return day, part1, part2


def discover_available_days():
    """Scan the days/ folder for dayXX.py files"""
    import days

    day_ids = []
    for m in pkgutil.iter_modules(days.__path__):
        if m.name.startswith("day") and m.name[3:].isdigit():
            day_ids.append(int(m.name[3:]))
    return sorted(day_ids)


def run_all(max_workers: int | None = None):
    """
    Runs all discovered dayXX modules in parallel.
    Prints results in order after all jobs complete.
    input: The maximum number of processes that can be used to execute the given calls. If None or not given then as many worker processes will be created as the machine has processors.
    TODO: Improve formatting so that it updates a table when each day finishes and display them in order, rather than the current waiting until all finish.
    """
    day_ids = discover_available_days()

    print(f"Running {len(day_ids)} days in parallel...")

    results = {}
    with ProcessPoolExecutor(max_workers=max_workers) as exe:
        future_map = {exe.submit(_run_single_day_for_pool, d): d for d in day_ids}

        for future in as_completed(future_map):
            day = future_map[future]
            try:
                d, part1, part2 = future.result()
                results[d] = (part1, part2)
            except Exception as e:
                results[day] = (None, None)
                print(f"Day {day:02d} crashed: {e}")

    # Print results sorted by day
    print("\n=== All Days Complete ===")
    for d in sorted(results):
        p1, p2 = results[d]
        print(f"Day {d:02d}: Part1={p1}, Part2={p2}")

    return
