from abc import ABC, abstractmethod
from src.card import Card
from src.hand import Hand
from src.table import Table


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
