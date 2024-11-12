import pygame

from src.card import Card
from src.hand import Hand
from src.deck import Deck
from src.row import Row
from src.table import Table
from src.ui.view_card import ViewCard, Fly
from src.ui.view_hand import ViewHand
from src.ui.view_row import ViewRow
from src.ui.view_table import ViewTable


class ViewGame:
    DISPLAY_COLOR = 'azure3'
    YGAP = 0
    XGAP = 30

    def __init__(self):
        # Существующие инициализации
        self.fly = Fly()
        rplayer1, rrow, rtable = self.calculate_geom_contants()
        self.vhand = ViewHand(Hand.load('[13<1>] [31<1>] [10<2>] [6<1>] [17<1>] [18<1>] '
                                        '[101<1>] [104<1>] [93<1>] [1<1>]'), rplayer1)

        row = Row()
        for i in range(1, 10):
            row.add_card(Card(i))
        self.vrow = ViewRow(row, rrow)

        if len(row.cards) >= 5:  # 5 карт в верхнем ряду карт, выбранных игроками
            upper_row = Row()
            lower_row = Row()
            upper_row.cards = row.cards[:5]
            lower_row.cards = row.cards[5:]

            self.vrow = ViewRow(upper_row, rrow)
            new_rrow = pygame.Rect(rrow.x, rrow.y + ViewCard.HEIGHT + self.YGAP, rrow.width, rrow.height)
            self.vrow2 = ViewRow(lower_row, new_rrow)
        else:
            self.vrow = ViewRow(row, rrow)
            self.vrow2 = None

        data = {
            "row1": "[11<1>] [24<1>] [33<5>]",
            "row2": "[5<1>] [6<1>] [7<2>] [8<1>] [99<5>]",
            "row3": "[20<1>] [21<2>] [32<1>]",
            "row4": "[45<1>] [56<1>]"
        }
        table = Table.load(data)
        self.vtable = ViewTable(table, rtable)

    def calculate_geom_contants(self):
        screen_width, screen_height = pygame.display.get_window_size()
        card_width = ViewCard.WIDTH
        card_height = ViewCard.HEIGHT
        self.YGAP = (screen_height - 5 * card_height) // 4
        rplayer = pygame.Rect(self.XGAP, self.YGAP, screen_width - 2*self.XGAP, self.YGAP + card_height)
        rrow = pygame.Rect(self.XGAP + card_width*8, self.YGAP + card_height * 2, rplayer.width, card_height)
        rtable = pygame.Rect(self.XGAP, self.YGAP + 1.5*card_height, screen_width - 2*self.XGAP, self.YGAP)
        return rplayer, rrow, rtable

    def model_update(self):
        self.fly.fly()

    def redraw(self, display: pygame.Surface):
        display.fill(self.DISPLAY_COLOR)
        self.vhand.redraw(display)
        self.vrow.redraw(display)
        if self.vrow2:  # если есть 2 ряд(т.е карт было больше 5)
            self.vrow2.redraw(display)
        self.vtable.redraw(display)
        self.fly.redraw(display)
        pygame.display.update()

    def event_processing(self, event: pygame.event.Event):
        if self.fly.animation_mode:
            return
        self.vhand.event_processing(event)
        self.vrow.event_processing(event)
        if self.vrow2:  # для второго ряда выбранных карт
            self.vrow2.event_processing(event)
        self.vtable.event_processing(event)

