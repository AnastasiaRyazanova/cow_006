from src.card import Card
from src.row import Row
from src.table import Table


def test_table_init():
    table = Table()
    assert len(table.rows) == 4
    for row in table.rows:
        assert isinstance(row, Row)


def add_card_to_row(table: Table, card: Card):
    for _ in table.rows:
        if table.add_card(card):
            return True
    return False


def test_add_card():
    table = Table()

    # Добавление карт
    add_card_to_row(table, Card(10))  # добавляется в 1 ряд
    add_card_to_row(table, Card(25))  # во 2 ряд
    add_card_to_row(table, Card(41))  # в 3 ряд
    add_card_to_row(table, Card(73))  # в 4 ряд
    add_card_to_row(table, Card(55))  # в 3 ряд
    add_card_to_row(table, Card(76))  # в 4 ряд (после 73)
    add_card_to_row(table, Card(77))  # в 4 ряд (после 76)
    add_card_to_row(table, Card(83))  # в 4 ряд (после 77)
    add_card_to_row(table, Card(90))  # в 4 ряд (после 83)

    assert len(table.get_row(0).cards) == 1
    assert len(table.get_row(1).cards) == 1
    assert len(table.get_row(2).cards) == 2
    assert len(table.get_row(3).cards) == 5

    add_card_to_row(table, Card(91))  # 4 ряд очистится. игрок его забрал
    assert len(table.get_row(3).cards) == 1


def test_save_load():
    """Сохранение и загрузку стола."""
    table = Table()
    table.add_card(Card(10))
    table.add_card(Card(25))

    saved_data = table.save()
    new_table = Table.load(saved_data)

    assert new_table.get_row(0).cards[0] == Card(10)
    assert new_table.get_row(1).cards[0] == Card(25)
    assert len(new_table.rows[0].cards) == 1
    assert len(new_table.rows[1].cards) == 1


def test_repr():
    """Тестируем строковое представление стола."""
    table = Table()
    card1 = Card(10)
    card2 = Card(20)

    table.add_card(card1)
    table.add_card(card2)

    expected_repr = f"r1: [{card1.number}<{card1.rank}>]\nr2: [{card2.number}<{card2.rank}>]\nr3: \nr4: "
    assert repr(table) == expected_repr
