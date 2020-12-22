def decks_from_file(fn):
    with open(fn) as f:
        txt = f.read()

    txt1, txt2 = txt.split('\n\n')
    deck1 = [int(line) for line in txt1.split('\n')[1:] if line]
    deck2 = [int(line) for line in txt2.split('\n')[1:] if line]
    return deck1, deck2


def play_game(d1, d2):
    turn = 0
    while d1 and d2:
        turn += 1
        print(f'-- Round {turn} --')
        print(f"Player 1's deck: {', '.join([str(c) for c in d1])}")
        print(f"Player 2's deck: {', '.join([str(c) for c in d2])}")
        c1 = d1.pop(0)
        print(f'Player 1 plays: {c1}')
        c2 = d2.pop(0)
        print(f'Player 2 plays: {c2}')
        if c1 > c2:
            print(f'Player 1 wins the round!')
            d1 += [c1, c2]
        else:
            print(f'Player 2 wins the round!')
            d2 += [c2, c1]
        print()
    return d1, d2


def score_deck(d):
    card_scores = [(i + 1) * v for i, v in enumerate(d[::-1])]
    return sum(card_scores)


def main():
    deck1, deck2 = decks_from_file('../data/input22.txt')
    deck1, deck2 = play_game(deck1, deck2)
    if deck1:
        return score_deck(deck1)
    else:
        return score_deck(deck2)


if __name__ == '__main__':
    print(main())
