import os
from app.src.lib.helpers.encode import encode
from app.src.lib.helpers.compress import compress
from app.src.lib.helpers.make_dirs import make_dirs
from app.src.lib.helpers.read_file import read_file
from app.src.lib.helpers.object_path import object_path
from app.src.lib.helpers.compute_sha1 import compute_sha1
from app.src.lib.helpers.write_to_file import write_to_file
from app.src.lib.constants import DETECTIVE_DIR


def write_tree():
    # TODO: Add a step to check staged files/directories
    cwd = os.getcwd()
    tree_hash = build_tree(cwd)
    print(tree_hash)


def build_tree(directory):
    entries = []

    for entry in sorted(os.listdir(directory)):
        if entry == DETECTIVE_DIR:
            continue

        entry_path = os.path.join(directory, entry)

        if os.path.isdir(entry_path):
            subtree_hash = build_tree(entry_path)
            entries.append((b"40000", encode(entry), subtree_hash))

        else:
            data = read_file(entry_path, "rb")
            object_hash = hash("blob", data)
            entries.append((b"100644", encode(entry), object_hash))

    tree_content = b""
    for mode, name, sha in entries:
        sha_binary = bytes.fromhex(sha)
        tree_content += mode + b" " + name + b"\x00" + sha_binary

    tree_hash = hash("tree", tree_content)
    return tree_hash


def hash(type, data, write=True):
    header = encode(f"{type} {len(data)}") + b"\0"
    store_data = header + data
    hash_object = compress(store_data)
    obj_hash = compute_sha1(hash_object)

    if write:
        obj_path = object_path(obj_hash)
        make_dirs(os.path.dirname(obj_path))
        write_to_file(obj_path, hash_object, "wb")

    return obj_hash
