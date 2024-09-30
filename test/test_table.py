import pytest
from src.card import Card
from src.row import Row
from src.table import Table


def test_table_init():
    table = Table()
    assert len(table.rows) == 4
    for row in table.rows:
        assert isinstance(row, Row)


def test_add_card_to_row():
    table = Table()

    assert table.add_card_to_row(Card(10), 0) is True  # добавление карты в 1-й ряд
    assert len(table.get_row(0).cards) == 1
    assert str(table.get_row(0)) == "[10<3>]"
    assert table.add_card_to_row(Card(21), 1) is True  # во 2-й ряд
    assert len(table.get_row(1).cards) == 1
    assert table.add_card_to_row(Card(5), 0) is False  # добавление карты  меньшим номером
    assert len(table.get_row(1).cards) == 1
    assert table.add_card_to_row(Card(56), 1) is True
    assert len(table.get_row(1).cards) == 2


def test_add_card_invalid_index():
    table = Table()
    with pytest.raises(IndexError):
        table.add_card_to_row(Card(10), 10)  # индекс вне диапазона


def test_add_card():
    table = Table()

    assert table.add_card(Card(10)) is True  # добавление первой карты
    assert len(table.get_row(0).cards) == 1
    assert table.add_card(Card(25)) is True
    assert len(table.get_row(0).cards) == 2
    assert table.add_card(Card(5)) is False  # не удается добавить
    assert len(table.get_row(0).cards) == 2


def test_save_load():
    """Тестируем сохранение и загрузку стола."""
    table = Table()
    table.add_card_to_row(Card(10), 0)

    saved_data = table.save()
    new_table = Table.load(saved_data)

    assert new_table.get_row(0).cards[0] == Card(10)


def test_repr():
    """Тестируем строковое представление стола."""
    table = Table()
    card1 = Card(10)
    card2 = Card(20)

    table.add_card_to_row(card1, 0)
    table.add_card_to_row(card2, 1)

    expected_repr = f"r1: [{card1.number}<{card1.rank}>]\nr2: [{card2.number}<{card2.rank}>]\nr3: \nr4: "
    assert repr(table) == expected_repr

