from app.src.lib.constants import DETECTIVE_DIR


def object_path(object_hash):
    return f"{DETECTIVE_DIR}/objects/{object_hash[:2]}/{object_hash[2:]}"
