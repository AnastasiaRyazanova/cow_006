import json
import typing
from src.hand import Hand
from src.row import Row


class Player:
    score_limit = 66

    def __init__(self, name: str, hand: Hand, score: int = 0):
        self.name = name
        self.hand = hand
        self.score = score

    def __str__(self):
        return f'{self.name}({self.score}): {self.hand}'

    def __eq__(self, other: typing.Self | str | dict):
        if isinstance(other, str):
            other = self.load(json.loads(other))
        if isinstance(other, dict):
            other = self.load(other)
        return self.name == other.name \
            and self.score == other.score \
            and self.hand == other.hand

    def save(self) -> dict:
        return {
            'name': self.name,
            'hand': self.hand.save(),
            'score': self.score
        }

    @classmethod
    def load(cls, data: dict):
        return cls(name=data['name'], hand=Hand.load(data['hand']), score=int(data['score']))

    def update_score_from_row(self, row: Row):
        """Обновляет счет игрока."""
        self.score += row.score()

    def is_loser(self) -> bool:
        """Проверяет, проиграл ли игрок."""
        return self.score >= self.score_limit
    
