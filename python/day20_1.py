import math
from collections import defaultdict
from copy import deepcopy, copy
from datetime import datetime
from enum import Enum, auto
from itertools import chain

from file_ops import read


def text_to_tiles(txt):
    tiles = {}
    blocks = txt.split('\n\n')
    for block in blocks:
        if not block.strip():
            continue
        lines = [line.strip() for line in block.split('\n')]
        tile_num = int((lines[0].split()[1][:-1]))
        tiles[tile_num] = [line for line in lines[1:] if line]

    return tiles


def main_first_thought(txt):
    tiles = text_to_tiles(txt)
    lefts = {k: ''.join([line[0] for line in v]) for k, v in tiles.items()}
    rights = {k: ''.join([line[-1] for line in v]) for k, v in tiles.items()}
    tops = {k: v[0] for k, v in tiles.items()}
    bottoms = {k: v[-1] for k, v in tiles.items()}

    rights_matching_lefts = defaultdict(list)
    for right_num, right in rights.items():
        for left_num, left in lefts.items():
            if right == left:
                rights_matching_lefts[right_num].append(left_num)

    rights_matching_flipped_rights = defaultdict(list)
    for right_num, right in rights.items():
        for flipped_right_num, flipped_right in rights.items():
            if right == reversed(flipped_right):
                rights_matching_flipped_rights[right_num].append(flipped_right_num)

    bottoms_matching_tops = defaultdict(list)
    for bottom_num, bottom in bottoms.items():
        for top_num, top in tops.items():
            if bottom == top:
                bottoms_matching_tops[bottom_num].append(top_num)

    bottoms_matching_flipped_bottoms = defaultdict(list)
    for bottom_num, bottom in bottoms.items():
        for flipped_bottom_num, flipped_bottom in bottoms.items():
            if bottom == reversed(flipped_bottom):
                bottoms_matching_flipped_bottoms[bottom_num].append(flipped_bottom_num)

    print('hello')


def find_first_blank(square):
    for x, row in enumerate(square):
        for y, column in enumerate(row):
            if column is None:
                return x, y


def does_fit(tiles, tile, square, first_blank, orientation):
    # the first thing to do here is to calculate the tile's top and left based on orientation for easier comparison
    if first_blank[0] > 0:
        above_tile = square[first_blank[0] - 1][first_blank[1]]
        above_row = (
            tiles[above_tile][-1]
            if above_tile > 0
            else reversed(tiles[abs(above_tile)][0])
        )
        top_row = reversed(tile[-1]) if flipped else tile[0]

        if above_row != top_row:
            return False

    if first_blank[1] > 0:
        left_tile = square[first_blank[0]][first_blank[1] - 1]
        right_column = (
            ''.join([line[-1] for line in tiles[left_tile]])
            if left_tile > 0
            else ''.join([row[0] for row in tiles[abs(left_tile)][::-1]])
        )

        left_column = (
            ''.join([row[-1] for row in tile[::-1]])
            if flipped
            else ''.join([row[0] for row in tile])
        )

        if right_column != left_column:
            return False

    return True


def solve(tiles, square_in):
    square = deepcopy(square_in)
    first_blank = find_first_blank(square)
    all_used = {item for row in square for item in row}
    for num, tile in tiles.items():
        if num in all_used:
            continue

        # TODO: Instead of these two if statements, make a for loop through the flip/rotate enum
        if does_fit(tiles, tile, square, first_blank, flipped=False):

            # TODO: Square should have `place` method that takes a tile num, tile, and orientation
            # and in that method it should calculate the right and bottom column/row for easier comparison
            square[first_blank[0]][first_blank[1]] = num
            solution = solve(tiles, square)
            if solution:
                return solution
        if does_fit(tiles, tile, square, first_blank, flipped=True):
            square[first_blank[0]][first_blank[1]] = -num
            solution = solve(tiles, square)
            if solution:
                return solution
    return False


class Arrangement(Enum):
    NORMAL = auto()
    ROT90 = auto()
    ROT180 = auto()
    ROT270 = auto()
    FLIPPED = auto()
    FLIPPED90 = auto()
    FLIPPED180 = auto()
    FLIPPED270 = auto()


class ArrangedTile():
    def __init__(self, number, lines, arrangement):
        self.number = number
        self.lines = lines
        self.arrangement = arrangement

    def __repr__(self):
        return f'{self.number} {self.arrangement}'

    @property
    def arranged_lines(self):
        if self.arrangement == Arrangement.NORMAL:
            return self.lines
        elif self.arrangement == Arrangement.ROT90:
            new_lines = []
            for i in range(len(self.lines)):
                new_lines.append(''.join([line[i] for line in self.lines[::-1]]))
            return new_lines
        elif self.arrangement == Arrangement.ROT180:
            new_lines = []
            for line in self.lines[::-1]:
                new_lines.append(line[::-1])
            return new_lines
        elif self.arrangement == Arrangement.ROT270:
            new_lines = []
            for i in range(len(self.lines)-1, -1, -1):
                new_lines.append(''.join([line[i] for line in self.lines]))
            return new_lines
        elif self.arrangement == Arrangement.FLIPPED:
            return [line[::-1] for line in self.lines]
        elif self.arrangement == Arrangement.FLIPPED90:
            new_lines = []
            for i in range(len(self.lines)-1, -1, -1):
                new_lines.append(''.join(line[i] for line in self.lines[::-1]))
            return new_lines
        elif self.arrangement == Arrangement.FLIPPED180:
            return self.lines[::-1]
        elif self.arrangement == Arrangement.FLIPPED270:
            new_lines = []
            for i in range(len(self.lines)):
                new_lines.append(''.join([line[i] for line in self.lines]))
            return new_lines

    @property
    def image_lines(self):
        return [line[1:-1] for line in self.arranged_lines]

    @property
    def top(self):
        if self.arrangement == Arrangement.NORMAL:
            return list(self.lines[0])
        elif self.arrangement == Arrangement.ROT90:
            return [line[0] for line in self.lines[::-1]]
        elif self.arrangement == Arrangement.ROT180:
            return list(self.lines[-1][::-1])
        elif self.arrangement == Arrangement.ROT270:
            return [line[-1] for line in self.lines]
        elif self.arrangement == Arrangement.FLIPPED:
            return list(self.lines[0][::-1])
        elif self.arrangement == Arrangement.FLIPPED90:
            return [line[-1] for line in self.lines[::-1]]
        elif self.arrangement == Arrangement.FLIPPED180:
            return list(self.lines[-1])
        elif self.arrangement == Arrangement.FLIPPED270:
            return [line[0] for line in self.lines]

    @property
    def bottom(self):
        if self.arrangement == Arrangement.NORMAL:
            return list(self.lines[-1])
        elif self.arrangement == Arrangement.ROT90:
            return [line[-1] for line in self.lines[::-1]]
        elif self.arrangement == Arrangement.ROT180:
            return list(self.lines[0][::-1])
        elif self.arrangement == Arrangement.ROT270:
            return [line[0] for line in self.lines]
        elif self.arrangement == Arrangement.FLIPPED:
            return list(self.lines[-1][::-1])
        elif self.arrangement == Arrangement.FLIPPED90:
            return [line[0] for line in self.lines[::-1]]
        elif self.arrangement == Arrangement.FLIPPED180:
            return list(self.lines[0])
        elif self.arrangement == Arrangement.FLIPPED270:
            return [line[-1] for line in self.lines]

    @property
    def right(self):
        if self.arrangement == Arrangement.NORMAL:
            return [line[-1] for line in self.lines]
        elif self.arrangement == Arrangement.ROT90:
            return list(self.lines[0])
        elif self.arrangement == Arrangement.ROT180:
            return [line[0] for line in self.lines[::-1]]
        elif self.arrangement == Arrangement.ROT270:
            return list(self.lines[-1][::-1])
        elif self.arrangement == Arrangement.FLIPPED:
            return [line[0] for line in self.lines]
        elif self.arrangement == Arrangement.FLIPPED90:
            return list(self.lines[0][::-1])
        elif self.arrangement == Arrangement.FLIPPED180:
            return [line[-1] for line in self.lines[::-1]]
        elif self.arrangement == Arrangement.FLIPPED270:
            return list(self.lines[-1])

    @property
    def left(self):
        if self.arrangement == Arrangement.NORMAL:
            return [line[0] for line in self.lines]
        elif self.arrangement == Arrangement.ROT90:
            return list(self.lines[-1])
        elif self.arrangement == Arrangement.ROT180:
            return [line[-1] for line in self.lines[::-1]]
        elif self.arrangement == Arrangement.ROT270:
            return list(self.lines[0][::-1])
        elif self.arrangement == Arrangement.FLIPPED:
            return [line[-1] for line in self.lines]
        elif self.arrangement == Arrangement.FLIPPED90:
            return list(self.lines[-1][::-1])
        elif self.arrangement == Arrangement.FLIPPED180:
            return [line[0] for line in self.lines[::-1]]
        elif self.arrangement == Arrangement.FLIPPED270:
            return list(self.lines[0])


class Square:
    def __init__(self, size, tiles):
        self.size = size
        self.raw_tiles = tiles
        self.placed_tiles = []
        tile_row = [None] * self.size
        for _ in range(self.size):
            self.placed_tiles.append(copy(tile_row))

    @property
    def unused_tiles(self):
        return [
            tile_num
            for tile_num in self.raw_tiles
            if tile_num not in [t.number for t in chain(*self.placed_tiles) if t]
        ]

    def fits(self, tile_num, arrangement, x, y):
        arranged_tile = ArrangedTile(tile_num, self.raw_tiles[tile_num], arrangement)
        if y > 0 and arranged_tile.top != self.placed_tiles[y-1][x].bottom:
            return False
        if x > 0 and arranged_tile.left != self.placed_tiles[y][x-1].right:
            return False
        return True

    def place(self, tile_num, arrangement, x, y):
        self.placed_tiles[y][x] = ArrangedTile(tile_num, self.raw_tiles[tile_num], arrangement)

    def solve(self):
        if not self.unused_tiles:
            return True

        for y in range(self.size):
            for x in range(self.size):
                if self.placed_tiles[y][x]:
                    continue

                for tile_num in self.unused_tiles:
                    for arrangement in Arrangement:

                        if self.fits(tile_num, arrangement, x, y):
                            self.place(tile_num, arrangement, x, y)
                            if self.solve():
                                return True
                            else:
                                self.clear(x, y)

                if self.unused_tiles:
                    return False

    def clear(self, x, y):
        self.placed_tiles[y][x] = None

    def to_image(self):
        lines = []
        for row in self.placed_tiles:
            as_lines = [tile.image_lines for tile in row]
            for i in range(len(as_lines[0])):
                lines.append(''.join([tile[i] for tile in as_lines]))
        return lines

    def to_lines(self):
        """I don't think I want this"""
        lines = []
        for row in self.placed_tiles:
            as_lines = [tile.arranged_lines for tile in row]
            for i in range(len(as_lines[0])):
                lines.append(''.join([tile[i] for tile in row]))
        return lines


def main(txt):
    print(datetime.now())
    square = build_solved_square(txt)
    print(datetime.now())  # it only takes 32 seconds
    print(square)
    corners = [
        square.placed_tiles[0][0].number,
        square.placed_tiles[0][-1].number,
        square.placed_tiles[-1][0].number,
        square.placed_tiles[-1][-1].number,
    ]

    return math.prod(corners)


def build_solved_square(txt):
    tiles = text_to_tiles(txt)
    square_size = int(math.sqrt(len(tiles)))
    square = Square(square_size, tiles)
    square.solve()
    return square


if __name__ == '__main__':
    txt = read(20)
    print(main(txt))
