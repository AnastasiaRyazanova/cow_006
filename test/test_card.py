from src.card import Card
import pytest


def test_init():
    c = Card('y', 3)
    assert c.color == 'y'
    assert c.number == 3


def test_save():
    c = Card('y', 3)
    assert repr(c) == 'y3'
    assert c.save() == 'y3'

    c = Card('g', 7)
    assert repr(c) == 'g7'
    assert c.save() == 'g7'

    c = Card('v', 55)
    assert repr(c) == 'y3'
    assert c.save() == 'y3'


def test_validation():
    with pytest.raises(ValueError):
        Card('yellow', 1)
    with pytest.raises(ValueError):
        Card('ф', 1)
    with pytest.raises(ValueError):
        Card('b', 10)
    with pytest.raises(ValueError):
        Card('b', 3)


# def test_play_on():
#     c1 = Card.load('y1')
#     c2 = Card.load('y5')
#     c3 = Card.load('g1')
#     c4 = Card.load('g6')
#
#     assert c1.can_play_on(c1)
#     assert c2.can_play_on(c1)
#     assert c1.can_play_on(c2)
#     assert c3.can_play_on(c1)
#     assert not c4.can_play_on(c1)


