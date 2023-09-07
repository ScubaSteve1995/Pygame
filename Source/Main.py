import tcod
from engine import Engine
from entity import Entity
from procgen import generate_dungeon
from input_handler import Event_Handler


def main()-> None:
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    
    map_width = 80
    map_height = 45
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    
    
   
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    
    event_handler = Event_Handler()
    
    player = Entity(int(SCREEN_WIDTH /2), int(SCREEN_HEIGHT / 2), "@", (255, 255, 255))
    npc = Entity(int(SCREEN_WIDTH /2 - 5), int(SCREEN_HEIGHT / 2), "@", (255, 255, 0))
    entities = {npc, player}
    game_map = generate_dungeon(map_width,map_height)
    
    engine = Engine(entities = entities, event_handler = event_handler,game_map = game_map, player = player)
    
    with tcod.context.new_terminal(
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        tileset = tileset,
        title = "Yet another Roguelike",
        vsync = True,
    ) as context:
        root_console = tcod.console.Console(SCREEN_WIDTH,SCREEN_HEIGHT,order="F")
        while True:
            engine.render(console = root_console, context = context)
            
            events = tcod.event.wait()
            engine.handle_events(events)
            
            
    

if __name__ == "__main__":
    main()    