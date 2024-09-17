import pytest

from src.card import Card


def test_init():
    c = Card(22)
    assert c.number == 22


def test_save():
    c = Card(22)
    assert repr(c) == '[22<5>]'
    assert c.save() == '[22<5>]'

    c = Card(7)
    assert repr(c) == '[7<1>]'
    assert c.save() == '[7<1>]'


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

