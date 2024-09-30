'''
класс deck + тесты
'''

import random
from src.card import Card


class Deck:
    def __init__(self, cards: None | list[Card]):
        if cards is None:
            cards = Card.all_cards()
            random.shuffle(cards)
        self.cards: list[Card] = cards

    def __repr__(self) -> str:
        return self.save()

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            other = Deck.load(other)
        return self.cards == other.cards

    def save(self) -> str:
        """Сохраняет колоду в простом текстовом формате."""
        return ' '.join(card.save() for card in self.cards)

    @classmethod
    def load(cls, text: str) -> 'Deck':
        cards = []
        for s in text.split():
            if s.startswith('[') and s.endswith(']'):
                try:
                    cards.append(Card.load(s[1:-1]))
                except Exception as e:
                    print(f"Error loading card from {s}: {e}")
        return cls(cards=cards)

    def draw_card(self):
        """Берет карту из колоды и возвращает ее."""
        return self.cards.pop() if self.cards else None

    def full_deck(self):
        """Возвращает всю колоду."""
        return self.cards

    def shuffle(self):
        """Перемешивает колоду."""
        random.shuffle(self.cards)
