"""Карты Корова006."""
from typing import Self


class Card:
    RANK_COLORS = {
        1: '\033[92m',   # Зеленый
        2: '\033[96m',   # Голубой
        3: '\033[93m',   # Желтый
        5: '\033[91m',   # Красный
        7: '\033[95m',   # Фиолетовый
    }
    RESET = '\033[0m'  # Сброс цвета
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

    def color(self) -> str:
        return self.RANK_COLORS.get(self.rank, self.RESET)

    def __repr__(self) -> str:
        return f'{self.color()}[{self.number}<{self.rank}>]{self.RESET}'

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        number_str = text.split('<')[0].strip('[]')
        return Card(number=int(number_str))

    @staticmethod
    def load_multiple(text: str) -> list['Card']:
        """Загружает несколько карт из строки."""
        cards = []
        for s in text.strip('[]').split('] ['):
            if s:  # Проверяем на пустую строку
                cards.append(Card.load(f'[{s}]'))
        return cards

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

