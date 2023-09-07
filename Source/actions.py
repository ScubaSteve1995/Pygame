from __future__ import annotations
from typing import Optional, Tuple, TYPE_CHECKING

from engine  import Engine
from entity import Entity

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class Action:
    def __init__(self, entity: Entity) -> None:
        super().__init__()
        self.entity = entity
        
    @property
    def engine(self) -> Engine:
        # Return the engine that this action belongs to. #
        return self.entity.gamemap.engine
        
    def perform(self) -> None:
       raise NotImplementedError()
         



class Escape_Action(Action):
    def perform(self) -> None:
        raise SystemExit()
    


class ActionWithDirection(Action):
    def __init__(self, entity: Entity, dx: int, dy: int):
        super().__init__(entity)
        
        self.dx = dx
        self.dy = dy
        
    @property
    def dest_xy(self) -> Tuple[int, int]:
        return self.entity.x + self.dx, self.entity.y + self.dy
    
    @property
    def blocking_entity(self) -> Optional[Entity]:
        return self.engine.game_map.get_blocking_entity_at_location(*self.dest_xy)
        
    def perform(self) -> None:
        raise NotImplementedError()
    


class Melee_Action(ActionWithDirection):
    def perform(self) -> None:
     target = self.blocking_entity
     if not target:
            return # No entity to attack.
        
     print(f"You kick the {target.name}, much to it's annoyance!!")
        

class Movement(ActionWithDirection):
   
    def perform(self) -> None:
        dest_x, dest_y = self.dest_xy
        
        if not self.game_map.in_bounds(dest_x, dest_y):
            return # Destination is out of bounds.
        if not self.game_map.tiles["walkable"][dest_x, dest_y]:
            return # Destination is blocked by a tile.
        if self.game_map.get_blocking_entity_at_location(dest_x, dest_y):
            return # Destination is blocked by an entity.
        
        self.entity.move(self.dx, self.dy)
        
class Bump_Action(ActionWithDirection):
    def perform(self) -> None:
       if self.blocking_entity:
           return Melee_Action(self.entity, self.dx, self.dy).perform()
       else:
           return Movement(self.entity, self.dx, self.dy).perform()
