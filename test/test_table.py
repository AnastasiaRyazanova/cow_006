from src.card import Card
from src.row import Row
from src.table import Table
import json


def test_table_init():
    table = Table()
    assert len(table.rows) == 4
    for row in table.rows:
        assert isinstance(row, Row)


def test_add_card():
    table = Table()

    # Добавление карт
    table.add_card(Card(10))  # добавляется в 1 ряд
    table.add_card(Card(25))  # во 2 ряд
    table.add_card(Card(41))  # в 3 ряд
    table.add_card(Card(73))  # в 4 ряд
    table.add_card(Card(55))  # в 3 ряд
    table.add_card(Card(76))  # в 4 ряд (после 73)
    table.add_card(Card(77))  # в 4 ряд (после 76)
    table.add_card(Card(83))  # в 4 ряд (после 77)
    table.add_card(Card(90))  # в 4 ряд (после 83)
    #print(table)

    assert repr(table[0]) == '[10<3>]'
    assert repr(table[1]) == '[25<2>]'
    assert repr(table[2]) == '[41<1>] [55<7>]'
    assert repr(table[3]) == '[73<1>] [76<1>] [77<5>] [83<1>] [90<3>]'

    table.add_card(Card(91))  # 4 ряд очистится. игрок его забрал
    assert repr(table[3]) == '[91<1>]'
    assert len(table[3].cards) == 1
    #print(table)


def test_save_load():
    """Сохранение и загрузку стола."""
    table = Table()
    table.add_card(Card(10))
    table.add_card(Card(25))

    saved_data = table.save()
    loaded_data = json.loads(saved_data)
    new_table = Table.load(loaded_data)

    assert new_table[0].cards[0] == Card(10)
    assert new_table[1].cards[0] == Card(25)
    assert len(new_table[0].cards) == 1
    assert len(new_table[1].cards) == 1


def test_repr():
    """Тестируем строковое представление стола."""
    table = Table()
    card1 = Card(10)
    card2 = Card(20)

    table.add_card(card1)
    table.add_card(card2)

    expected_repr = f"r1: [{card1.number}<{card1.rank}>]\nr2: [{card2.number}<{card2.rank}>]\nr3: \nr4: "
    assert repr(table) == expected_repr
