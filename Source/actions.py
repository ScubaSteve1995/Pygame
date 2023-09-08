from __future__ import annotations
from typing import Optional, Tuple, TYPE_CHECKING


if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity, Actor
    from game_map import Game_Map

class Action:
    def __init__(self, entity: Actor) -> None:
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
    
class Wait_Action(Action):
    def perform(self) -> None:
        pass
    


class ActionWithDirection(Action):
    def __init__(self, entity: Actor, dx: int, dy: int):
        super().__init__(entity)
        
        self.dx = dx
        self.dy = dy
        
    @property
    def dest_xy(self) -> Tuple[int, int]:
        return self.entity.x + self.dx, self.entity.y + self.dy
    
    @property
    def blocking_entity(self) -> Optional[Entity]:
        return self.engine.game_map.get_blocking_entity_at_location(*self.dest_xy)
    
    @property
    def target_actor(self) -> Optional[Actor]:
        return self.engine.game_map.get_actor_at_location(*self.dest_xy)
        
    def perform(self) -> None:
        raise NotImplementedError()
    


class Melee_Action(ActionWithDirection):
    def perform(self) -> None:
     target = self.target_actor
     if not target:
            return # No entity to attack.
        
     damage = self.entity.fighter.power - target.fighter.defense
     
     attack_desc = f"{self.entity.name.capitalize()} attacks {target.name}"
     if damage > 0:
         print(f"{attack_desc} for {damage} hit points.")
         target.fighter.hp -= damage
     else:
         print(f"{attack_desc} but does no damage.")
        
     
        

class Movement(ActionWithDirection):
   
    def perform(self, gamemap: Game_Map) -> None:
        dest_x, dest_y = self.dest_xy
        self.gamemap = gamemap
        
        if not self.gamemap.in_bounds(dest_x, dest_y):
            return # Destination is out of bounds.
        if not self.gamemap.tiles["walkable"][dest_x, dest_y]:
            return # Destination is blocked by a tile.
        if self.gamemap.get_blocking_entity_at_location(dest_x, dest_y):
            return # Destination is blocked by an entity.
        
        self.entity.move(self.dx, self.dy)
        
class Bump_Action(ActionWithDirection):
    def perform(self) -> None:
       if self.target_actor:
           return Melee_Action(self.entity, self.dx, self.dy).perform()
       else:
           return Movement(self.entity, self.dx, self.dy).perform()
