from file_ops import readlines


def move(command, number, facing, x, y):
    if command == 'N':
        return facing, x, y-number
    elif command == 'E':
        return facing, x+number, y
    elif command == 'S':
        return facing, x, y+number
    elif command == 'W':
        return facing, x-number, y
    elif command == 'R':
        return (facing + number) % 360, x, y
    elif command == 'L':
        return (360 + facing - number) % 360, x, y
    elif command == 'F':
        if facing == 0:
            return move('E', number, facing, x, y)
        elif facing == 90:
            return move('S', number, facing, x, y)
        elif facing == 180:
            return move('W', number, facing, x, y)
        elif facing == 270:
            return move('N', number, facing, x, y)
        else:
            raise Exception('why am i here')
    elif command == 'B':
        if facing == 0:
            return move('W', number, facing, x, y)
        elif facing == 90:
            return move('N', number, facing, x, y)
        elif facing == 180:
            return move('E', number, facing, x, y)
        elif facing == 270:
            return move('S', number, facing, x, y)
        else:
            raise Exception('why am i here')
    else:
        raise Exception('why am i here')


def main(lines):
    instructions = [(line[0], int(line[1:])) for line in lines]
    facing = 0
    x = 0
    y = 0

    for command, number in instructions:
        facing, x, y = move(command, number, facing, x, y)

    print(x, y)
    answer = abs(x) + abs(y)
    return answer


if __name__ == '__main__':
    lines = readlines(12)
    print(main(lines))
