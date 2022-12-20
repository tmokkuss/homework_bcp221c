def read_data(file_name):
    with open(file_name) as f:
        rows = f.read()
        return rows


def write_data(out_file, out):
    with open(out_file, 'w') as f:
        f.write(out)



