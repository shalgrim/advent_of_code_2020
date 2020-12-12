from file_ops import readlines


def reverse(x, y, way_x, way_y):
    return x, y, -way_x, -way_y


def move_clockwise(x, y, way_x, way_y):
    return x, y, -way_y, way_x


def move_counterclockwise(x, y, way_x, way_y):
    return x, y, way_y, -way_x


def move_waypoint(command, number, x, y, way_x, way_y):
    if command == 'N':
        return x, y, way_x, way_y-number
    elif command == 'E':
        return x, y, way_x+number, way_y
    elif command == 'S':
        return x, y, way_x, way_y+number
    elif command == 'W':
        return x, y, way_x-number, way_y
    elif command == 'R':
        if number == 180:
            return reverse(x, y, way_x, way_y)
        elif number == 90:
            return move_clockwise(x, y, way_x, way_y)
        elif number == 270:
            return move_counterclockwise(x, y, way_x, way_y)
        else:
            raise Exception('why am i here')
    elif command == 'L':
        if number == 180:
            return reverse(x, y, way_x, way_y)
        elif number == 90:
            return move_counterclockwise(x, y, way_x, way_y)
        elif number == 270:
            return move_clockwise(x, y, way_x, way_y)
        else:
            raise Exception('why am i here')

    elif command == 'F':
        return x + number * way_x, y + number * way_y, way_x, way_y
    else:
        raise Exception('why am i here')


def main(lines):
    instructions = [(line[0], int(line[1:])) for line in lines]
    x = 0
    y = 0
    way_x = 10
    way_y = -1

    for command, number in instructions:
        x, y, way_x, way_y = move_waypoint(command, number, x, y, way_x, way_y)

    print(x, y)
    answer = abs(x) + abs(y)
    return answer


if __name__ == '__main__':
    lines = readlines(12)
    print(main(lines))
