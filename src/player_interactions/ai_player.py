from src.card import Card
from src.row import Row
from src.hand import Hand
from src.table import Table
from src.player import Player
from src.player_interaction import PlayerInteraction
import random


class Bot(PlayerInteraction):
    @classmethod
    def choose_card(
            cls, hand: Hand, table: Table, hand_counts: list[int] | None = None
    ) -> Card:
        """Принимает решение, какую карту с руки играть"""
        # print("Карты бота", hand)
        chosen_card = random.choice(hand.cards)
        # print(f"Бот выбрал карту {chosen_card}")

        # """# для теста 2 ботов"""
        # chosen_card = hand.cards[0]
        return chosen_card

    @classmethod
    def choose_row(cls, table: Table, card: Card) -> int:
        """Здесь выбор ряда, который забирает Бот"""
        # """для теста выбирает 2 ряд"""
        # chosen_row = 1
        chosen_row = random.randint(0, len(table.rows) - 1)
        print(f"\tБот выбрал ряд {chosen_row+1}")
        return chosen_row

    @classmethod
    def inform_card_chosen(cls, player: Player):
        """
        Сообщает, что игрок выбрал карту.
        """
        pass

    @classmethod
    def inform_row_chosen(cls, player: Player, row: int):
        """
        Сообщает, что игрок выбрал ряд.
        """
        pass


