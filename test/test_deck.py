import random
from typing import List, Optional
from src.card import Card
from src.deck import Deck


cards = [Card(3), Card(10), Card(7), Card(55), Card(99)]


def test_init():
    d = Deck(cards=cards)
    assert d.cards == cards


def test_init_shuffle():
    """Проверяем, что карт столько же, но они в другом порядке."""
    full_deck1 = Deck(None)
    full_deck2 = Deck(None)
    assert len(full_deck1.cards) == len(full_deck2.cards)
    assert full_deck1.cards != full_deck2.cards


def test_save():
    d = Deck(cards=cards)
    assert d.save() == '[3<1>] [10<3>] [7<1>] [55<7>] [99<5>]'

    d = Deck(cards=[])
    assert d.save() == ''


def test_load():
    d = Deck.load('[3<1>] [10<3>] [7<1>] [55<7>] [99<5>]')
    expected_deck = Deck(cards)
    assert d == expected_deck


def test_draw_card():
    d1 = Deck(cards=[Card(3), Card(10), Card(7)])
    assert d1.draw_card() == Card(7)
    assert len(d1.cards) == 2
    assert d1.draw_card() == Card(10)
    assert len(d1.cards) == 1
    assert d1.draw_card() == Card(3)
    assert d1.draw_card() is None


def test_shuffle_1():
    deck = Deck(cards=cards.copy())
    deck_list = [deck.save()]
    for _ in range(5):
        deck.shuffle()
        s = deck.save()
        assert s not in deck_list
        deck_list.append(s)





# import pytest
# from src.deck import Deck
# from src.card import Card
#
#
# def test_init():
#     deck = Deck()
#     assert len(deck.cards) == 104
#     original_cards = set(Card.all_cards())
#     deck_cards = set(deck.cards)
#     assert deck_cards == original_cards
#
#
# def test_draw_card():
#     deck = Deck()
#     initial_size = len(deck.cards)
#     drawn_card = deck.draw_card()
#     assert len(deck.cards) == initial_size - 1
#     assert drawn_card not in deck.cards  # снята с колоды
#
#
# def test_shuffle():
#     # колода перемешивается shuffle
#     deck = Deck()
#     first_card = deck.cards[0]
#     deck.shuffle()
#     assert deck.cards[0] != first_card  # Исходная первая карта должна измениться
#
