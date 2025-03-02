from app.src.lib.constants import NULL_BYTE, HASH_LEN
from app.src.lib.helpers.decode import decode
from app.src.lib.helpers.read_file import read_file
from app.src.lib.helpers.decompress import decompress
from app.src.lib.helpers.object_path import object_path


def cat_file(flag, object_hash):
    if flag == "-p":
        if object_hash and len(object_hash) == HASH_LEN:
            obj_path = object_path(object_hash)
            bin_data = read_file(obj_path, "rb")
            data = decode(decompress(bin_data))
            null_byte_index = data.find(NULL_BYTE)
            if null_byte_index != -1:
                data = data[null_byte_index + 1:]
                print(data)
        else:
            raise RuntimeError(f"Invalid object hash {object_hash}")
    else:
        raise RuntimeError(f"Unknown flag {flag}")
