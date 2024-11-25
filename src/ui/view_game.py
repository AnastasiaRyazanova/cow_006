import pygame

from src.card import Card
from src.hand import Hand
from src.deck import Deck
from src.row import Row
from src.table import Table
from src.ui.view_card import ViewCard, Fly
from src.ui.view_hand import ViewHand
from src.ui.view_row_of_sel_cards import ViewSelCards
from src.ui.view_row import ViewRow
from src.ui.view_table import ViewTable
from src.game_server import GameServer


class ViewGame:
    DISPLAY_COLOR = 'azure3'
    YGAP = 0
    XGAP = 30

    def __init__(self, game_server: GameServer):
        # Существующие инициализации
        self.game = game_server
        self.fly = Fly()
        rplayer1, rscards, rtable = self.calculate_geom_contants()
        game = game_server.game_state

        self.v_hand = ViewHand(game.players[0].hand, rplayer1)

        self.v_s_cards = ViewSelCards(game.table.selected_cards, rscards)

        self.v_table = ViewTable(game.table, rtable)

    def calculate_geom_contants(self):
        screen_width, screen_height = pygame.display.get_window_size()
        card_width = ViewCard.WIDTH
        card_height = ViewCard.HEIGHT
        self.YGAP = (screen_height - 5 * card_height) // 4
        rplayer = pygame.Rect(self.XGAP, self.YGAP, screen_width - 2*self.XGAP, self.YGAP + card_height)
        rscards = pygame.Rect(self.XGAP + card_width*8, self.YGAP + card_height * 2, rplayer.width, card_height)
        rtable = pygame.Rect(self.XGAP, self.YGAP + 1.5*card_height, screen_width - 2*self.XGAP, self.YGAP)
        return rplayer, rscards, rtable

    def model_update(self):
        self.fly.fly()

    def redraw(self, display: pygame.Surface):
        display.fill(self.DISPLAY_COLOR)
        self.v_hand.redraw(display)
        self.v_s_cards.redraw(display)
        self.v_table.redraw(display)
        self.fly.redraw(display)
        pygame.display.update()

    def event_processing(self, event: pygame.event.Event):
        if self.fly.animation_mode:
            return
        self.v_hand.event_processing(event)
        self.v_s_cards.event_processing(event)
        self.v_table.event_processing(event)


