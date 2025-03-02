import hashlib


def compute_sha1(data):
    return hashlib.sha1(data).hexdigest()
