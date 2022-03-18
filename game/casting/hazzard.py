import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Hazzard(Actor):
    """
    Try not to run into this item.
    
    The responsibility of Obstacle is to select a random position and set it up as another way for a cycle to lose a game.

    Attributes:
        None.
    """
    def __init__(self):
        "Constructs a new Obstacle."
        super().__init__()
        self.set_text("O")
        self.set_color(constants.YELLOW)
        self.reset()
        
    def reset(self):
        """Selects a random position for the Obstacle."""
        x = random.randint(1, constants.COLUMNS- 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
