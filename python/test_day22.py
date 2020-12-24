from unittest import TestCase


from day22_1 import decks_from_file, play_game, score_deck, main
from day22_2 import play_recursive_game


class TestDay22(TestCase):
    def test_decks_from_file(self):
        deck1, deck2 = decks_from_file('../data/test22.txt')
        self.assertEqual([9, 2, 6, 3, 1], deck1)
        self.assertEqual([5, 8, 4, 7, 10], deck2)

    def test_score_deck(self):
        self.assertEqual(306, score_deck([3, 2, 10, 6, 8, 5, 9, 4, 7, 1]))
        self.assertEqual(291, score_deck([7, 5, 6, 2, 4, 1, 10, 8, 9, 3]))

    def test_part1(self):
        deck1, deck2 = decks_from_file('../data/test22.txt')
        deck1, deck2 = play_game(deck1, deck2)
        self.assertEqual([], deck1)
        self.assertEqual([3, 2, 10, 6, 8, 5, 9, 4, 7, 1], deck2)
        self.assertEqual(35370, main())

    def test_part2(self):
        deck1, deck2 = decks_from_file('../data/test22.txt')
        winner, winning_deck = play_recursive_game(deck1, deck2)
        self.assertEqual(2, winner)
        self.assertEqual([7, 5, 6, 2, 4, 1, 10, 8, 9, 3], winning_deck)
        self.assertEqual(291, score_deck(winning_deck))
