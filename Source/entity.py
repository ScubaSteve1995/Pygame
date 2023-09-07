from __future__ import annotations
import copy
from typing import Optional, Tuple, TypeVar, TYPE_CHECKING
if TYPE_CHECKING:
    from game_map import Game_Map
T = TypeVar("T", bound = "Entity")

class Entity:
    
    gememap: Game_Map
    def __init__(
        self,
        gamemap: Optional[Game_Map] = None, 
        x: int = 0, 
        y: int = 0, 
        char: str = "?", 
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        blocks_movement: bool = False,
    ):
        
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap:
            self.gamemap = gamemap
            gamemap.entities.add(self)
        
    def spawn(self: T, gamemap: Game_Map, x: int, y: int) ->T:
        # Spawn a copy of this instance at the given location #
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)
        return clone
    
    def place(self, x: int, y: int, gamemap: Optional[Game_Map] = None) -> None:
        self.x = x
        self.y = y
        if gamemap:
            if hasattr(self, "gamemap"):
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)
        
    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy    