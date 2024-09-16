class Card:
    def __init__(self, color: str, number: int):
        self.color = color
        self.number = number
        # self.rank = self.calculate_rank()

    def __repr__(self):
        return f'{self.color}{self.number}'

    def save(self):
        return repr(self)

    # def calculate_rank(self) -> int:
    #     # Определяем ранг карты
    #     if self.number % 5 == 0 and self.number % 11 == 0:  # 55
    #         return 7  # фиолетовая карта
    #     elif self.number % 5 == 0:
    #         return 2  # голубые карты (кратные 5)
    #     elif self.number % 10 == 0:
    #         return 3  # желтые карты (кратные 10)
    #     elif self.number % 11 == 0:  # двойные карты: 11, 22, 33...
    #         return 5  # красные карты
    #     else:
    #         return 1  # зеленые карты (все остальные)

# Дополнительные методы для взаимодействия с правилами игры
    def can_place_in_row(self, last_card: 'Card'):
        """Проверка, можно ли положить текущую карту в ряд."""
        return self.number > last_card.number


# Пример использования класса
if __name__ == "__main__":
    card1 = Card('g', 3)
    card2 = Card('b', 5)
    card3 = Card('y', 10)
    card4 = Card('r', 11)
    card5 = Card('p', 55)

    print(card1, card1)  # g3 1
    print(card2, card2)  # b5 2
    print(card3, card3)  # y10 3
    print(card4, card4)  # r11 5
    print(card5, card5)  # p55 7

    # print(card1, card1.rank)  # g3 1
    # print(card2, card2.rank)  # b5 2
    # print(card3, card3.rank)  # y10 3
    # print(card4, card4.rank)  # r11 5
    # print(card5, card5.rank)  # p55 7

    # Проверка на возможность размещения
    print(card1.can_place_in_row(card2))
