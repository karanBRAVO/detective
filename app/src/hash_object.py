import os
from app.src.lib.constants import NULL_BYTE
from app.src.lib.helpers.encode import encode
from app.src.lib.helpers.compress import compress
from app.src.lib.helpers.read_file import read_file
from app.src.lib.helpers.make_dirs import make_dirs
from app.src.lib.helpers.path_exists import path_exists
from app.src.lib.helpers.object_path import object_path
from app.src.lib.helpers.compute_sha1 import compute_sha1
from app.src.lib.helpers.write_to_file import write_to_file


def hash_object(flag, filepath):
    if flag == "-w":
        if path_exists(filepath):
            data = read_file(filepath)
            header = f"blob {len(data)}{NULL_BYTE}"
            blob = header + data
            compressed_blob = compress(encode(blob))
            obj_hash = compute_sha1(compressed_blob)
            obj_path = object_path(obj_hash)
            make_dirs(os.path.dirname(obj_path))
            write_to_file(obj_path, compressed_blob, 'wb')
            print(obj_hash)
        else:
            raise RuntimeError(f"File {filepath} not found")
    else:
        raise RuntimeError(f"Unknown flag {flag}")
