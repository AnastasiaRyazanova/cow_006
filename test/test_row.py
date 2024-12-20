from src.card import Card
from src.row import Row


def test_add_card_to_row():
    row = Row()
    assert row.add_card(Card(2)) is True
    assert row.cards == [Card(2)]

    row = Row()
    row.add_card(Card(2))
    assert row.add_card(Card(3)) is True
    assert row.cards == [Card(2), Card(3)]

    row = Row()
    row.add_card(Card(3))
    row.add_card(Card(8))
    assert row.add_card(Card(2)) is False
    assert row.cards == [Card(3), Card(8)]


def test_save_row():
    row = Row()
    assert row.save() == ""

    row = Row()
    row.add_card(Card(1))
    assert row.save() == "[1<1>]"

    row = Row()
    row.add_card(Card(1))
    row.add_card(Card(11))
    row.add_card(Card(55))
    assert row.save() == "[1<1>] [11<5>] [55<7>]"


def test_load_row():
    row = Row.load("[]")
    assert row.cards == []

    row = Row.load("[1<1>]")
    assert row.cards == [Card(1)]

    row = Row.load("[1<1>] [11<1>] [55<7>]")
    assert row.cards == [Card(1), Card(11), Card(55)]


def test_total_rank():
    row = Row()
    row.add_card(Card(1))
    row.add_card(Card(2))
    row.add_card(Card(3))
    assert row.score() == 3

    row = Row()
    row.add_card(Card(7))
    row.add_card(Card(55))
    row.add_card(Card(104))
    assert row.score() == 9


def test_clear():
    row = Row()
    row.add_card(Card(1))
    row.clear()
    assert row.cards == []
