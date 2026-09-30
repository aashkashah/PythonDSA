from enum import Enum
from typing import Optional

class DiscColor(Enum):
    RED = "RED"
    YELLOW = "YELLOW" 

class Board:
    def __init__(self, rows: int = 6, cols: int = 7):
        self.rows = rows
        self.cols = cols
        self.grid: list[list[Optional[DiscColor]]] = [
            [None for _ in range(cols)] for _ in range(rows)
        ]
        
    def get_rows(self) -> int:
        return self.rows
    
    def get_cols(self) -> int:
        return self.cols
    
    def can_place(self, coumn: int) -> bool:
        pass
    
    def place_disc(self, column: int, color: DiscColor) -> int:
        pass
    
    def check_win(self, row: int, column: int, color: DiscColor) -> bool:
        pass
    
    def is_full(self) -> bool:
        pass
    
    def get_cell(self, row: int, column: int) -> Optional[DiscColor]:
        pass
    
    def _count_in_direction(self) -> int:
        pass
    
    def _in_bounds(self, row: int, column: int) -> bool:
        pass
    