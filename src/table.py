import json
from typing import List
from src.card import Card
from src.row import Row


class Table:
    def __init__(self):
        self.rows: List[Row] = [Row() for _ in range(4)]
