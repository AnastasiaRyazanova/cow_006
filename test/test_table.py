import pytest
from src.card import Card
from src.table import Table


@pytest.fixture
def table():
    return Table()


def test_init(table):
    # Тест 1: Проверяем начальное состояние таблицы
    assert len(table.rows) == 4, "Ошибка: должно быть 4 ряда."
    for row in table.rows:
        assert len(row.cards) == 0, "Ошибка: все ряды должны быть пустыми в начале."


def test_add_card(table):
    # Тест 2: Добавление карты и проверка, что она попадает в ряд
    card1 = Card(5)
    row_index1 = table.add_card(card1)
    assert row_index1 >= 0, "Ошибка: карта не была добавлена в ряд."
    assert card1 in table.rows[row_index1].cards, "Ошибка: карта не была найдена в ряду."

    card2 = Card(3)  # меньше чем 5
    row_index2 = table.add_card(card2)
    assert row_index2 >= 0, "Ошибка: должен быть вызван метод choose_row_for_picking."

#def test_choose_row_for_picking():


def test_min_card(table):
    table.add_card(Card(10))
    table.add_card(Card(25))
    table.add_card(Card(5))
    min_card_number = table.min_card()
    assert min_card_number == 5


def test_save_load(table):
    saved_data = table.save()
    new_table = Table.load(saved_data)
    assert new_table.rows == table.rows, "Ошибка: состояние после загрузки не совпадает с сохраненным."



