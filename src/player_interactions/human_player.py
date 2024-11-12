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
                card_number = int(input("Введите номер карты: "))
                for card in hand:
                    if card.number == card_number:
                        # print(f"Игрок выбрал карту {card}")
                        return card
            except ValueError:
                print("Повторите ввод. Введите число, указывающее на номер карты ")

    @classmethod
    def choose_row(cls, table: Table, card: Card) -> int:
        """Здесь выбор ряда, который забирает игрок"""
        while True:
            try:
                row_number = int(input("Выберете ряд, который заберете (1-4): ")) - 1
                if 0 <= row_number < len(table.rows):
                    print(f"\tИгрок выбрал ряд {row_number+1}")
                    return row_number
                else:
                    print("Повторите ввод. Введите число, указывающее на номер ряда ")
            except ValueError:
                print("Повторите ввод. Введите число, указывающее на номер ряда ")
