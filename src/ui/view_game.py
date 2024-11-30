import pygame
import random

from src.card import Card
from src.ui.view_card import ViewCard, Fly
from src.ui.view_hand import ViewHand
from src.ui.view_players import ViewPlayers
from src.ui.view_row_of_sel_cards import ViewSelCards
from src.ui.view_row import ViewRow
from src.ui.view_table import ViewTable
from src.game_server import GameServer, GamePhase
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

        selected_cards_with_players = [(card, player) for card, player in game.table.selected_cards]
        self.v_s_cards = ViewSelCards(selected_cards_with_players, rscards)  # ряд карт выбранных игроками

        self.v_table = ViewTable(game.table, rtable)

        self.v_players = ViewPlayers(game.players, rplayers)

        self.bot_thinking: int = 0
        self.begin_bot_thinking()

        self.delay = RSC['delay']  # задержка между ходами

    def show_winners(self):  # вывод победителей
        one_winner, winners = self.game.game_state.find_winner()
        return [winner.name for winner in winners]

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
        if self.fly.animation_mode:
            self.fly.fly()
            return
        elif self.stupid_pause():
            return
        self.game.run_one_turn()
        pygame.time.delay(self.delay)

    def begin_bot_thinking(self):
        self.bot_thinking = RSC['FPS']

    def stupid_pause(self):
        self.bot_thinking -= 1
        if self.bot_thinking > 0:
            return True
        return False

    def redraw(self, display: pygame.Surface):
        display.fill(self.DISPLAY_COLOR)
        self.v_players.redraw(display)
        self.v_hand.redraw(display)
        self.v_s_cards.redraw(display)
        self.v_table.redraw(display)
        self.fly.redraw(display)
        self.display_winners(display)
        pygame.display.update()

    def display_winners(self, display: pygame.Surface):  # создается табличка с именами победителей
        winners = self.show_winners()
        if winners:
            if self.game.current_phase == GamePhase.GAME_END:
                font = pygame.font.SysFont("Arial", 36)
                winners_text = "Победители: " + ", ".join(winners)
                text_surface = font.render(winners_text, True, 'tomato')
                display.blit(text_surface, (self.XGAP + 8 * ViewCard.WIDTH, self.YGAP + 3 * ViewCard.HEIGHT))

                text_rect = text_surface.get_rect(center=(self.XGAP + 8 * ViewCard.WIDTH + text_surface.get_width() // 2,
                                              self.YGAP + 3 * ViewCard.HEIGHT + text_surface.get_height() // 2))
                rect_width = text_surface.get_width() + 20
                rect_height = text_surface.get_height() + 20
                back_rect = pygame.Rect(text_rect.x - 10, text_rect.y - 10, rect_width, rect_height)
                pygame.draw.rect(display, 'white', back_rect)
                display.blit(text_surface, text_rect.topleft)

    def event_processing(self, event: pygame.event.Event):
        if self.fly.animation_mode:
            return

        if event.type == EVENT_PLAY_CARD:
            data = event.user_data
            print(f'EVENT_PLAY_CARD user_data={data}')
            card = data['card']
            player_index = data['player_index']
            self.on_play_card(card=card)
            selected_cards_with_players = [(card, player) for card, player in self.game.game_state.table.selected_cards]
            self.v_s_cards = ViewSelCards(selected_cards_with_players, self.v_s_cards.bound)
            self.v_players = ViewPlayers(self.game.game_state.players, self.v_players.bound)
            self.v_table = ViewTable(self.game.game_state.table, self.v_table.bound)
        self.v_hand.event_processing(event)
        self.v_table.event_processing(event)

    def on_play_card(self, card: Card):
        vhand = self.v_hand
        for ivc, vc in enumerate(vhand.vcards if vhand else []):
            if vc and vc.card == card:
                vhand.vcards[ivc] = None
                break

    def end_card_playing(self, **kwargs):
        player_index = kwargs['player']
        player = self.game.game_state.players[player_index]
        if player_index == 0:
            self.vhand = ViewHand(player.hand, self.v_hand.bound)
            self.redraw(pygame.display.get_surface())

            selected_cards_with_players = [(card, player) for card, player in self.game.game_state.table.selected_cards]
            self.v_s_cards = ViewSelCards(selected_cards_with_players, self.v_s_cards.bound)




