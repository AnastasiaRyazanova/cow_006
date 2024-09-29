from src.hand import Hand
from src.card import Card
from src.player import Player


def test_init():
    h = Hand(cards=[Card(1), Card(25), Card(10)])
    p = Player(name='Ast', hand=h, score=0)
    assert p.name == 'Ast'
    assert p.hand == h
    assert p.score == 0


def test_str():
    h = Hand(cards=[Card(1), Card(25), Card(10)])
    p = Player(name='Ast', hand=h, score=6)
    assert str(p) == 'Ast(6): [1<1>] [25<2>] [10<3>]'


def test_save():
    h = Hand(cards=[Card(1), Card(25), Card(10)])
    p = Player(name='Ast', hand=h, score=6)
    assert p.save() == {'name': 'Ast', 'score': 6, 'hand': h.save()}


def test_eq():
    h1 = Hand(cards=[Card(1), Card(25), Card(10)])
    h2 = Hand(cards=[Card(1), Card(25), Card(10)])
    p1 = Player(name='Ast', hand=h1, score=6)
    p2 = Player(name='Ast', hand=h2, score=6)
    assert p1 == p2


def test_load():
    data = {'name': 'Ast', 'score': 3, 'hand': '[1<1>] [13<1>] [5<2>]'}
    h = Hand.load('[1<1>] [13<1>] [5<2>]')
    p_expected = Player(name='Ast', hand=h, score=3)
    p = Player.load(data)
    assert p == p_expected


def test_is_loser():
    h = Hand(cards=[Card(55)])
    p = Player(name='Ast', hand=h, score=63)
    assert not p.is_loser()
    h = Hand(cards=[Card(55)])
    p = Player(name='Ast', hand=h, score=69)
    assert p.is_loser()

