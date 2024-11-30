from src.row import Row
from src.card import Card
from src.ui.view_card import ViewCard
from src.resource import RESOURCE as RSC

import pygame


class ViewRow:
    def __init__(self, row: Row, bound: pygame.Rect):
        self.bound = bound
        self.vrow: list[ViewRow] = self.create_view_row(row, bound)

    def redraw(self, display: pygame.Surface):
        for vc in self.vrow:
            vc.redraw(display)

    def event_processing(self, event: pygame.event.Event):
        for vc in self.vrow:
            vc.event_processing(event)

    def create_view_row(self, row: Row, bound: pygame.Rect):
        if row is None:
            return []
        bx = bound.x
        by = bound.y

        view_cards = []

        for card in row.cards:
            vcard = ViewCard(card, x=bx, y=by)
            view_cards.append(vcard)
            bx += ViewCard.WIDTH + RSC["card_xgap"]

            print(f'Add view row card {card}')

        return view_cards


