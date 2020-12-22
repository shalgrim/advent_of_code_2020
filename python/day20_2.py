from day20_1 import build_solved_square
from file_ops import read


def count_sea_monsters(image):
    return 2


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
