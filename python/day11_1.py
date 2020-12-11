from file_ops import readlines


def is_left_occupied(row, column, lines):
    if column > 0 and lines[row][column - 1] == '#':
        return True
    return False


def is_right_occupied(row, column, lines):
    if column < len(lines[0]) - 1 and lines[row][column + 1] == '#':
        return True
    return False


def is_up_occupied(row, column, lines):
    if row > 0 and lines[row - 1][column] == '#':
        return True
    return False


def is_down_occupied(row, column, lines):
    if row < len(lines) - 1 and lines[row + 1][column] == '#':
        return True
    return False


def should_become_occupied(row, column, lines):
    return num_adjacent_occupied(row, column, lines) == 0


def should_become_empty(row, column, lines):
    return num_adjacent_occupied(row, column, lines) >= 4


def num_adjacent_occupied(row, column, lines):
    seats = []
    if row > 0:
        seats += lines[row - 1][max(0, column - 1) : column + 2]

    if column > 0:
        seats.append(lines[row][column - 1])

    try:
        seats.append(lines[row][column + 1])
    except IndexError:
        pass

    try:
        lower_row = lines[row + 1]
    except IndexError:
        pass
    else:
        seats += lower_row[max(0, column - 1) : column + 2]

    return ''.join(seats).count('#')


def main(lines):
    changes = True

    while changes:
        changes = False
        newlines = []
        for row, line in enumerate(lines):
            newline = ''
            for column, character in enumerate(line):
                if character == '.':
                    newline += '.'
                elif character == 'L':
                    if should_become_occupied(row, column, lines):
                        newline += '#'
                        changes = True
                    else:
                        newline += 'L'
                elif character == '#':
                    if should_become_empty(row, column, lines):
                        newline += 'L'
                        changes = True
                    else:
                        newline += '#'

            newlines.append(newline)
        lines = newlines

    occupied_per_row = [line.count('#') for line in lines]
    return sum(occupied_per_row)


if __name__ == '__main__':
    lines = readlines(11)
    print(main(lines))
