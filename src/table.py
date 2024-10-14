import json
from src.card import Card
from src.row import Row


class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]

    def __getitem__(self, item):
        return self.rows[item]

    def add_card(self, card: Card) -> (bool, int):
        """Добавляет карту в оптимальный ряд."""
        for row in self.rows:
            if not row.cards:
                row.add_card(card)
                return True, 0

        good_rows = []

        for row in self.rows:
            if card.can_play(row.cards[-1]):
                good_rows.append(row)

        if not good_rows:
            return False, 0

        attached_row = min(good_rows, key=lambda r: abs(card.number - r.cards[-1].number))

        points = 0
        if len(attached_row.cards) == Row.MAX_CARDS - 1:
            points = attached_row.score()
            print(f"\nИгрок забрал ряд {self.rows.index(attached_row) + 1}. Получено очков: {points}")
            attached_row.clear()

        attached_row.add_card(card)
        return True, points

    def save(self) -> str:
        return json.dumps([[[card.number, card.rank] for card in row.cards] for row in self.rows])

    @classmethod
    def load(cls, rows_data: list):
        table = cls()
        for row_index, cards in enumerate(rows_data):
            for card_data in cards:
                card = Card.load(f'[{card_data[0]}<{card_data[1]}>]')
                table[row_index].add_card(card)
        return table

    def __repr__(self):
        repr_rows = [f"r{i + 1}: {repr(row)}" for i, row in enumerate(self.rows)]
        return "\n".join(repr_rows)
