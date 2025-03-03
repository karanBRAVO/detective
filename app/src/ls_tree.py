import binascii
from app.src.lib.helpers.decode import decode
from app.src.lib.helpers.encode import encode
from app.src.lib.helpers.read_file import read_file
from app.src.lib.helpers.decompress import decompress
from app.src.lib.helpers.object_path import object_path
from app.src.lib.constants import HASH_LEN, SHA_BYTES


def ls_tree(flag, tree_hash):
    if tree_hash and len(tree_hash) == HASH_LEN:
        # calculate the object path from tree hash
        # read the object file
        # decompress the object file
        # parse the data
        # print the data

        obj_path = object_path(tree_hash)
        bin_data = read_file(obj_path, "rb")

        # data -> b'tree <size>\0<mode> <filename>\0<sha-hash>...'
        data = decompress(bin_data)

        if data.startswith(b"tree"):
            null_byte_index = data.index(b"\x00")
            data = data[null_byte_index + 1:]

            entries = {
                "mode": [],
                "filename": [],
                "sha_hash": []
            }

            while data:
                mode_filename_index = data.index(b"\x00")

                mode, filename = data[:mode_filename_index].split(b" ")
                # 20 bytes sha-hash
                sha_bytes = data[mode_filename_index: mode_filename_index + SHA_BYTES + 1]
                sha_hash = binascii.hexlify(sha_bytes)

                entries["mode"].append(decode(mode))
                entries["filename"].append(decode(filename))
                entries["sha_hash"].append(decode(sha_hash))

                data = data[mode_filename_index + SHA_BYTES + 1:]

            if flag == "--name-only":
                print("\n".join(entries["filename"]))
            else:
                raise RuntimeError(f"Unknown flag {flag}")

        else:
            raise RuntimeError(f"Invalid tree hash {tree_hash}")

    else:
        raise RuntimeError(f"Invalid tree hash {tree_hash}")
