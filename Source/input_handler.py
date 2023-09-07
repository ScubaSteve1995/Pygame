from typing import Optional
import tcod
import tcod.event
from actions import Action, Escape_Action, Bump_Action


class Event_Handler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None
        
        key = event.sym
        
        if key == tcod.event.KeySym.UP:
            action = Bump_Action(dx = 0, dy = -1)
        
        elif key == tcod.event.KeySym.DOWN:
            action = Bump_Action(dx = 0, dy = 1)
            
        elif key == tcod.event.KeySym.LEFT:
            action = Bump_Action(dx=-1,dy=0)
            
        elif key == tcod.event.KeySym.RIGHT:
            action = Bump_Action(dx=1,dy=0)
            
        elif key == tcod.event.KeySym.ESCAPE:
            action = Escape_Action()
            
        return action                    