from src.card import Card
from src.hand import Hand
from src.table import Table
from src.player_interaction import PlayerInteraction
import random


class Bot(PlayerInteraction):
    @classmethod
    def choose_card(
            cls, hand: Hand, table: Table, hand_counts: list[int] | None = None
    ) -> Card:
        """Принимает решение, какую карту с руки играть"""
        chosen_card = random.choice(hand.cards)
        print(f"Бот выбрал карту {chosen_card}")
        return chosen_card

    @classmethod
    def choose_row(cls, table: Table, card: Card) -> int:
        """Здесь выбор ряда, который забирает Бот"""
        chosen_row = random.randint(0, len(table.rows) - 1)
        print(f"Бот забирает ряд {chosen_row+1}")
        return chosen_row



