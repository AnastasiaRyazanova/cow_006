from abc import ABC, abstractmethod
from src.card import Card
from src.row import Row
from src.hand import Hand
from src.table import Table
from src.player import Player


class PlayerInteraction(ABC):
    @classmethod
    @abstractmethod
    def choose_card(
            cls, hand: Hand, table: Table, hand_counts: list[int] | None = None
    ) -> Card:
        pass

    @classmethod
    @abstractmethod
    def choose_row(cls, table: Table, card: Card) -> int:
        pass

    @classmethod
    def inform_card_chosen(cls, player: Player):
        """
        Сообщает, что игрок выбрал карту.
        """
        pass

    @classmethod
    def inform_card_played(cls, card: Card):
        """
        Сообщает, что карта проигралась.
        """
        pass

    @classmethod
    def inform_row_chosen(cls, player: Player, row: int):
        """
        Сообщает, что игрок выбрал ряд.
        """
        pass
