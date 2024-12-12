from pathlib import Path

import pygame

from src.resource import RESOURCE as RSC
from src.ui.view_game import ViewGame
from src.game_server import GameServer


class Application:
    def __init__(self):
        pygame.init()
        self.size = (self.width, self.height) = (RSC['width'], RSC['height'])
        self.display = pygame.display.set_mode(self.size)
        self.display.fill(ViewGame.DISPLAY_COLOR, (0, 0, self.width, self.height))
        pygame.display.set_caption("COW_006")
        try:
            icon_img = pygame.image.load('img/icon.png')
            pygame.display.set_icon(icon_img)
        except FileNotFoundError:
            pass
        # self.vgame = ViewGame()
        self.vgame = None

    def run(self):
        clock = pygame.time.Clock()
        running = True
        pygame.display.update()
        while running:
            # изменение модели
            self.vgame.model_update()
            # отрисовка изменений
            self.vgame.redraw(self.display)
            # реакция на кравиши и мышь
            for event in pygame.event.get():
                if (event.type == pygame.QUIT
                        or event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    running = False
                self.vgame.event_processing(event)
            clock.tick(RSC['FPS'])

    def connect_with_game(self, game_server: GameServer):
        self.vgame = ViewGame(game_server)


if __name__ == '__main__':
    app = Application()
    json_dir = Path(__file__).parent
    filename_to_load = json_dir / 'cow5bots_9turn.json'
    # filename_to_load = 'cow4bots_1turn.json'
    #filename_to_load = 'cow10bots_9turn.json'
    #filename_to_load = 'cow10bots_1turn.json'
    #filename_to_load = 'cow_2bots_9turn.json'
    game_server = GameServer.load_game(filename_to_load)
    app.connect_with_game(game_server)
    app.run()

