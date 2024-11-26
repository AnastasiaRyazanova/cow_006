import pygame

from src.card import Card
from src.hand import Hand
from src.deck import Deck
from src.row import Row
from src.table import Table
from src.ui.view_card import ViewCard, Fly
from src.ui.view_hand import ViewHand
from src.ui.view_players import ViewPlayers
from src.ui.view_row_of_sel_cards import ViewSelCards
from src.ui.view_row import ViewRow
from src.ui.view_table import ViewTable
from src.game_server import GameServer
from src.resource import RESOURCE as RSC
from src.ui.event import post_event, EVENT_PLAY_CARD


class ViewGame:
    DISPLAY_COLOR = 'azure3'
    YGAP = 0
    XGAP = 30

    def __init__(self, game_server: GameServer):
        # Существующие инициализации
        self.game = game_server
        self.fly = Fly()
        rplayer1, rscards, rtable, rplayers = self.calculate_geom_contants()
        game = game_server.game_state

        self.v_hand = ViewHand(game.players[0].hand, rplayer1)

        self.v_s_cards = ViewSelCards(game.table.selected_cards, rscards)

        self.v_table = ViewTable(game.table, rtable)

        self.v_players = ViewPlayers(game.players, rplayers)

        self.bot_thinking: int = 0
        self.begin_bot_thinking()

    def calculate_geom_contants(self):
        screen_width, screen_height = pygame.display.get_window_size()
        card_width = ViewCard.WIDTH
        card_height = ViewCard.HEIGHT
        self.YGAP = (screen_height - 5 * card_height) // 4
        rplayer = pygame.Rect(self.XGAP, self.YGAP, screen_width - 2*self.XGAP, self.YGAP + card_height)
        rscards = pygame.Rect(self.XGAP + card_width*8, self.YGAP + card_height * 2, rplayer.width, card_height)
        rtable = pygame.Rect(self.XGAP, self.YGAP + 1.5*card_height, screen_width - 2*self.XGAP, self.YGAP)
        rplayers = pygame.Rect(screen_width - 150, self.YGAP, 150, screen_height)
        return rplayer, rscards, rtable, rplayers

    def model_update(self):
        # self.fly.fly()
        if self.fly.animation_mode:
            self.fly.fly()
            return
        elif self.stupid_pause():
            return
        self.game.run_one_turn()

    def begin_bot_thinking(self):
        self.bot_thinking = RSC['FPS']

    def stupid_pause(self):
        self.bot_thinking -= 1
        if self.bot_thinking > 0:
            return True
        return False

    def redraw(self, display: pygame.Surface):
        display.fill(self.DISPLAY_COLOR)
        if self.game.game_state.current_player_index == 0:
            self.v_players.redraw(display)
            self.v_hand.redraw(display)
        self.v_s_cards.redraw(display)
        self.v_table.redraw(display)
        self.fly.redraw(display)

        pygame.display.update()

    def event_processing(self, event: pygame.event.Event):
        if self.fly.animation_mode:
            return
        if event.type == EVENT_PLAY_CARD:
            data = event.user_data
            print(f'EVENT_PLAY_CARD user_data={data}')
            card = data['card']
            player_index = data['player_index']
            self.on_play_card(card=card, player_index=player_index)
        self.v_hand.event_processing(event)
        self.v_s_cards.event_processing(event)
        self.v_table.event_processing(event)
        self.v_players.event_processing(event)

    def on_play_card(self, card: Card, player_index: int):
        if player_index == 0:
            vhand = self.v_hand
        else:
            vhand = None  # ????????? :(

        vc = None

        for ivc, vc in enumerate(vhand.vcards if vhand else []):
            if vc and vc.card == card:
                vhand.vcards[ivc] = None
                break

        finish_position = (0, 0)
        for vcard, _ in self.v_s_cards.vscards:
            if vcard.card == card:
                finish_position = (vcard.x, vcard.y)
                break

        self.fly.begin(vcard=vc, finish=finish_position)

        if len(self.game.game_state.table.selected_cards) == len(self.game.game_state.players):
            self.move_selected_cards_to_table()

    def move_selected_cards_to_table(self):
        updated_vscards = []
        for vcard, player in self.v_s_cards.vscards:
            if vcard.selected:
                card = vcard.card
                target_row = None
                for vr in self.v_table.vtable:
                    if vr.row.can_add_card(card):
                        target_row = vr
                        break

                if target_row:
                    target_position = (0, 0)
                    for vcard, _ in self.v_s_cards.vscards:
                        if vcard.card == card:
                            target_position = (vcard.x, vcard.y)
                            break
                    self.fly.begin(vcard=vcard, finish=target_position)
                    self.game.game_state.table.add_card(card, player)
            else:
                updated_vscards.append((vcard, player))

        self.v_s_cards.vscards = updated_vscards






