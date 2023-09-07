from __future__ import annotations
from typing import TYPE_CHECKING

from engine  import Engine
from entity import Entity

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class Action:
   def perform(self, engine: Engine, entity: Entity) -> None:
       raise NotImplementedError()
         

class Escape_Action(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()
    
class ActionWithDirection(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        
        self.dx = dx
        self.dy = dy
        
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError()
    
class Melee_Action(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
        if not target:
            return # No entity to attack.
        
        print(f"You kick the {target.name}, much to it's annoyance!!")
        

class Movement(ActionWithDirection):
   
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        
        if not engine.game_map.in_bounds(dest_x, dest_y):
            return # Destination is out of bounds.
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return # Destination is blocked by a tile.
        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return # Destination is blocked by an entity.
        
        entity.move(self.dx, self.dy)
        
class Bump_Action(ActionWithDirection):
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        
        if engine.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return Melee_Action(self.dx, self.dy).perform(engine, entity)
        else:
            return Movement(self.dx, self.dy).perform(engine, entity)
        
