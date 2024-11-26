import pygame

from src.resource import RESOURCE as RSC
from src.card import Card
from src.hand import Hand
from src.ui.view_card import ViewCard


class ViewHand:
    def __init__(self, hand: Hand, bound: pygame.Rect):
        self.vcards: list[ViewCard] | None = self.create_view_hand(hand, bound)
        self.bound = bound

    def redraw(self, display: pygame.Surface):
        for vc in self.vcards:
            if vc is None:
                continue
            vc.redraw(display)

    def event_processing(self, event: pygame.event.Event):
        for vc in self.vcards:
            if vc is None:
                continue
            vc.event_processing(event)

    def create_view_hand(self, hand: Hand, bound: pygame.Rect):
        print('\nhand')
        if hand is None:
            return []
        length = len(hand)
        #bx, by, bw, bh = bound
        bx = bound.x
        by = bound.y
        bw = bound.width
        bh = bound.height
        print('Hand Bounds:', bx, by, bw, bh)
        vcards = []
        for n, card in enumerate(hand):
            vcard = ViewCard(card, x=bx + n * (ViewCard.WIDTH + RSC["card_xgap"]), y=by)
            print(f'Add view card {card}')
            vcards.append(vcard)
        return vcards
