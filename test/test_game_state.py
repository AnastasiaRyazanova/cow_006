from src.card import Card
from src.deck import Deck
from src.game_state import GameState
from src.player import Player
from src.table import Table

data = {
    'deck': ' '.join(Card(number=i).save() for i in range(1, 105)),
    'row1': '[39<1>]',
    'row2': '[89<1>]',
    'row3': '[80<3>]',
    'row4': '[77<1>]',
    'current_player_index': 0,
    'players': [
        {
            'name': 'Ast',
            'hand': '[82<1>]  [102<1>]  [35<2>]  [65<2>]  [33<1>]  [66<5>]  [44<5>]  [98<1>]  [97<1>]  [25<2>]',
            'score': 0,
            'is_human': True
        },
        {
            'name': 'P1',
            'hand': '[12<1>]  [71<1>]  [5<1>]  [81<1>]  [49<1>]  [21<1>]  [3<1>]  [85<2>]  [22<5>]  [26<1>]',
            'score': 0,
            'is_human': False
        }
    ]
}


ast = Player.load(data['players'][0])
p1 = Player.load(data['players'][1])

rows_data = [data['row1'], data['row2'], data['row3'], data['row4']]
table = Table.load(rows_data)

deck = Deck(None)


def test_init():
    game = GameState(players=[ast, p1], deck=deck, table=table, current_player_index=0)
    assert game.players == [ast, p1]
    assert game.deck == deck
    assert game.table == table
    assert game.current_player_index == 0


def test_current_player():
    game = GameState(players=[ast, p1], deck=deck, table=table, current_player_index=0)
    assert game.current_player() == ast

    game.current_player_index = 1
    assert game.current_player() == p1


def test_eq():
    game1 = GameState(players=[ast, p1], deck=deck, table=table, current_player_index=0)
    game2 = GameState(players=[ast, p1], deck=deck, table=table, current_player_index=0)
    game3 = GameState(players=[ast], deck=deck, table=table, current_player_index=0)

    assert game1 == game2
    assert game1 != game3


def test_save():
    game = GameState(players=[ast, p1], deck=deck, table=table, current_player_index=0)
    saved_data = game.save()

    assert saved_data['current_player_index'] == 0
    assert len(saved_data['players']) == 2
    assert saved_data['deck'] == deck.save()
    assert saved_data['table'] == table.save()


def test_load():
    game = GameState.load(data)
    assert game.current_player() == ast


def test_next_player():
    game = GameState(players=[ast, p1], deck=deck, table=table, current_player_index=0)

    game.next_player()
    assert game.current_player() == p1

    game.next_player()
    assert game.current_player() == ast


def test_play_card():
    game = GameState(players=[ast, p1], deck=deck, table=table, current_player_index=0)

    initial_hand_size = len(game.current_player().hand.cards)

    card_to_play = Card.load('[82<1>]')
    game.play_card(card_to_play)

    initial_hand_size -= 1

    assert len(game.current_player().hand.cards) == initial_hand_size
    assert table.rows[3].cards[-1] == card_to_play  # Проверка, что карта добавлена к ряду 3

    card_to_play = Card(44)
    game.play_card(card_to_play)

    initial_hand_size -= 1

    assert len(game.current_player().hand.cards) == initial_hand_size
    assert table.rows[0].cards[-1] == card_to_play  # Проверка, что карта добавлена к ряду 1


def test_is_game_over():
    game = GameState(players=[ast, p1], deck=deck, table=table, current_player_index=0)
    assert not game.is_game_over()

    ast.score = 66
    assert game.is_game_over()
