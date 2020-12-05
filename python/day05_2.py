from day05_1 import get_pass_id
from itertools import combinations


if __name__ == '__main__':
    with open('../data/input05.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    pass_ids = {line: get_pass_id(line) for line in lines}
    diff_of_twos = [
        combo
        for combo in combinations(pass_ids.values(), 2)
        if abs(combo[0] - combo[1]) == 2
    ]
    print(len(diff_of_twos))  # 836
    sorted_diff_of_twos = [(diff[0], diff[1]) if diff[0] < diff[1] else (diff[1], diff[0]) for diff in diff_of_twos]
    possible_seats = []

    column_reps = ['LLL', 'LLR', 'LRL', 'LRR', 'RLL', 'RLR', 'RRL', 'RRR']

    for row in range(128):
        row_rep = str(bin(row))[2:].replace('1', 'B').replace('0', 'F')
        row_rep = 'F' * (7 - len(row_rep)) + row_rep
        for column, column_rep in enumerate(column_reps):
            seat_rep = row_rep + column_rep
            pass_id = row * 8 + column

            if pass_id - 1 in pass_ids.values() and pass_id + 1 in pass_ids.values() and seat_rep not in pass_ids:
                possible_seats.append(pass_id)

    print(len(possible_seats))
    print(possible_seats)
