from src.card import Card
from src.player import Player
from src.table import Table
from src.ui.view_card import ViewCard
from src.resource import RESOURCE as RSC

import pygame
from pygame import font


class ViewSelCards:
    def __init__(self, sel_cards: list[tuple[Card, Player]], bound: pygame.Rect):
        self.bound = bound
        self.vscards: list[tuple[ViewCard, pygame.Surface]] = self.create_view_scards(sel_cards, bound)

    def redraw(self, display: pygame.Surface):
        for vcard, name_surface in self.vscards:
            vcard.redraw(display)
            display.blit(name_surface, (vcard.x, vcard.y + ViewCard.HEIGHT))

    def event_processing(self, event: pygame.event.Event):
        for vcard, _ in self.vscards:
            vcard.event_processing(event)

    def create_view_scards(self, sel_cards: list[tuple[Card, Player]], bound: pygame.Rect):
        print('\nselected_cards')
        if not sel_cards:
            return []
        bx = bound.x
        by = bound.y

        view_sel_cards = []
        basic_font = font.SysFont('arial', 24)

        for index, (card, player) in enumerate(sel_cards):
            vcard = ViewCard(card, x=bx, y=by)
            name_surface = basic_font.render(player.name, True, ('darkslategray'))
            view_sel_cards.append((vcard, name_surface))
            bx += ViewCard.WIDTH + RSC["card_xgap"]

            if (index + 1) % 5 == 0:  # переход на следующую строку после 5 карт
                bx = bound.x
                by += ViewCard.HEIGHT + 4*RSC["card_ygap"]

            print(f'-----Add selected card {card} from {player.name}----')
            print(f'---Выбранные карты: {view_sel_cards}----')

        return view_sel_cards



