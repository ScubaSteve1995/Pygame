from components.AI import Hostile_Enemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char = "@",
    color = (255, 255, 255),
    name = "Player",
    ai_class = Hostile_Enemy,
    fighter = Fighter(hp = 30, defense = 2, power = 5),
)

orc = Actor(
    char = "o",
    color = (63, 127, 63),
    name = "Orc",
    ai_class=Hostile_Enemy,
    fighter=Fighter(hp = 10, defense = 0, power = 3),
)

troll = Actor(
    char = "T",
    color = (0, 127, 0),
    name = "Troll",
    ai_class=Hostile_Enemy,
    fighter=Fighter(hp = 16, defense = 1, power = 4),
)
