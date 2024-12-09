import pygame
from pygame import font
from src.player import Player


class ViewPlayers:
    FONT_SIZE = 28
    FONT = 'verdana'
    MAX_NAME_WIDTH = 130

    def __init__(self, players: list[Player], bound: pygame.Rect):
        self.bound = bound
        self.vplayers: list[tuple[Player, pygame.Surface]] = self.create_view_players(players, bound)

    def redraw(self, display: pygame.Surface):
        screen_width, screen_height = pygame.display.get_window_size()
        rect_x = screen_width - 183
        rect_y = 0
        rect_width = 183
        rect_height = screen_height
        pygame.draw.rect(display, 'gray', (rect_x, rect_y, rect_width, rect_height))

        font = pygame.font.SysFont("Arial", 38)
        text = font.render("Игроки", True, 'black')
        text_rect = text.get_rect(center=(rect_x + rect_width // 2, rect_y + 40))
        display.blit(text, text_rect)

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
            text_surface = basic_font.render(player_text, True, 'black')
            if text_surface.get_width() > self.MAX_NAME_WIDTH:
                t_name = self.trim_name(player.name, basic_font)
                player_text = f"{t_name}: {player.score}"
                text_surface = basic_font.render(player_text, True, 'black')

            player.x = bx
            player.y = by
            view_players.append((player, text_surface))
            by += self.FONT_SIZE

            print(f'Add selected player {player.name}')
        return view_players

    def trim_name(self, name: str, font: pygame.font.Font) -> str:  # ф-я сокращает имя если оно длинное
        dots = '..'
        name_width = font.size(name)[0]
        dots_width = font.size(dots)[0]
        while name_width + dots_width > self.MAX_NAME_WIDTH:
            name = name[:-1]
            name_width = font.size(name)[0]
        return name + dots
