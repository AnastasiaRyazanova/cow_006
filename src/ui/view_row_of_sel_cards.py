from src.card import Card
from src.player import Player
from src.ui.view_card import ViewCard
from src.resource import RESOURCE as RSC

import pygame
from pygame import font


class ViewSelCards:
    def __init__(self, selected_cards: list[tuple[Card, Player]], bound: pygame.Rect):
        self.vscards: list[tuple[ViewCard, pygame.Surface]] = self.create_view_scards(selected_cards, bound)

    def redraw(self, display: pygame.Surface):
        for vcard, name_surface in self.vscards:
            vcard.redraw(display)
            display.blit(name_surface, (vcard.x, vcard.y + ViewCard.HEIGHT))

    def event_processing(self, event: pygame.event.Event):
        for vcard, _ in self.vscards:
            vcard.event_processing(event)

    def create_view_scards(self, selected_cards: list[tuple[Card, Player]], bound: pygame.Rect):
        print('\nselected_cards')
        if not selected_cards:
            return []
        bx = bound.x
        by = bound.y

        view_sel_cards = []
        basic_font = font.SysFont('arial', 24)

        for index, (card, player) in enumerate(selected_cards):
            vcard = ViewCard(card, x=bx, y=by)
            name_surface = basic_font.render(player.name, True, (180, 0, 0))
            view_sel_cards.append((vcard, name_surface))
            bx += ViewCard.WIDTH + RSC["card_xgap"]

            if (index + 1) % 5 == 0:  # переход на следующую строку после 5 карт
                bx = bound.x
                by += ViewCard.HEIGHT + RSC["card_ygap"]

            print(f'Add selected card {card} from {player.name}')

        return view_sel_cards



