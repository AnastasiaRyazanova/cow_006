from src.table import Table
from src.card import Card
from src.deck import Deck
from src.player import Player


class GameState:
    def __init__(self, players: list[Player], deck: Deck, table: Table, current_player_index: int = 0):
        self.players = players
        self.deck = deck
        self.table = table
        self.current_player_index = current_player_index

    def current_player(self) -> Player:
        return self.players[self.current_player_index]

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def __eq__(self, other):
        if not isinstance(other, GameState):
            return False
        if self.current_player_index != other.current_player_index:
            return False
        if self.players != other.players:
            return False
        if self.deck != other.deck:
            return False
        if self.table != other.table:
            return False
        return True

    def save(self) -> dict:
        return {
            'deck': self.deck.save(),
            'current_player_index': self.current_player_index,
            'players': [player.save() for player in self.players],
            'table': self.table.save()
        }

    @classmethod
    def load(cls, data: dict):
        players = [Player.load(p_data) for p_data in data['players']]
        deck = Deck.load(data['deck'])
        table = Table.load([data['row1'], data['row2'], data['row3'], data['row4']])
        return cls(players=players, deck=deck, table=table, current_player_index=data['current_player_index'])

    def play_card(self, card: Card):
        self.current_player().hand.remove_card(card)

        if not self.table.add_card(card):
            print(f"{self.current_player().name}: выбрана карта {card}")
            chosen_row = self.table.choose_row()
            points = chosen_row.score()
            chosen_row.clear()
            chosen_row.add_card(card)
            self.current_player().score += points
            print(f"\n{self.current_player().name} забирает ряд. Получает штрафные баллы: {points}")
        else:
            print(f"\n{self.current_player().name}: выбрана карта {card}")
            row = self.table
            row.add_card(card)

    def is_game_over(self) -> bool:
        return any(player.is_loser() for player in self.players)



