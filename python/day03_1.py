def move(position, right, down):
    return position[0] + right, position[1] + down


def is_tree(position, lines):
    line = lines[position[1]]
    cell = line[position[0] % len(line)]
    return cell == '#'


def count_trees(right, down, lines):
    position = (0, 0)
    height = len(lines)
    num_trees = 0
    while position[1] < height:
        num_trees += 1 if is_tree(position, lines) else 0
        position = move(position, right, down)

    return num_trees


if __name__ == '__main__':
    with open(f'../data/input03.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    right = 3
    down = 1
    num_trees = count_trees(right, down, lines)

    print(num_trees)
