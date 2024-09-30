import json
from typing import List
from src.card import Card
from src.row import Row


class Table:
    def __init__(self):
        self.rows: List[Row] = [Row() for _ in range(4)]

    def add_card_to_row(self, card: Card, row_index: int) -> bool:
        """Добавляет карту в указанный ряд по индексу."""
        if 0 <= row_index < len(self.rows):
            return self.rows[row_index].add_card(card)
        else:
            raise IndexError("Индекс ряда вне диапазона.")

    def add_card(self, card: Card) -> bool:
        """Добавляется карта в первый ряд, в который можно её положить."""
        for row in self.rows:
            if not row.is_full():
                if row.add_card(card):
                    return True
        return False

    # def add_card(self, card: Card) -> bool:
    #     """Добавляет карту в первый ряд, в который можно её положить."""
    #     for row in self.rows:
    #         if row.add_card(card):
    #             return True
    #     return False

    def get_row(self, index: int) -> Row:
        return self.rows[index]

    # def get_row(self, row_index: int) -> Row:
    #     """Возвращает ряд по индексу."""
    #     if 0 <= row_index < len(self.rows):
    #         return self.rows[row_index]
    #     else:
    #         raise IndexError("Индекс ряда вне диапазона.")

    def save(self) -> str:
        return json.dumps([[card.to_dict() for card in row.cards] for row in self.rows])

    @classmethod
    def load(cls, json_data: str):
        data = json.loads(json_data)
        table = cls()
        for i, row_data in enumerate(data):
            for card_data in row_data:
                card = Card.from_dict(card_data)
                table.rows[i].add_card(card)
        return table

    def __repr__(self):
        repr_rows = [f"r{i + 1}: {repr(row)}" for i, row in enumerate(self.rows)]
        return "\n".join(repr_rows)


def main():
    table = Table()
    card1 = Card(10)
    card2 = Card(25)
    card3 = Card(41)
    card4 = Card(73)
    card5 = Card(55)

    # Добавление карты в конкретные ряды
    table.add_card_to_row(card1, 0)  # добавляем в 1 ряд
    table.add_card_to_row(card2, 1)  # во 2 ряд
    table.add_card_to_row(card3, 0)  # в 1 ряд
    table.add_card_to_row(card4, 3)  # в 4 ряд
    table.add_card_to_row(card5, 2)  # в 3 ряд

    print("Состояние стола:")
    print(table)

    # Печать конкретного ряда
    print("Содержимое 1-го ряда:")
    print(table.get_row(0))

    print("Содержимое 2-го ряда:")
    print(table.get_row(1))

    #print("Содержимое ?-го ряда:")
    #print(table.get_row(6))


if __name__ == "__main__":
    main()
