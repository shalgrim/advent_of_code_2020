def get_row(row_spec):
    binary_rep = row_spec.replace('B', '1').replace('F', '0')
    return int(binary_rep, 2)


def get_column(column_spec):
    binary_rep = column_spec.replace('R', '1').replace('L', '0')
    return int(binary_rep, 2)


def get_pass_id(specification):
    row = get_row(specification[:7])
    column = get_column(specification[7:])
    return row * 8 + column


if __name__ == '__main__':
    with open('../data/input05.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    pass_ids = [get_pass_id(line) for line in lines]
    print(max(pass_ids))
