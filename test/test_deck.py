import random
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

    d = Deck([Card(9), Card(77), Card(1)])
    assert d.save() == '[9<1>] [77<5>] [1<1>]'

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

    d2 = Deck.load('[3<1>] [10<3>] [7<1>]')
    d3 = Deck.load('[3<1>] [10<3>]')
    c = d2.draw_card()
    assert c == Card.load('[7<1>]')
    assert d2 == d3

    d2 = Deck([Card(10), Card(7), Card(55)])
    d3 = Deck([Card(10), Card(7)])
    c = d2.draw_card()
    assert c == Card(55)
    assert d2 == d3


def test_shuffle_1():
    deck = Deck(cards=cards.copy())
    deck_list = [deck.save()]
    for _ in range(5):
        deck.shuffle()
        s = deck.save()
        assert s not in deck_list
        deck_list.append(s)


def test_shuffle_2():
    random.seed(3)

    cards = Card.all_cards()
    deck = Deck(cards=cards)
    original_deck = deck.save()

    deck.shuffle()
    assert deck.save() != original_deck

    deck.shuffle()
    assert deck.save() != original_deck

    deck.shuffle()
    assert deck.save() != original_deck


def test_full_deck():
    deck = Deck(None)
    assert len(deck.full_deck()) == len(Card.all_cards())
    assert set(deck.full_deck()) == set(Card.all_cards())

    original_deck = deck.full_deck()
    deck.shuffle()
    assert len(deck.full_deck()) == len(original_deck)
    assert set(deck.full_deck()) == set(original_deck)
