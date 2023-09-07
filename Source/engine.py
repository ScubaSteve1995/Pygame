from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console
from game_map import Game_Map
from actions import Escape_Action, Movement
from entity import Entity
from input_handler import Event_Handler


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: Event_Handler, game_map: Game_Map, player: Entity) -> None:
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player
        
    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)
            if action is None:
                continue
            action.perform(self, self.player)
            
            
    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, entity.color)
        context.present(console)
        
        console.clear()    