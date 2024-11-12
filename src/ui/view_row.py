from src.row import Row
from src.card import Card
from src.ui.view_card import ViewCard
from src.resource import RESOURCE as RSC

import pygame


class ViewRow:
    def __init__(self, row: Row, bound: pygame.Rect):
        self.vrow: list[ViewRow] = self.create_view_row(row, bound)

    def redraw(self, display: pygame.Surface):
        for vc in self.vrow:
            vc.redraw(display)

    def event_processing(self, event: pygame.event.Event):
        for vc in self.vrow:
            vc.event_processing(event)

    def create_view_row(self, row: Row, bound: pygame.Rect):
        print('\ntable')
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

    # def create_view_s_row(self, row: Row, bound: pygame.Rect):
    #     print('\nrow')
    #     if row is None:
    #         return []
    #     length = len(row.cards)
    #     print('Row lengh: ', length)
    #     bx = bound.x
    #     by = bound.y
    #
    #     view_sel_cards = []
    #     max_cards_in_row = 5
    #
    #     for index, card in enumerate(row.cards):
    #         if index >= max_cards_in_row:
    #             bx = bound.x
    #             y_offset = RSC['card_ygap']
    #         else:
    #             y_offset = 0
    #
    #         vscard = ViewCard(card, x=bx, y=by + y_offset)
    #         view_sel_cards.append(vscard)
    #         bx += ViewCard.WIDTH + RSC["card_xgap"]
    #         if (index + 1) % max_cards_in_row == 0:
    #             by += ViewCard.HEIGHT + RSC["card_ygap"]
    #
    #         print(f'Add view row selected_card {vscard}')
    #     return view_sel_cards


