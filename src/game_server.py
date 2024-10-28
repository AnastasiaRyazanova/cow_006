import inspect
import json
import sys
import enum
from src.deck import Deck
from src.game_state import GameState
from src.table import Table
from src.player import Player
from src.hand import Hand
from src.player_interaction import PlayerInteraction
import src.player_interactions as all_player_types

# END_TURN = "End turn"

"""
1. не читается и не добавляется в ряды стола последняя карта из selected_cards (класс table)
2. почему то идет сравнение выбранной карты первого игрока с картами второго (в play_card класса game_state)
 --- Раскрытие выбранных карт ---
lex(0): [19<1>]
ast(0): [96<1>]
Добавили карту [19<1>]
lex не имеет карты [96<1>] в руке.
?????

3. пока сделано окончание игры, когда у игроков заканчиваются карты (победил у кого меньше очков)
"""


class GamePhase(enum.StrEnum):
    START_GAME = "Start game"
    DEAL_CARDS = "Deal cards"
    FILL_TABLE = "Place cards on the table"
    DISPLAY_TABLE = "Display table state"
    CHOOSE_CARD = "Choose card"
    PLACE_CARD = "Place card"
    NEXT_PLAYER = "Switch current player"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"


class GameServer:
    INITIAL_HAND_SIZE = 10

    def __init__(self, player_types, game_state):
        self.game_state: GameState = game_state
        self.player_types: dict = player_types  # {player: PlayerInteractions}

    @classmethod
    def get_players(cls):
        player_count = cls.request_player_count()

        player_types = {}
        for p in range(player_count):
            name, kind = cls.request_player()
            player = Player(name, Hand())
            player_types[player] = kind
        return player_types

    @classmethod
    def load_game(cls):
        filename = 'cow.json'
        with open(filename, 'r') as fin:
            data = json.load(fin)
            game_state = GameState.load(data)
            print(game_state.save())
            player_types = {}
            for player, player_data in zip(game_state.players, data['players']):
                kind = player_data['kind']
                kind = getattr(all_player_types, kind)
                player_types[player] = kind
            return GameServer(player_types=player_types, game_state=game_state)

    def save_to_dict(self):
        data = self.game_state.save()
        for player_index, player in enumerate(self.player_types.keys()):
            player_interaction = self.player_types[player]
            data['players'][player_index]['kind'] = self.player_types[player].__name__
        return data

    def save(self):
        filename = 'cow.json'
        data = self.save_to_dict()
        with open(filename, 'w') as fout:
            json.dump(data, fout, indent=4)

    @classmethod
    def new_game(cls, player_types: dict):
        deck = Deck(cards=None)
        game_state = GameState(list(player_types.keys()), deck, Table())
        return cls(player_types, game_state)

    def run(self):
        current_phase = self.start_game_phase()
        while current_phase != GamePhase.GAME_END:
            phases = {
                GamePhase.DEAL_CARDS: self.deal_cards_phase,  # карты раздаются игрокам
                GamePhase.FILL_TABLE: self.fill_table_phase,  # заполнение стола (в начале игры)
                GamePhase.DISPLAY_TABLE: self.display_table_state,  # отображение состояние стола
                GamePhase.CHOOSE_CARD: self.choose_card_phase,  # игроки выбирают карты, карты добавляются в selected_cards класса table
                GamePhase.PLACE_CARD: self.place_card_phase,  # карты из selected_cards кладут в ряды стола!!&?
                GamePhase.NEXT_PLAYER: self.next_player_phase,  # ?
                GamePhase.DECLARE_WINNER: self.declare_winner_phase, # пока у игроков не закончатся карты/пока не будет 66 очков
            }
            current_phase = phases[current_phase]()

    def start_game_phase(self) -> GamePhase:
        print("Master: Начинаем игру!")
        self.game_state.deck.shuffle()
        print("Master: Колода перемешана.")
        return GamePhase.DEAL_CARDS

    def deal_cards_phase(self) -> GamePhase:  # карты раздаются игрокам
        for _ in range(self.INITIAL_HAND_SIZE):
            for player in self.player_types.keys():
                card = self.game_state.deck.draw_card()
                if card:
                    player.hand.add_card(card)
        print("Master: Карты разданы игрокам.")
        return GamePhase.FILL_TABLE

    def fill_table_phase(self) -> GamePhase:  # заполнение стола (в начале игры)
        for _ in range(len(self.game_state.table.rows)):
            if self.game_state.deck.cards:
                card = self.game_state.deck.draw_card()
                self.game_state.table.add_card(card)
        print("Master: Карты добавлены на стол.")
        return GamePhase.DISPLAY_TABLE

    def display_table_state(self):  # отображение состояние стола
        print("\nСостояние стола:")
        print(self.game_state.table)
        print("\nMaster: Игроки выбирают карту")
        return GamePhase.CHOOSE_CARD

    def choose_card_phase(self) -> GamePhase:  # игроки выбирают карты
        current_player = self.game_state.current_player()
        print(f"Ход игрока: {current_player.name}({current_player.score})")  # убрать

        card = self.player_types[current_player].choose_card(current_player.hand, self.game_state.table)  # выбор
        self.inform_all("inform_card_chosen", current_player)
        if card:
            print(f"{current_player.name}({current_player.score}): выбирает карту {card}")  # убрать
            self.game_state.table.add_selected_cards(current_player, card)  # добавляется в selected_cards

        if len(self.game_state.table.selected_cards) == len(self.player_types):  # пока все игроки не выберут карты
            return GamePhase.PLACE_CARD  # переход к размещению карт на стол
        else:
            return GamePhase.NEXT_PLAYER

    def next_player_phase(self) -> GamePhase:
        if not self.game_state.current_player().hand.cards:
            return GamePhase.DECLARE_WINNER  # здесь переход не к поиску победителей a
        self.game_state.next_player()
        return GamePhase.CHOOSE_CARD

    def place_card_phase(self) -> GamePhase:
        print("\n--- Раскрытие выбранных карт ---")
        for player, card in self.game_state.table.selected_cards:
            print(f"{player.name}({player.score}): {card}")

        failed_additions = []

        for player, card in self.game_state.table.selected_cards:
            try:
                successful, points = self.game_state.play_card(card)
                self.inform_all("inform_card_played", card)
                if successful:
                    print(f'Добавили карту {card}')
                else:
                    failed_additions.append((player, card))
                    print(f'Не добавляется {card}')
            except ValueError as e:
                failed_additions.append((player, card))
                print(str(e))

        for player, card in failed_additions:
            print(f"{player.name} не смог добавить карту {card} на стол.")
            row = self.player_types[player].choose_row(self.game_state.table, card)
            self.inform_all("inform_row_chosen", player, row)
            try:
                selected_row_index = int(row)
                if 0 <= selected_row_index < len(self.game_state.table.rows):
                    row_to_take = self.game_state.table.rows[selected_row_index]
                    if row_to_take.cards:
                        points = row_to_take.score()
                        print(f"{player.name} забирает ряд {selected_row_index + 1} и получает {points} очков.")
                        player.score += points
                        row_to_take.clear()
                    row_to_take.add_card(card)
                    player.hand.remove_card(card)
                    self.inform_all("inform_card_played", card)
                else:
                    print("Некорректный номер ряда.")
            except ValueError:
                print("Пожалуйста, вводите только числа.")

        self.display_table_state()
        self.game_state.table.selected_cards.clear()
        return GamePhase.NEXT_PLAYER

    # successful, points = self.game_state.play_card(card)
    # self.inform_all("inform_card_played", card)
    # if not successful:
    #     failed_additions.append((player, card))
    #     print(f'Не добавляется {card}')
    # else:
    #     print(f'Добавили карту {card}')

    def inform_all(self, method: str, *args, **kwargs):
        for p in self.player_types.values():
            getattr(p, method)(*args, **kwargs)

    def declare_winner_phase(self) -> GamePhase:
        winner = self.game_state.find_winner()[1]
        print(f"{winner.name}({winner.score}) стал победителем")

        print(f"Остальные игроки: ")
        remaining_players = [player for player in self.player_types.keys() if player != winner]
        sorted_remaining_players = sorted(remaining_players, key=lambda player: player.score)
        for player in sorted_remaining_players:
            print(f"{player.name}({player.score})")

        return GamePhase.GAME_END

    @staticmethod
    def request_player_count() -> int:
        while True:
            try:
                player_count = int(input("Сколько игроков? "))
                if 2 <= player_count <= 10:
                    return player_count
            except ValueError:
                pass
            print("Пожалуйста, введите число от 2 до 10.")

    @staticmethod
    def request_player() -> (str, PlayerInteraction):
        player_types = {cls.__name__: cls for name, cls in inspect.getmembers(all_player_types)
                        if inspect.isclass(cls) and issubclass(cls, PlayerInteraction)}

        if not player_types:
            print("Не удалось определить типы игроков. Убедитесь, что классы PlayerInteraction правильно определены.")
            sys.exit(1)

        player_types_as_str = ', '.join(player_types.keys())

        while True:
            name = input("Введите имя игрока: ")
            if name.isalpha():
                break
            print("Имя должно быть одним словом, только буквенные символы.")

        while True:
            kind = input(f"Выберите тип игрока ({player_types_as_str}): ")
            if kind in player_types:
                kind = player_types[kind]
                break
            print(f"Разрешенные типы игроков: {player_types_as_str}.")

        return name, kind


def __main__():
    load_from_file = False  # True - загрузить игру
    if load_from_file:
        server = GameServer.load_game()
        server.save()
    else:
        server = GameServer.new_game(GameServer.get_players())
    server.run()


if __name__ == "__main__":
    __main__()





