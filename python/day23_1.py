from copy import copy


def convert_cups_to_answer(cups):
    one_index = cups.index(1)
    return ''.join([str(c) for c in cups[one_index + 1 :] + cups[:one_index]])


def play_game(cups, moves):
    current_cup_index = 0
    new_cups = copy(cups)
    for turn in range(moves):
        print(f'-- move {turn+1} --')
        new_cups, current_cup_index = move(new_cups, current_cup_index)

    return new_cups


def print_cup_string(cups, current_cup_index):
    cupstrings = ['cups:']
    for i, nc in enumerate(cups):
        if i == current_cup_index:
            cupstrings.append(f'({nc})')
        else:
            cupstrings.append(str(nc))

    print(' '.join(cupstrings))


def print_picked_up_string(picked_up):
    pustrings = [str(pu) for pu in picked_up]
    print('pick up: ' + ', '.join(pustrings))


def move(cups, current_cup_index):
    print_cup_string(cups, current_cup_index)
    current_cup = cups[current_cup_index]

    # Part 1
    pick_up_indexes = [
        current_cup_index + 1,
        current_cup_index + 2,
        current_cup_index + 3,
    ]
    pick_up_indexes = [pui % len(cups) for pui in pick_up_indexes]
    picked_up = [cups[pui] for pui in pick_up_indexes]
    print_picked_up_string(picked_up)
    new_circle = copy(cups)
    for pu in picked_up:
        new_circle.remove(pu)

    # Part 2
    destination_cup = current_cup - 1
    while destination_cup in picked_up and destination_cup > 0:
        destination_cup -= 1

    if destination_cup <= 0:
        destination_cup = max(new_circle)

    print(f'destination: {destination_cup}\n')

    destination_cup_index = new_circle.index(destination_cup)

    # Part 3
    new_circle = (
        new_circle[: destination_cup_index + 1]
        + picked_up
        + new_circle[destination_cup_index + 1 :]
    )

    # Part 4
    current_cup_index = new_circle.index(current_cup)
    new_current_cup_index = (current_cup_index + 1) % len(new_circle)

    return new_circle, new_current_cup_index


def main(cupstring, moves):
    cups = [int(c) for c in cupstring]
    new_cups = play_game(cups, moves)
    return convert_cups_to_answer(new_cups)


if __name__ == '__main__':
    print(main('853192647', 100))
