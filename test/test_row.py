from src.card import Card
from src.row import Row


def test_add_card_to_empty_row():
    row = Row()
    card = Card(2)
    assert row.add_card(card) is True
    assert row.cards == [card]


def test_add_card_to_full_row():
    row = Row()
    for i in range(1, 7):
        row.add_card(Card(i))
    assert row.is_full() is True
    new_card = Card(8)
    assert row.add_card(new_card) is False


def test_add_card_with_valid_play():
    row = Row()
    row.add_card(Card(2))
    card = Card(3)
    assert row.add_card(card) is True
    assert row.cards == [Card(2), Card(3)]


def test_add_card_with_invalid_play():
    row = Row()
    row.add_card(Card(3))
    row.add_card(Card(8))
    card = Card(2)
    assert row.add_card(card) is False
    assert row.cards == [Card(3), Card(8)]


def test_total_rank():
    row = Row()
    row.add_card(Card(1))
    row.add_card(Card(2))
    row.add_card(Card(3))
    assert row.total_rank() == 3

    row = Row()
    row.add_card(Card(7))
    row.add_card(Card(55))
    row.add_card(Card(104))
    assert row.total_rank() == 9


def test_clear():
    row = Row()
    row.add_card(Card(1))
    row.clear()
    assert row.cards == []
