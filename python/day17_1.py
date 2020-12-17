import itertools

from file_ops import readlines


def list_neighbors(x, y, z):
    neighbors_inclusive = list(itertools.product([x-1, x, x+1], [y-1, y, y+1], [z-1, z, z+1]))
    neighbors_inclusive.remove((x, y, z))
    return neighbors_inclusive


def run_cycle(active_cubes):
    min_x = min(ac[0] for ac in active_cubes)
    max_x = max(ac[0] for ac in active_cubes)
    min_y = min(ac[1] for ac in active_cubes)
    max_y = max(ac[1] for ac in active_cubes)
    min_z = min(ac[2] for ac in active_cubes)
    max_z = max(ac[2] for ac in active_cubes)

    new_actives = set()

    for z in range(min_z-1, max_z+2):
        for y in range(min_y-1, max_y+2):
            for x in range(min_x-1, max_x+2):
                neighbors = list_neighbors(x, y, z)
                active_neighbors = [neighbor for neighbor in neighbors if neighbor in active_cubes]
                num_active_neighbors = len(active_neighbors)
                if (x, y, z) in active_cubes:
                    if num_active_neighbors in [2, 3]:
                        new_actives.add((x, y, z))
                elif (x, y, z) not in active_cubes and num_active_neighbors == 3:
                    new_actives.add((x, y, z))

    return new_actives


def get_active_cubes(active_cubes, num_cycles):
    for _ in range(num_cycles):
        active_cubes = run_cycle(active_cubes)

    return active_cubes


def count_active_cubes(active_cubes, num_cycles):
    return len(get_active_cubes(active_cubes, num_cycles))


def active_cubes_from_lines(lines):
    answer = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                answer.add((x, y, 0))

    return answer


if __name__ == '__main__':
    active_cubes = active_cubes_from_lines(readlines(17))
    print(count_active_cubes(active_cubes, 6))
