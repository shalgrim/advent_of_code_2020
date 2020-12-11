from file_ops import readlines


def num_can_see_occupied(row, column, lines):
    num_occupied = 0

    # Northwest
    lookcolumn = column
    for lookrow in range(row - 1, -1, -1):
        lookcolumn -= 1
        if lookcolumn < 0:
            break
        seen = lines[lookrow][lookcolumn]
        if seen in ('#', 'L'):
            if seen == '#':
                num_occupied += 1
            break

    # North
    for lookrow in range(row - 1, -1, -1):
        seen = lines[lookrow][column]
        if seen in ('#', 'L'):
            if seen == '#':
                num_occupied += 1
            break

    # Northeast
    lookcolumn = column
    for lookrow in range(row - 1, -1, -1):
        lookcolumn += 1
        try:
            seen = lines[lookrow][lookcolumn]
        except IndexError:
            break
        else:
            if seen in ('#', 'L'):
                if seen == '#':
                    num_occupied += 1
                break

    # East
    for lookcolumn in range(column + 1, len(lines[0])):
        seen = lines[row][lookcolumn]
        if seen in ('#', 'L'):
            if seen == '#':
                num_occupied += 1
            break

    # Southeast
    lookcolumn = column
    for lookrow in range(row + 1, len(lines)):
        lookcolumn += 1
        try:
            seen = lines[lookrow][lookcolumn]
        except IndexError:
            break
        else:
            if seen in ('#', 'L'):
                if seen == '#':
                    num_occupied += 1
                break

    # South
    for lookrow in range(row + 1, len(lines)):
        seen = lines[lookrow][column]
        if seen in ('#', 'L'):
            if seen == '#':
                num_occupied += 1
            break

    # Southwest
    lookcolumn = column
    for lookrow in range(row + 1, len(lines)):
        lookcolumn -= 1
        if lookcolumn < 0:
            break
        seen = lines[lookrow][lookcolumn]
        if seen in ('#', 'L'):
            if seen == '#':
                num_occupied += 1
            break

    # West
    for lookcolumn in range(column - 1, -1, -1):
        seen = lines[row][lookcolumn]
        if seen in ('#', 'L'):
            if seen == '#':
                num_occupied += 1
            break

    return num_occupied


def should_become_occupied(row, column, lines):
    return num_can_see_occupied(row, column, lines) == 0


def should_become_empty(row, column, lines):
    return num_can_see_occupied(row, column, lines) >= 5


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
