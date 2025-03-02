def read_file(filepath, mode='r'):
    with open(filepath, mode) as f:
        return f.read()
