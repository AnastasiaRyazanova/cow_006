from src.card import Card


class Row:
    MAX_CARDS = 6

    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> bool:
        if not self.cards or card.can_play(self.cards[-1]): #если ряд пустой или карта проходит проверку(ее номер больше)
            self.cards.append(card)
            return True #то можно добавить в ряд
        return False

    def score(self) -> int:
        """Возвращает сумму рангов карт в ряду."""
        return sum(c.cow_rank() for c in self.cards)

    def save(self) -> str:
        """Сохраняет карты в формате строки для хранения."""
        return ' '.join(card.save() for card in self.cards)

    @staticmethod
    def load(data: str) -> 'Row':
        """Загружает ряд из строки."""
        row = Row()
        cards_str = data.strip('[]')
        if cards_str:
            card_entries = cards_str.split('] [')

            for card_entry in card_entries:
                card = Card.load(card_entry)
                row.add_card(card)

        return row

    def clear(self):
        """Очищает ряд."""
        self.cards.clear()

    def __repr__(self):
        return ' '.join(repr(card) for card in self.cards)
