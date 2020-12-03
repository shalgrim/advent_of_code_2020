def move(position, right, down):
    return position[0] + right, position[1] + down


def is_tree(position, lines):
    line = lines[position[1]]
    cell = line[position[0] % len(line)]
    return cell == '#'


if __name__ == '__main__':
    with open(f'../data/input03.txt') as f:
        lines = [line.strip()  for line in f.readlines()]

    right = 3
    down = 1
    position = (0, 0)
    width = len(lines[0])
    height = len(lines)
    num_trees = 0

    while position[1] < height:
        num_trees += 1 if is_tree(position, lines) else 0
        position = move(position, right, down)

    print(num_trees)



