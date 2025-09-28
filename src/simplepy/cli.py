from . import greet


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(prog="simplepy", description="Simple greeter")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    args = parser.parse_args()

    print(greet(args.name))


if __name__ == "__main__":
    main()
