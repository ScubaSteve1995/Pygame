from __future__ import annotations
from typing import Optional, TYPE_CHECKING
import tcod
import tcod.event
from actions import Action, Escape_Action, Bump_Action
if TYPE_CHECKING:
    from engine import Engine


class Event_Handler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        
    def handle_events(self) -> None:
        for event in tcod.event.wait():
            action = self.dispatch(event)
            
            if action is None:
                continue
            action.perform()
            
            self.engine.handle_enemy_turns()
            self.engine.update_fov() # Update FOV before the player's next action.
            
            
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None
        
        key = event.sym
        player = self.engine.player
        
        if key == tcod.event.KeySym.UP:
            action = Bump_Action(player, dx = 0, dy = -1)
        
        elif key == tcod.event.KeySym.DOWN:
            action = Bump_Action(player, dx = 0, dy = 1)
            
        elif key == tcod.event.KeySym.LEFT:
            action = Bump_Action(player, dx=-1,dy=0)
            
        elif key == tcod.event.KeySym.RIGHT:
            action = Bump_Action(player, dx=1,dy=0)
            
        elif key == tcod.event.KeySym.ESCAPE:
            action = Escape_Action(player)
            
        return action                    