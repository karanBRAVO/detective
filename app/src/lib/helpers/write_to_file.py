def write_to_file(filepath, data, mode='w'):
    with open(filepath, mode) as f:
        f.write(data)
