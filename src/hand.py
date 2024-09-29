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
        cards = [Card.load(s[1:-1]) for s in text.split() if s.startswith('[') and s.endswith(']')]
        return cls(cards=cards)

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def score(self) -> int:
        return sum(c.cow_rank() for c in self.cards)


def main():
    card1 = Card(45)
    card2 = Card(2)
    card3 = Card(55)

    # Создаем руку игрока и добавляем карты в руку
    hand = Hand()
    hand.add_card(card1)
    hand.add_card(card2)
    hand.add_card(card3)

    # Выводим руку игрока
    print("Карты в руке игрока:", hand)


if __name__ == "__main__":
    main()
