"""Карты Корова006."""
from typing import Self


class Card:
    #RANK = [1, 2, 3, 5, 7]
    #COLORS = ['g', 'b', 'y', 'r', 'p']
    NUMBERS = list(range(1, 105))

    def __init__(self, number: int):
        if number not in Card.NUMBERS:
            raise ValueError
        #if rank not in Card.RANK:
            #raise ValueError

        self.number = number
        self.rank = self.cow_rank()

    def cow_rank(self) -> int:
        if self.number == 55:
            return 7
        elif self.number % 11 == 0 and self.number != 55:
            return 5
        elif self.number % 10 == 0:
            return 3
        elif self.number % 5 == 0 and self.number % 10 != 0:
            return 2
        else:
            return 1

    def __repr__(self):
        return f'[{self.number}<{self.rank}>]'
            #return f'[{self.color}{self.number}<{self.rank}>]'

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        """From 'y3' to Card('y', 3)."""
        return Card(number=int(text[0]))

    def can_play(self, last_card: Self) -> bool:
        """Можно ли играть карту self на карту last."""
        return self.number > last_card.number

    @staticmethod
    def all_cards(colors: list[str] | None = None, numbers: None | list[int] = None):
        if numbers is None:
            numbers = Card.NUMBERS
        # cards = []
        # for col in colors:
        #     for num in numbers:
        #         cards.append(Card(color=col, number=num))
        cards = [Card(number=num) for num in numbers]
        return cards

        #def score(self):
            #"""Штрафные очки за карту."""
            #return self.rank
