from copy import copy

from day24_1 import get_part1_tiles, count_black


def generate_neighbors(x, y, z):
    return [
        (x + 1, y - 1, z),
        (x - 1, y + 1, z),
        (x, y - 1, z + 1),
        (x, y + 1, z - 1),
        (x + 1, y, z - 1),
        (x - 1, y, z + 1),
    ]


def rearrange(tiles):
    to_flip_black = set()
    to_flip_white = set()

    for coordinates, tile in copy(tiles).items():
        if tile == 'white':
            continue
        neighbor_coordinates = generate_neighbors(*coordinates)
        neighbors = [tiles[nc] for nc in neighbor_coordinates]
        if tile == 'black' and neighbors.count('black') not in [1, 2]:
            to_flip_white.add(coordinates)

    for coordinates, tile in copy(tiles).items():
        if tile == 'black':
            continue
        neighbor_coordinates = generate_neighbors(*coordinates)
        neighbors = [tiles[nc] for nc in neighbor_coordinates]
        if tile == 'white' and neighbors.count('black') == 2:
            to_flip_black.add(coordinates)

    for coordinates in to_flip_white:
        tiles[coordinates] = 'white'

    for coordinates in to_flip_black:
        tiles[coordinates] = 'black'


def main(lines, days):
    tiles = get_part1_tiles(lines)
    for _ in range(days):
        rearrange(tiles)

    return count_black(tiles)


if __name__ == '__main__':
    with open('../data/input24.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines, 100))
