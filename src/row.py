from src.card import Card


class Row:
    MAX_CARDS = 6

    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> bool:
        if not self.cards:
            self.cards.append(card)
            return True
        else:
            last_card = self.cards[-1]
            if card.can_play(last_card):
                self.cards.append(card)
                return True

        return False

    def score(self) -> int:
        """Возвращает сумму рангов карт в ряду."""
        return sum(c.cow_rank() for c in self.cards)

    def clear(self):
        """Очищает ряд."""
        self.cards.clear()

    def __repr__(self):
        return ' '.join(repr(card) for card in self.cards)
