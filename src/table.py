import json
from src.card import Card
from src.row import Row
from src.player import Player


class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]
        self.selected_cards: list[tuple[Card, Player]] = []

    def __getitem__(self, item):
        return self.rows[item]

    def add_selected_cards(self, card: Card, player: Player):
        self.selected_cards.append((card, player))  # создается ряд с выбранными картами
        self.selected_cards.sort(key=lambda x: x[0].number)  # сортирует карты по возрастанию

    def add_card(self, card: Card, player: Player | None = None) -> (bool, int):
        """Добавляет карту в оптимальный ряд."""
        # для заполнения стола в начале игры в game_server, player = None
        for row in self.rows:     # если в ряд пустой, то автоматически добавляется карта
            if not row.cards:
                row.add_card(card)
                return True, 0  # возвращается 0 штрафных очков

        good_rows = [row for row in self.rows if card.can_play(row.cards[-1])]    # ряды, в которые можно добавить карту

        if not good_rows:
            return False, 0

        # Если есть подходящие ряды, добавляем в оптимальный
        attached_row = min(good_rows, key=lambda r: abs(card.number - r.cards[-1].number))

        points = 0
        if len(attached_row.cards) == Row.MAX_CARDS - 1:
            points = attached_row.score()
            print(f"\tКарта игрока 6-я в ряду {self.rows.index(attached_row) + 1}")
            print(f"\tИгрок забрал ряд {self.rows.index(attached_row) + 1} и получил {points} очков")
            if player:
                player.update_score_from_row(attached_row)
            attached_row.clear()
        attached_row.add_card(card)
        return True, points

    def save(self) -> str:
        """Сохраняет состояние стола в виде JSON строки."""
        return json.dumps(
            {f"row{i + 1}": self.rows[i].save() for i in range(len(self.rows))}
        )

    @classmethod
    def load(cls, data: dict) -> 'Table':
        """Загружает состояние стола из предоставленных данных."""
        table = cls()
        for row_key, cards_str in data.items():
            row = Row.load(cards_str)
            row_index = int(row_key.replace("row", "")) - 1
            table.rows[row_index] = row
        return table

    def __repr__(self):
        repr_rows = [f"r{i + 1}: {repr(row)}" for i, row in enumerate(self.rows)]
        return "\n".join(repr_rows)
