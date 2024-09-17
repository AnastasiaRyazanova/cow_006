import pytest

from src.cards import Card


def test_init():
    c = Card(22)
    assert c.number == 22


def test_save():
    c = Card(22)
    assert c.save() == '[22<5>]'

    c = Card(7)
    assert c.save() == '[7<1>]'

    with pytest.raises(ValueError):
        Card(200)


def test_eq():
    card1 = Card(10)
    card2 = Card(10)
    card3 = Card(20)

    assert card1 == card2
    assert card1 != card3


def test_can_play():
    c1 = Card(43)
    c2 = Card(7)
    c3 = Card(66)
    c4 = Card(6)
    c5 = Card(55)

    assert c1.can_play(c2)
    assert not c2.can_play(c1)
    assert c3.can_play(c2)
    assert not c2.can_play(c3)
    assert c3.can_play(c4)
    assert not c4.can_play(c3)
    assert not c5.can_play(c3)


def test_load():
    s = '[17<1>]'
    c = Card.load(s)
    assert c == Card(17)

    s = '[55<7>]'
    c = Card.load(s)
    assert c == Card(55)


def test_card_color():
    for card_number, expected_color in [(1, Card.RANK_COLORS[1]),
                                        (10, Card.RANK_COLORS[3]),
                                        (15, Card.RANK_COLORS[2]),
                                        (22, Card.RANK_COLORS[5]),
                                        (55, Card.RANK_COLORS[7])]:
        card = Card(card_number)
        assert card.color() == expected_color


def test_all_cards():
    all_cards = Card.all_cards()
    assert len(all_cards) == 104
    assert all_cards[0].number == 1
    assert all_cards[-1].number == 104



