import pygame

from src.card import Card
from src.row import Row
from src.table import Table
from src.ui.view_card import ViewCard
from src.ui.view_row import ViewRow
from src.resource import RESOURCE as RSC


class ViewTable:
    def __init__(self, table: Table, bound: pygame.Rect):
        self.vtable: list[ViewTable] = self.create_view_table(table, bound)

    def redraw(self, display: pygame.Surface):
        for vr in self.vtable:
            vr.redraw(display)

    def event_processing(self, event: pygame.event.Event):
        for vr in self.vtable:
            vr.event_processing(event)

    def create_view_table(self, table: Table, bound: pygame.Rect):
        print('\ntable')
        if table is None:
            return []
        view_table = []
        by = bound.y
        for index, row in enumerate(table.rows):
            vrow = ViewRow(row, pygame.Rect(bound.x, by, bound.width, bound.height))
            view_table.append(vrow)
            by += ViewCard.HEIGHT + RSC["row_ygap"]

            print(f'Add view row {row}')

        return view_table
