import json
from src.card import Card
from src.row import Row


class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]

    def add_card(self, card: Card) -> bool:
        """Добавляет карту в оптимальный ряд."""
        best_row_index = None
        best_difference = float('inf')

        for i, row in enumerate(self.rows):
            if not row.is_full():
                if row.cards:
                    last_card = row.cards[-1]
                    difference = card.number - last_card.number
                    if 0 < difference < best_difference:
                        best_difference = difference
                        best_row_index = i
                else:
                    best_row_index = i
                    break

        if best_row_index is not None:
            row = self.rows[best_row_index]
            if len(row.cards) == 5:
                points = row.total_rank()
                row.clear()
                row.add_card(card)
                print(f"\n Игрок забрал ряд {best_row_index + 1}. Получено очков: {points}")
            else:
                return row.add_card(card)
        return False  # Если нет доступного ряда, игрок выберет ряд, который заберет.
                        # Прописывать в table?

    def get_row(self, index: int) -> Row:
        return self.rows[index]

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
