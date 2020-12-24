ALL_TILES = []


class Tile:
    def __init__(self):
        self.color = 'white'
        self.directions = {'e': None, 'se': None, 'sw': None, 'w': None, 'nw': None, 'ne': None}
        ALL_TILES.append(self)

    def set_from_direction(self, direction, tile):
        if direction == 'e':
            self.directions['w'] = tile
        elif direction == 'w':
            self.directions['e'] = tile
        elif direction == 'nw':
            self.directions['se'] = tile
        elif direction == 'ne':
            self.directions['sw'] = tile
        elif direction == 'sw':
            self.directions['ne'] = tile
        elif direction == 'se':
            self.directions['nw'] = tile

    @property
    def neighbors(self):
        return {k: v for k, v in self.directions.items() if v}

    def discover(self):
        old_neighbors = 0

        while len(self.neighbors) > old_neighbors:
            old_neighbors = len(self.neighbors)
            for direction, tile in self.neighbors.items():
                if direction == 'e':
                    if not self.directions['ne'] and tile.directions['nw']:
                        self.directions['ne'] = tile.directions['nw']
                        tile.directions['nw'].set_from_direction('ne', self)
                    if not self.directions['se'] and tile.directions['sw']:
                        self.directions['se'] = tile.directions['sw']
                        tile.directions['sw'].set_from_direction('se', self)

                elif direction == 'se':
                    if not self.directions['e'] and tile.directions['ne']:
                        self.directions['e'] = tile.directions['ne']
                        tile.directions['ne'].set_from_direction('e', self)
                    if not self.directions['sw'] and tile.directions['w']:
                        self.directions['sw'] = tile.directions['w']
                        tile.directions['w'].set_from_direction('sw', self)

                elif direction == 'sw':
                    if not self.directions['se'] and tile.directions['e']:
                        self.directions['se'] = tile.directions['e']
                        tile.directions['e'].set_from_direction('se', self)
                    if not self.directions['w'] and tile.directions['nw']:
                        self.directions['w'] = tile.directions['nw']
                        tile.directions['nw'].set_from_direction('w', self)

                elif direction == 'w':
                    if not self.directions['sw'] and tile.directions['se']:
                        self.directions['sw'] = tile.directions['se']
                        tile.directions['se'].set_from_direction('sw', self)
                    if not self.directions['nw'] and tile.directions['ne']:
                        self.directions['nw'] = tile.directions['ne']
                        tile.directions['ne'].set_from_direction('nw', self)

                elif direction == 'nw':
                    if not self.directions['w'] and tile.directions['sw']:
                        self.directions['w'] = tile.directions['sw']
                        tile.directions['sw'].set_from_direction('w', self)
                    if not self.directions['ne'] and tile.directions['e']:
                        self.directions['ne'] = tile.directions['e']
                        tile.directions['e'].set_from_direction('ne', self)

                elif direction == 'ne':
                    if not self.directions['nw'] and tile.directions['w']:
                        self.directions['nw'] = tile.directions['w']
                        tile.directions['w'].set_from_direction('nw', self)

                    if not self.directions['e'] and tile.directions['se']:
                        self.directions['e'] = tile.directions['se']
                        tile.directions['se'].set_from_direction('e', self)

    def traverse(self, line):
        if len(line) == 0:
            return self

        if line[0] in ['e', 'w']:
            direction = line[0]
            remainder = line[1:]
        else:
            direction = line[:2]
            remainder = line[2:]

        if self.directions[direction]:
            return self.directions[direction].traverse(remainder)

        new_tile = Tile()
        new_tile.set_from_direction(direction, self)
        self.directions[direction] = new_tile
        new_tile.discover()
        return new_tile.traverse(remainder)

    def flip(self):
        self.color = 'black' if self.color == 'white' else 'white'


def main(lines):
    reference_tile = Tile()
    for line in lines:
        tile_to_flip = reference_tile.traverse(line)
        tile_to_flip.flip()

    return sum([1 for tile in ALL_TILES if tile.color == 'black'])


if __name__ == '__main__':
    with open('../data/input24.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(main(lines))
