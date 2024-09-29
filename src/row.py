from typing import List
from src.card import Card


class Row:
    MAX_CARDS = 6

    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> bool:
        """Добавляет карту в ряд, если это возможно."""
        if len(self.cards) >= Row.MAX_CARDS:
            return False

        if not self.cards:
            self.cards.append(card)
            return True

        last_card = self.cards[-1]
        if card.can_play(last_card):
            self.cards.append(card)
            return True

        return False

    def is_full(self) -> bool:
        """Проверяет, достигнут ли максимум карт в ряду."""
        return len(self.cards) >= Row.MAX_CARDS

    def total_rank(self) -> int:
        """Возвращает сумму рангов карт в ряду."""
        return sum(card.rank for card in self.cards)

    def clear(self):
        """Очищает ряд."""
        self.cards.clear()

    def __repr__(self):
        return f"Row({self.cards})"
