import os


def make_dirs(*args):
    for path in args:
        os.makedirs(path, exist_ok=True)
