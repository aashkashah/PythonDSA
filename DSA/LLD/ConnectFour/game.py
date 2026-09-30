from enum import Enum
from typing import Optional

from DSA.LLD.ConnectFour.board import Board
from DSA.LLD.ConnectFour.player import Player

class GameState(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    WON = "WON"
    DRAW = "DRAW"

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.state = GameState.IN_PROGRESS
        self.winner = Optional[Player] = None
        
    def make_move(self, player, column: int) -> bool:
            pass
     
    def get_current_player(self) -> Player:
        pass
    
    def get_game_state(self) -> GameState:
        pass
    
    def get_winner(self) -> Optional[Player]:
        pass
    
    def get_board(self) -> Board:
        pass