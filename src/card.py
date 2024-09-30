"""Карты Корова006."""
from typing import Self


class Card:
    NUMBERS = list(range(1, 105))

    def __init__(self, number: int):
        if number not in Card.NUMBERS:
            raise ValueError("Неверный номер карты.")

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

    def to_dict(self):
        return {'number': self.number, 'rank': self.rank}

    def __repr__(self):
        return f'[{self.number}<{self.rank}>]'

    def save(self):
        return repr(self)

    @classmethod
    def from_dict(cls, data):
        return cls(data['number'])

    @staticmethod
    def load(text: str):
        number_str = text.split('<')[0].strip('[]')
        return Card(number=int(number_str))

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.number == other.number
        return False

    def can_play(self, last_card: Self) -> bool:
        """Можно ли играть карту self на карту last."""
        return self.number > last_card.number

    def __hash__(self):
        return hash(self.number)

    @staticmethod
    def all_cards() -> list['Card']:
        """Создаёт и возвращает все карты от 1 до 104."""
        return [Card(number=num) for num in Card.NUMBERS]


def create_deck() -> list:
    """Создаёт и возвращает колоду из всех карт."""
    return Card.all_cards()





def show_cards():
    deck = create_deck()

    # Вывод карт в строчку
    print('Карты в строчку:', deck)

    # Вывод карт в столбики
    def display_cards(cards, columns=10):
        for i in range(0, len(cards), columns):
            print(' '.join(repr(card) for card in cards[i:i + columns]))

    print('Карты в столбик')
    display_cards(deck, columns=13)


def main():
    input('Нажмите Enter, чтобы посмотреть список карт') or show_cards()


if __name__ == "__main__":
    main()




