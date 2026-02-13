import importlib
import itertools
import os
import pkgutil
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def load_input(day: int) -> str:
    path = os.path.join("inputs", f"day{day:02d}.txt")
    if not os.path.exists(path):
        raise FileNotFoundError(f"missing input file: {path}")
    with open(path, "r") as f:
        return f.read().rstrip("\n")


def run_day(day: int, part: int | None = None) -> None:
    """
    loads the function for the specific day, the input data, and runs the solver
    input: 1) day, an integer indicating which day to run and 
    2) part (optional, will run both if left empty), which part to run
    """
    module_name = f"days.day{day:02d}"

    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"module for day {day} not found ({module_name}).")
        return

    missing = [p for p in ("solve_part1", "solve_part2") if not hasattr(module, p)]
    if missing:
        print(f"module {module_name} is missing: {', '.join(missing)}")
        return

    try:
        input_data = load_input(day)
    except:
        print("error finding input file for day", day)
        return

    print(f"--- day {day:02d} ---")

    if part in (None, 1):
        part1 = module.solve_part1(input_data)
        print(f"part 1: {part1}")

    if part in (None, 2):
        part2 = module.solve_part2(input_data)
        print(f"part 2: {part2}")


def _run_single_day_for_pool(day: int):
    start = time.perf_counter()

    module_name = f"days.day{day:02d}"
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        return day, None, None, None  # missing module

    input_data = load_input(day)

    part1 = module.solve_part1(input_data)
    part2 = module.solve_part2(input_data)

    duration = time.perf_counter() - start
    return day, part1, part2, duration


def discover_available_days():
    """scan the days/folder for day_xx.py files"""
    import days

    day_ids = []
    for m in pkgutil.iter_modules(days.__path__):
        if m.name.startswith("day") and m.name[3:].isdigit():
            day_ids.append(int(m.name[3:]))
    return sorted(day_ids)


def run_all(max_workers: int | None = None):
    day_ids = discover_available_days()

    print(f"running {len(day_ids)} days in parallel...\n")

    status = {
        d: {
            "done": False,
            "part1": "",
            "part2": "",
            "time": 0.0,
            "error": None,
        }
        for d in day_ids
    }

    spinner_cycle = itertools.cycle(["|", "/", "-", "\\"])

    def render():
        # Move cursor to top instead of clearing (less flicker)
        print("\033[H", end="")

        print("Advent of Code — Parallel Run\n")
        print(f"{'Day':>4}  {'St':^3}  {'Part 1':>15}  {'Part 2':>15}  {'Time(s)':>8}")
        print("-" * 55)

        spin_char = next(spinner_cycle)

        for d in sorted(status):
            info = status[d]

            if info["done"]:
                if info["error"]:
                    state = "X"
                    p1 = p2 = "-"
                    runtime = "-"
                else:
                    state = "✓"
                    p1 = str(info["part1"])
                    p2 = str(info["part2"])
                    runtime = f"{info['time']:.3f}"
            else:
                state = spin_char
                p1 = p2 = runtime = ""

            print(f"{d:>4}  {state:^3}  {p1:>15}  {p2:>15}  {runtime:>8}")

        sys.stdout.flush()

    # Clear once before starting
    print("\033[2J")  # Clear screen

    with ProcessPoolExecutor(max_workers=max_workers) as exe:
        future_map = {exe.submit(_run_single_day_for_pool, d): d for d in day_ids}

        while future_map:
            done_now = []

            for future in list(future_map):
                if future.done():
                    day = future_map.pop(future)
                    try:
                        d, part1, part2, duration = future.result()
                        status[d]["done"] = True
                        status[d]["part1"] = part1
                        status[d]["part2"] = part2
                        status[d]["time"] = duration
                    except Exception as e:
                        status[day]["done"] = True
                        status[day]["error"] = str(e)

            render()
            time.sleep(0.2)

    print("\nAll days complete!")
    """
    runs all discovered day_xx modules in parallel.
    prints results in order after all jobs complete.
    input: the maximum number of processes that can be used to execute the given calls.
    if None or not given then as many worker processes will be created as the machine has processors
    todo: improve formatting so that it updates a table when each day is running/completed 
    and display them in order, rather than the current waiting until all finish.
    """
    day_ids = discover_available_days()

    print(f"running {len(day_ids)} days in parallel...")

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
                print(f"day {day:02d} crashed: {e}")

    # print results sorted by day
    print("\n=== all days complete ===")
    for d in sorted(results):
        p1, p2 = results[d]
        print(f"day {d:02d}: part1={p1}, part2={p2}")
