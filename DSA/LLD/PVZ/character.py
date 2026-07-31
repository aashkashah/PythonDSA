
from enum import Enum


class CharacterType(Enum):
    Sunflower = 1
    Chomper = 2
    Peashooter = 3
    
class Character:
    
    def __init__(self, characterType: CharacterType):
        self._characterType = characterType 
