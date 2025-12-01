import sys
from runner import run_all, run_day


def main():
    if len(sys.argv) == 1:
        print("Usage:")
        print("  python main.py <day> [part]")
        print("Examples:")
        print("  python main.py 3        # run both parts")
        print("  python main.py 3 1      # run part 1 only")
        print("  python main.py 3 2      # run part 2 only")
        sys.exit()

    try:
        if len(sys.argv) == 2 and sys.argv[1] == "all":
            run_all()
            sys.exit()
    except Exception as e:
        print("Error with running all days.")
        print(e)
        return

    try:
        day = int(sys.argv[1])
    except ValueError:
        print("Day must be an integer.")
        return

    part = None
    if len(sys.argv) >= 3:
        try:
            part = int(sys.argv[2])
            if part not in (1, 2):
                raise ValueError
        except ValueError:
            print("Part must be 1 or 2.")
            return

    run_day(day, part)


if __name__ == "__main__":
    main()
