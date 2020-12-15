from collections import defaultdict


def play_game(starting_numbers, turns):
    memory = defaultdict(list)
    for i, number in enumerate(starting_numbers):
        memory[number].append(i + 1)

    turn = len(starting_numbers)

    while turn < turns:
        turn += 1
        if turn % 1_000_000 == 0:
            print(turn)

        if len(memory[number]) > 1:
            number = memory[number][-1] - memory[number][-2]
            memory[number].append(turn)
        else:
            number = 0
            memory[number].append(turn)

    return number


if __name__ == '__main__':
    print(play_game([0, 5, 4, 1, 10, 14, 7], 2020))
