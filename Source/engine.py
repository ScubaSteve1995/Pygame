from __future__ import annotations
from typing import TYPE_CHECKING
from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov
from actions import Escape_Action, Movement
from input_handler import Event_Handler

if TYPE_CHECKING:
    from entity import Entity
    from game_map import Game_Map


class Engine:
    game_map: Game_Map
    def __init__(self, player: Entity):
        self.event_handler: Event_Handler = Event_Handler(self)
        self.player = player
   
        
    def handle_enemy_turns(self) -> None:
        for entity in self.game_map.entities - {self.player}:
            print(f'The {entity.name} wonders when it will get to take a real turn.')
        
   
    def update_fov(self) -> None:
        # Recompute the visible area based on the Player's point of view.
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius = 8,
        )
        # If the tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible
            
            
    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)
        
                
        context.present(console)
        
        console.clear()    