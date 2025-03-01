import sys
from app.src.init import init


def main():
    commands = sys.argv[1:]
    print(commands)
    if commands:
        command = commands[0]
        if command == "init":
            init()
        else:
            raise RuntimeError(f"Invalid command {commands}")
    else:
        raise RuntimeError("No command provided")


if __name__ == "__main__":
    main()
