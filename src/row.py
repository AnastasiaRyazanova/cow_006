import random
import typing
from src.card import Card


class Row:
    MAX_LENGTH = 6

    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> int:
        """Добавляет карту в ряд. Если это шестая карта, возвращает очки за первые пять."""
        self.cards.append(card)
        points = 0

        if len(self.cards) > self.MAX_LENGTH:
            points += self.truncate(card)

        return points

    def has_max_length(self) -> bool:
        """Проверка, достигнут ли максимальный размер ряда."""
        return len(self.cards) >= self.MAX_LENGTH

    def truncate(self, new_card: Card) -> int:
        """Удаляет первые карты и возвращает количество очков."""
        points = sum(card.rank for card in self.cards[:self.MAX_LENGTH - 1])
        self.cards = [new_card]  # Оставляем только новую карту
        return points

    def can_play(self, card: Card) -> bool:
        """Можно ли положить карту в ряд."""
        if self.cards:
            return card.number > self.cards[-1].number
        return True

    def last_card(self) -> typing.Optional[Card]:
        """Возвращает последнюю карту в ряду или None, если ряд пуст."""
        return self.cards[-1] if self.cards else None

    def save(self) -> str:
        return ' '.join(card.save() for card in self.cards)

    @classmethod
    def load(cls, text: str) -> 'Row':
        row = cls()
        for card_str in text.split():
            row.cards.append(Card.load(card_str))
        return row

    def __eq__(self, other):
        if isinstance(other, Row):
            return self.cards == other.cards
        return False

