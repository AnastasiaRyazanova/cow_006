import pytest
from src.row import Row
from src.deck import Deck
from src.table import Table
from src.card import Card


def test_init():
    deck = Deck()
    assert len(deck.cards) == 104
    original_cards = set(Card.all_cards())
    deck_cards = set(deck.cards)
    assert deck_cards == original_cards


def test_draw_card(deck):
    deck = Deck()
    initial_size = len(deck.cards)
    drawn_card = deck.draw_card()
    assert len(deck.cards) == initial_size - 1
    assert drawn_card not in deck.cards  # снята с колоды


def test_shuffle(deck):
    # колода перемешивается
    deck = Deck()
    first_card = deck.cards[0]
    deck.shuffle()
    assert deck.cards[0] != first_card  # Исходная первая карта должна измениться
