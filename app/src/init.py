from app.src.lib.constants import DETECTIVE_DIR
from app.src.lib.helpers.make_dirs import make_dirs
from app.src.lib.helpers.write_to_file import write_to_file


def init():
    make_dirs(f"{DETECTIVE_DIR}",
              f"{DETECTIVE_DIR}/objects",
              f"{DETECTIVE_DIR}/refs")
    write_to_file(f"{DETECTIVE_DIR}/HEAD", "ref: refs/heads/main\n")
    print(f"Initialized empty Git repository in {DETECTIVE_DIR}/")
