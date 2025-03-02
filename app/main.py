import sys
from app.src.init import init
from app.src.cat_file import cat_file
from app.src.hash_object import hash_object


def main():
    commands = sys.argv[1:]

    if commands:
        command = commands[0]

        if command == "init":
            init()

        elif command == "cat-file":
            flag = commands[1]
            object_hash = commands[2]
            cat_file(flag, object_hash)

        elif command == "hash-object":
            flag = commands[1]
            file_path = commands[2]
            hash_object(flag, file_path)

        else:
            raise RuntimeError(f"Invalid command {command}")

    else:
        raise RuntimeError("No command provided")


if __name__ == "__main__":
    main()
