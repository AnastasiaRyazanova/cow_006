
from src.card import Card
from src.hand import Hand
from src.table import Table
from src.player_interaction import PlayerInteraction


class Human(PlayerInteraction):
    @classmethod
    def choose_card(
            cls, hand: Hand, table: Table, hand_counts: list[int] | None = None
    ) -> Card:
        """Здесь выбор карты из руки"""
        while True:
            try:
                print("Ваши карты: ", hand)
                user_input = input("Введите номер карты (или 'q' для выхода): ")
                if user_input.lower() == 'q':
                    return None
                card_number = int(user_input)
                for card in hand:
                    if card.number == card_number:
                        return card
            except ValueError:
                print("Повторите ввод. Введите число, указывающее на номер карты ")

    @classmethod
    def choose_row(cls, table: Table, card: Card) -> int:
        """Здесь выбор ряда, который забирает игрок"""
        while True:
            try:
                row_input = input("Выберите ряд, который заберете (1-4) (или 'q' для выхода): ")
                if row_input.lower() == 'q':
                    return None
                row_number = int(row_input) - 1
                if 0 <= row_number < len(table.rows):
                    print(f"\tИгрок выбрал ряд {row_number + 1}")
                    return row_number
                else:
                    print("Повторите ввод. Введите число, указывающее на номер ряда ")
            except ValueError:
                print("Повторите ввод. Введите число, указывающее на номер ряда ")


