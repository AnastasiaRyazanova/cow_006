import pytest
import json
from src.card import Card
from src.deck import Deck
from src.game_state import GameState
from src.player import Player
from src.table import Table

data = {
    "table": {
        "row1": "[39<1>] [45<2>]",
        "row2": "[89<1>]",
        "row3": "[80<3>] [99<5>] [101<1>]",
        "row4": "[77<5>]",
    },
    "deck": "",
    "current_player_index": 0,
    "players": [
        {
            "name": "Ast",
            "hand": "[82<1>] [102<1>] [35<2>] [65<2>] [33<5>] [97<1>] [25<2>]",
            # "is_human": True,
            "score": 0
        },
        {
            "name": "P1",
            "hand": "[12<1>] [71<1>] [5<2>] [81<1>] [3<1>] [22<5>] [26<1>]",
            # "is_human": False,
            "score": 0
        }
    ]
}

ast = Player.load(data["players"][0])
p1 = Player.load(data["players"][1])
full_deck = Deck(None)
json_data = json.dumps(data)
table = Table.load(json.loads(json_data)["table"])


@pytest.fixture()
def game():
    return GameState(players=[ast, p1], deck=full_deck, table=table, current_player=0)


def test_init(game):
    assert game.players == [ast, p1]
    assert game.deck == full_deck
    assert game.current_player().name == "Ast"


def test_current_player(game):
    game._current_player = 0
    assert game.current_player().name == "Ast"
    assert game._current_player == 0

    game._current_player = 1
    assert game.current_player().name == "P1"
    assert game._current_player == 1


def test_eq(game):
    game2 = GameState(players=[ast, p1], deck=full_deck, table=table, current_player=0)
    game3 = GameState(players=[ast, p1], deck=Deck([]), table=table, current_player=1)
    assert game == game2
    assert game != game3


def test_save(game):
    expected = {
        "table": data["table"],
        "deck": str(full_deck),
        "current_player_index": 0,
        "players": [player.save() for player in game.players],
    }
    assert game.save() == expected


def test_load():
    loaded_game = GameState.load(data)
    assert loaded_game.save() == data


def test_next_player(game):
    assert game.current_player().name == "Ast"
    game.next_player()
    assert game.current_player().name == "P1"
    game.next_player()
    assert game.current_player().name == "Ast"


def test_play_card_two_players(game):
    """Тест для случая, когда играют два игрока."""
    player1 = game.players[0]
    player2 = game.players[1]

    assert player1.hand.cards
    assert player2.hand.cards

    # Игрок 1 выбирает первую карту
    card_to_play = player1.hand.cards[0]  # [82<1>]
    game.table.add_selected_cards(player1, card_to_play)  # Добавляем карту игрока 1 в selected_cards

    game.next_player()
    assert game.current_player() == player2

    # Игрок 2 выбирает четвертую карту   # [81<1>]
    card_to_play_player2 = player2.hand.cards[3]
    game.table.add_selected_cards(player2, card_to_play_player2)  # Добавляем карту игрока 2 в selected_cards

    card_numbers_in_selected = [card.number for _, card in game.table.selected_cards]
    assert set(card_numbers_in_selected) == {81, 82}
    print(table.selected_cards)

    # Переходим к добавлению карт на стол
    # successful_card1, points1 = game.table.add_card(card_to_play)  # Добавляем карту игрока 1
    # successful_card2, points2 = game.table.add_card(card_to_play_player2)  # Добавляем карту игрока 2
    for player, card in table.selected_cards:
        successful, points = game.play_card(card)

    # Проверяем, что обе карты были успешно добавлены на стол
    # assert successful_card1 is True
    # assert successful_card2 is False
    assert repr(table[3]) == '[77<5>] [81<1>] [82<1>]'
    print(table)
    #
    # Проверяем, что карты убраны из рук игроков
    assert card_to_play not in player1.hand.cards  # Карта игрока 1 убрана из руки
    assert card_to_play_player2 not in player2.hand.cards  # Карта игрока 2 убрана из руки

    # Проверяем состояние стола
    assert game.table.save()  # Проверить, что стол не пустой



# def test_play_card_1(game):
#     """Если карта игрока подошла"""
#     current_player = game.current_player()
#     selected_card = current_player.hand.cards[0]  # ast выбирает первую карту из руки
#     assert current_player.hand.cards  # проверка, что у ast есть карты в руке
#
#     game.table.add_selected_cards(current_player, selected_card)
#     initial_table_state = game.table.save()  # сохр. текущее состояние стола
#     print(game.current_player().hand.cards)
#     print(table)
#
#     successful, points = game.play_card(selected_card)
#     assert successful is True  # карта проигралась
#     assert selected_card not in current_player.hand.cards  # проверяет, что карта больше не находится в руке
#
#     new_table_state = game.table.save()  # проверка состояния стола после игры карты
#     assert new_table_state != initial_table_state
#     assert repr(game.table[3]) == '[77<5>] [82<1>]'
#     print(table)
#     print(game.current_player().hand.cards)


# def test_play_card_2(game):
#     """Если карта игрока не подошла"""
#     current_player = game.current_player()
#     selected_card = current_player.hand.cards[2]  # ast играет картой [35<2>]
#     assert current_player.hand.cards
#
#     game.table.add_selected_cards(current_player, selected_card)
#     initial_table_state = game.table.save()
#     # print(table)
#
#     successful, points = game.play_card(selected_card)
#     assert successful is False  # карта не проигралась
#     assert selected_card in game.current_player().hand.cards
#
#     new_table_state = game.table.save()
#     assert new_table_state == initial_table_state  # состояние стола пока не изменилось
#     # print(table)


def test_play_invalid_card(game):
    with pytest.raises(ValueError, match="Неверный номер карты."):  # raise ValueError в классе Card
        invalid_card = Card(999)
        game.play_card(invalid_card)


def test_is_game_over(game):
    assert not game.is_game_over()

    ast.score = 128
    assert game.is_game_over()


def test_find_winner(game):

    ast.score = 65
    p1.score = 102
    is_winner, winner = game.find_winner()
    assert game.is_game_over()
    assert is_winner is True
    assert winner.name == 'Ast'

    ast.score = 71
    p1.score = 71
    is_winner, winners = game.find_winner()
    assert game.is_game_over()
    assert is_winner is False
    assert len(winners) == 2
    winner_names = {winner.name for winner in winners}
    assert winner_names == {"Ast", "P1"}
