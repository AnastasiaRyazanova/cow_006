import typing
from src.card import Card


class Hand:
    def __init__(self, cards: list[Card] = None):
        if cards is None:
            cards = []
        self.cards: list[Card] = cards

    def __repr__(self):
        return self.save()

    def __eq__(self, other):
        if isinstance(other, str):
            other = Hand.load(other)
        return self.cards == other.cards

    def save(self) -> str:
        return ' '.join(card.save() for card in self.cards)

    @classmethod
    def load(cls, text: str) -> typing.Self:
        """Загружает руку из строки"""
        cards = [Card.load(s[1:-1]) for s in text.split() if s.startswith('[') and s.endswith(']')]
        return cls(cards=cards)

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

