from src.card import Card
from src.player import Player
from src.table import Table


class GameState:
    """
    data = {
    "table": {
        "row1": "[39<1>] [45<2>]",
        "row2": "[89<1>]",
        "row3": "[80<3>] [99<5>] [101<1>]",
        "row4": "[77<5>]",
    },
    "current_player_index": 0,
    "players": [
        {
            "name": "Ast",
            "hand": "[82<1>] [102<1>] [35<2>] [65<2>] [33<5>] [66<5>] [44<5>] [98<1>] [97<1>] [25<2>]",
            "score": 0
        },
        {
            "name": "P1",
            "hand": "[12<1>] [71<1>] [5<2>] [81<1>] [49<1>] [21<1>] [3<1>] [85<2>] [22<5>] [26<1>]",
            "score": 0
        }
    ]
}
    """

    def __init__(
        self, players: list[Player], table: Table, current_player: int = 0
    ):
        self.players: list[Player] = players
        self.table: Table = table
        self.__current_player: int = current_player

    @property
    def current_player_index(self):
        return self.__current_player

    def current_player(self) -> Player:
        return self.players[self.__current_player]

    def __eq__(self, other):
        if not isinstance(other, GameState):
            return False
        if self.__current_player != other.__current_player:
            return False
        if self.players != other.players:
            return False
        if self.table != other.table:
            return False
        return True

    def save(self) -> dict:
        return {
            "table": {f"row{i + 1}": self.table[i].save() for i in range(len(self.table.rows))},
            "current_player_index": self.__current_player,
            "players": [p.save() for p in self.players],
        }

    @classmethod
    def load(cls, data: dict):
        players = [Player.load(p) for p in data["players"]]
        table = Table.load(data["table"])
        current_player = int(data["current_player_index"])

        return cls(
            players=players,
            table=table,
            current_player=current_player,
        )

    def next_player(self):
        """Ход переходит к следующему игроку."""
        self.__current_player = (self.__current_player + 1) % len(self.players)

    def play_card(self, card: Card, player: Player) -> (bool, int):
        """Текущий игрок играет карту."""
        if card.number not in Card.NUMBERS:
            return False, 0

        if card not in player.hand.cards:
            raise ValueError(f"{player.name} не имеет карты {card} в руке.")

        player.hand.remove_card(card)

        successful, points = self.table.add_card(card)
        return successful, points

    def is_game_over(self) -> bool:
        """Проверяет, закончилась ли игра."""
        return any(player.is_loser() for player in self.players)

    def find_winner(self) -> (bool, Player or list[Player]):
        """Находит победителя."""
        min_score = min(player.score for player in self.players)
        winners = [player for player in self.players if player.score == min_score]  #список игроков с минимальным количеством очков

        if len(winners) == 1:  #если победитель 1
            return True, winners
        else:
            return False, winners

