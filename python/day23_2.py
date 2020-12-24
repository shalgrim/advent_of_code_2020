from day23_1 import play_game


def main(cupstring, moves):
    cups = [int(c) for c in cupstring]
    max_cup = max(cups)
    for i in range(max_cup + 1, 1_000_001):
        cups.append(i)
    new_cups = play_game(cups, moves)
    index1 = new_cups.index(1)
    if index1 == len(new_cups) - 1:
        return new_cups[0] * new_cups[1]
    elif index1 == len(new_cups) - 2:
        return new_cups[0] * new_cups[-1]
    return new_cups[index1 + 1] * new_cups[index1 + 2]


if __name__ == '__main__':
    print(main('853192647', 10_000_000))
