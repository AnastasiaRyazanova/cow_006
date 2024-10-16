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
        return ' '.join(card.save() for card in self.cards)

    @classmethod
    def load(cls, text: str) -> 'Deck':
        """Загружает колоду из строки"""
        cards = []
        for s in text.split():
            if s.startswith('[') and s.endswith(']'):
                cards.append(Card.load(s[1:-1]))
        return cls(cards=cards)

    def draw_card(self):
        """Берет карту из колоды и возвращает ее, убирая из колоды"""
        return self.cards.pop() if self.cards else None

    def full_deck(self):
        """Возвращает всю колоду"""
        return self.cards

    def shuffle(self):
        """Перемешивает колоду"""
        random.shuffle(self.cards)


# full_deck = Deck(Card.all_cards())
# print(full_deck)
