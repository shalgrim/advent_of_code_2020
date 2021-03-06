from copy import copy

from day22_1 import decks_from_file, play_game, score_deck

game_number = 0


def play_recursive_game(d1, d2):
    global game_number
    game_number += 1
    this_game_number = game_number
    print(f'=== Game {this_game_number} ===')
    played_rounds = set()
    turn = 0

    while d1 and d2:
        turn += 1
        print()
        print(f'-- Round {turn} (Game {this_game_number}) --')
        print(f"Player 1's deck: {', '.join([str(c) for c in d1])}")
        print(f"Player 2's deck: {', '.join([str(c) for c in d2])}")
        if (tuple(d1), tuple(d2)) in played_rounds:
            print(f'The winner of {this_game_number} is player 1! (anti-infinite)')
            return 1, d1
        played_rounds.add((tuple(d1), tuple(d2)))
        c1 = d1.pop(0)
        print(f'Player 1 plays: {c1}')
        c2 = d2.pop(0)
        print(f'Player 2 plays: {c2}')

        if len(d1) >= c1 and len(d2) >= c2:
            print('Playing a sub-game to determine the winner...')
            print()
            round_winner, winning_deck = play_recursive_game(copy(d1)[:c1], copy(d2)[:c2])
        elif c1 > c2:
            round_winner = 1
        else:
            round_winner = 2

        print(f'Player {round_winner} wins round {turn} of game {this_game_number}!')

        if round_winner == 1:
            d1 += [c1, c2]
        else:
            d2 += [c2, c1]

    if d1:
        print(f'The winner of game {this_game_number} is player 1!')
        return 1, d1
    else:
        print(f'The winner of game {this_game_number} is player 2!')
        return 2, d2


def main():
    deck1, deck2 = decks_from_file('../data/input22.txt')
    winner, winning_deck = play_recursive_game(deck1, deck2)
    return score_deck(winning_deck)


if __name__ == '__main__':
    print(main())
