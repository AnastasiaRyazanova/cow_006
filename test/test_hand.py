from src.card import Card
from src.hand import Hand

cards = [Card(3), Card(10), Card(77)]


def test_init():
    d = Hand(cards=cards)
    assert d.cards == cards


def test_save():
    d = Hand(cards=cards)
    assert d.save() == '[3<1>] [10<3>] [77<5>]'

    d = Hand(cards=[])
    assert d.save() == ''


def test_load():
    d = Hand.load('[3<1>] [10<3>] [77<5>]')
    expected_deck = Hand(cards)
    assert d == expected_deck


def test_add_card():
    h = Hand.load('[3<1>] [10<3>] [77<5>]')
    h.add_card(Card.load('[60<3>]'))
    assert repr(h) == '[3<1>] [10<3>] [77<5>] [60<3>]'

    h.add_card(Card.load('[8<1>]'))
    assert repr(h) == '[3<1>] [10<3>] [77<5>] [60<3>] [8<1>]'

    h.add_card(Card(34))
    assert repr(h) == '[3<1>] [10<3>] [77<5>] [60<3>] [8<1>] [34<1>]'


def test_remove_card():
    h = Hand.load('[3<1>] [10<3>] [77<5>] [60<3>] [8<1>]')
    c = Card.load('[77<5>]')
    h.remove_card(c)
    assert repr(h) == '[3<1>] [10<3>] [60<3>] [8<1>]'
