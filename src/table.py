import random
import typing
from src.card import Card
from src.row import Row


class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]

    def add_card(self, card: Card) -> int:
        # Сначала проверяем, можем ли добавить карту в один из рядов
        for row in self.rows:
            if row.can_play(card):
                return row.add_card(card)

        # Если карта меньше всех последних карт в рядах
        return self.choose_row_for_picking(card)

    def choose_row_for_picking(self, card: Card) -> int:
        """Запрос выбора ряда для игрока, если карта меньше всех последних."""
        print("Выберите ряд для забирания карт (0-3):")
        for idx, row in enumerate(self.rows):
            last_card = row.last_card()
            print(f"Ряд {idx}: {last_card if last_card else 'пустой'}")

        row_choice = int(input())
        if 0 <= row_choice < len(self.rows):
            points = sum(card.rank for card in self.rows[row_choice].cards)
            self.rows[row_choice].cards.clear()  # Убираем все карты из выбранного ряда
            return points
        else:
            print("Неверный выбор. Ничего не взято.")
            return 0

    def min_card(self) -> typing.Optional[int]:
        """Возвращает минимальное значение из последних карт в рядах."""
        return min((row.last_card().number for row in self.rows if row.last_card()), default=None)

    def save(self) -> dict:
        return {f'row_{i}': row.save() for i, row in enumerate(self.rows)}

    @classmethod
    def load(cls, data: dict) -> 'Table':
        table = cls()
        for i in range(4):
            table.rows[i] = Row.load(data[f'row_{i}'])
        return table


