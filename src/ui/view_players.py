import pygame
from pygame import font
from src.player import Player


class ViewPlayers:
    FONT_SIZE = 24
    FONT = 'arial'

    def __init__(self, players: list[Player], bound: pygame.Rect):
        self.vplayers: list[tuple[Player, pygame.Surface]] = self.create_view_players(players, bound)

    def redraw(self, display: pygame.Surface):
        for player, text_surface in self.vplayers:
            display.blit(text_surface, (player.x, player.y))

    def event_processing(self, event: pygame.event.Event):
        for player, _ in self.vplayers:
            pass

    def create_view_players(self, players: list[Player], bound: pygame.Rect):
        print('\nplayers')
        if players is None:
            return []

        bx = bound.x
        by = bound.y

        view_players = []
        basic_font = font.SysFont(self.FONT, self.FONT_SIZE)

        for player in players:
            player_text = f"{player.name}: {player.score}"
            text_surface = basic_font.render(player_text, True, (0, 0, 0))
            player.x = bx
            player.y = by
            view_players.append((player, text_surface))
            by += self.FONT_SIZE

            print(f'Add selected player {player.name}')
        return view_players

