import re
from copy import copy

from day20_1 import Arrangement, build_solved_square
from file_ops import read

SEA_MONSTER_PATTERN = re.compile(r'#....##....##....###')


def arrange_image(image, arrangement):
    # TODO: DRY with ArrangedTile.arranged_lines
    if arrangement == Arrangement.NORMAL:
        return copy(image)
    elif arrangement == Arrangement.ROT90:
        new_lines = []
        for i in range(len(image)):
            new_lines.append(''.join([line[i] for line in image[::-1]]))
        return new_lines
    elif arrangement == Arrangement.ROT180:
        new_lines = []
        for line in image[::-1]:
            new_lines.append(line[::-1])
        return new_lines
    elif arrangement == Arrangement.ROT270:
        new_lines = []
        for i in range(len(image) - 1, -1, -1):
            new_lines.append(''.join([line[i] for line in image]))
        return new_lines
    elif arrangement == Arrangement.FLIPPED:
        return [line[::-1] for line in image]
    elif arrangement == Arrangement.FLIPPED90:
        new_lines = []
        for i in range(len(image) - 1, -1, -1):
            new_lines.append(''.join(line[i] for line in image[::-1]))
        return new_lines
    elif arrangement == Arrangement.FLIPPED180:
        return image[::-1]
    elif arrangement == Arrangement.FLIPPED270:
        new_lines = []
        for i in range(len(image)):
            new_lines.append(''.join([line[i] for line in image]))
        return new_lines


def count_sea_monsters_arranged(image, arrangement):
    arranged_image = arrange_image(image, arrangement)
    monsters = 0

    for i, row in enumerate(arranged_image):
        if i == 0 or i == len(arranged_image) - 1:
            continue
        match = SEA_MONSTER_PATTERN.search(row)
        while match:
            start = match.start()
            other_chars = [arranged_image[i - 1][start + 18]]
            other_chars.append(arranged_image[i + 1][start + 1])
            other_chars.append(arranged_image[i + 1][start + 4])
            other_chars.append(arranged_image[i + 1][start + 7])
            other_chars.append(arranged_image[i + 1][start + 10])
            other_chars.append(arranged_image[i + 1][start + 16])
            if all(c == '#' for c in other_chars):
                monsters += 1
            match = SEA_MONSTER_PATTERN.search(row, start+1)

    return monsters


def count_sea_monsters(image):
    answers = []
    for arrangement in Arrangement:
        answers.append(count_sea_monsters_arranged(image, arrangement))
    return max(answers)


def calculate_water_roughness(image):
    total_hashes = sum([line.count('#') for line in image])
    num_sea_monsters = count_sea_monsters(image)
    return total_hashes - num_sea_monsters * 15


def main(txt):
    square = build_solved_square(txt)
    image = square.to_image()
    return calculate_water_roughness(image)


if __name__ == '__main__':
    txt = read(20)
    print(main(txt))
