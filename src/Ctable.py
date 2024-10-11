import json
from src.Ccard import Card
from src.Crow import Row


class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]

    def add_card(self, card: Card) -> bool:
        """Добавляет карту в оптимальный ряд."""
        best_row_index = None
        best_difference = float('inf')

        for i, row in enumerate(self.rows):
            if len(row.cards) < Row.MAX_CARDS:
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
            if len(row.cards) == Row.MAX_CARDS - 1:
                points = row.score()
                row.clear()
                row.add_card(card)
                print(f"\n Игрок забрал ряд {best_row_index + 1}. Получено очков: {points}")
                return True
            else:
                return row.add_card(card)
        else:
            chosen_row = self.choose_row()
            points = chosen_row.score()
            chosen_row.clear()
            print(f"\nИгрок забрал ряд {self.rows.index(chosen_row) + 1}. Получено очков: {points}")
            chosen_row.add_card(card)

    def choose_row(self):
        while True:
            try:
                chosen_row_index = int(input("Выберите ряд (1-4): ")) - 1
                if 0 <= chosen_row_index < len(self.rows):
                    return self.rows[chosen_row_index]
                else:
                    print("Неверный номер ряда. Попробуйте снова.")
            except ValueError:
                print("Пожалуйста, введите число.")

    def get_row(self, index: int) -> Row:
        return self.rows[index]

    def save(self) -> str:
        return json.dumps([[[card.number, card.rank] for card in row.cards] for row in self.rows])

    @classmethod
    def load(cls, rows_data: str):
        table = cls()
        loaded_rows = json.loads(rows_data)
        for i, row_data in enumerate(loaded_rows):
            for card_data in row_data:
                card = Card(card_data[0])
                table.rows[i].add_card(card)
        return table

    def __repr__(self):
        repr_rows = [f"r{i + 1}: {repr(row)}" for i, row in enumerate(self.rows)]
        return "\n".join(repr_rows)


#проверка функции выбора пользователем ряда
if __name__ == "__main__":
    table = Table()
    test_cards = [
            [Card(1), Card(8), Card(9)],
            [Card(2), Card(7), Card(10)],
            [Card(3), Card(6), Card(11)],
            [Card(4), Card(5), Card(12), Card(13), Card(14)]
        ]

    for i in range(4):
        for card in test_cards[i]:
            table.rows[i].add_card(card)
    print(table)

    chosen_card = Card(15)
    table.add_card(chosen_card)
    print(f"<Игрок> выбрал карту {chosen_card}")
    print("\nТекущиее состояние стола:")
    print(table)


#1  Добавление 5-й карты в ряд
    # test_cards = [
    #     [Card(1), Card(8), Card(9)],
    #     [Card(2), Card(7), Card(10)],
    #     [Card(3), Card(6), Card(11)],
    #     [Card(4), Card(5), Card(12), Card(13), Card(14)]
    # ]
    #     table.add_card(Card(15))
#2  Добавление карты меньшей всех карт
    #     [Card(1), Card(82)],
    #     [Card(2), Card(7), Card(104)],
    #     [Card(3), Card(61)],
    #     [Card(49)]
    # ]
    #     table.add_card(Card(40))

