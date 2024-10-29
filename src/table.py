import json
from src.card import Card
from src.row import Row
from src.player import Player


class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]
        self.selected_cards: list[tuple[Player, Card]] = []

    def __getitem__(self, item):
        return self.rows[item]

    def add_selected_cards(self, player: Player, card: Card):
        self.selected_cards.append((player, card))  # создается ряд с выбранными картами
        self.selected_cards.sort(key=lambda x: x[1].number)  # сортирует карты по возрастанию

    def add_card(self, card: Card) -> (bool, int):
        """Добавляет карту в оптимальный ряд."""
        # для заполнения стола в начале игры в game_server
        for row in self.rows:     # если в ряд пустой, то автоматически добавляется карта
            if not row.cards:
                row.add_card(card)
                return True, 0  # возвращается 0 штрафных очков

        if not self.selected_cards:
            return False, 0

        for player, selected_card in self.selected_cards:
            good_rows = []

            for row in self.rows:
                if selected_card.can_play(row.cards[-1]):
                    good_rows.append(row)

            # Если есть подходящие ряды, добавляем в оптимальный
            if good_rows:
                attached_row = min(good_rows, key=lambda r: abs(selected_card.number - r.cards[-1].number))
                points = 0
                if len(attached_row.cards) == Row.MAX_CARDS - 1:
                    points = attached_row.score()
                #    print(f"\nИгрок забрал ряд {self.rows.index(attached_row) + 1}. Получено очков: {points}")
                    attached_row.clear()  # Очищаем ряд

                attached_row.add_card(selected_card)
                self.selected_cards.remove((player, selected_card))  # Удаляем карту из выбранных
                return True, points

        return False, 0


        # player, card = self.selected_cards.pop(0)
        #
        # good_rows = []    # ряды, в которые можно добавить карту
        #
        # for row in self.rows:
        #     if card.can_play(row.cards[-1]):
        #         good_rows.append(row)   # добавляется в список подходящих рядов
        #
        # if not good_rows:     # если нет подходящих рядов(номер карты меньше карт во всех рядах)
        #     return False, 0      # возвращается 0 штрафных очков
        #
        # attached_row = min(good_rows, key=lambda r: abs(card.number - r.cards[-1].number))     # оптимальный ряд
        #                                                                                       # (разница номеров минимальная)
        # points = 0  # число очков, к-е затем добавятся в score игрока, забравшего ряд
        # if len(attached_row.cards) == Row.MAX_CARDS - 1:  # если карта игрока становится 6-й в ряду
        #     points = attached_row.score()
        #     print(f"\nИгрок забрал ряд {self.rows.index(attached_row) + 1}. Получено очков: {points}")
        #     attached_row.clear()
        #
        # attached_row.add_card(card)  # 6-я карта становится 1-й в ряду
        # return True, points

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
