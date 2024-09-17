import random
import typing


from src.card import Card


class Deck:
    def __init__(self):
        self.cards = Card.all_cards()
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """Снимает карту с верхушки колоды."""
        return self.cards.pop()

    def save(self) -> str:
        return ' '.join(card.save() for card in self.cards)

    @classmethod
    def load(cls, text: str) -> 'Deck':
        deck = cls()
        deck.cards = [Card.load(card_str) for card_str in text.split()]
        return deck
