import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Boundary(Actor):
    """
    Try not to run into this item.
    
    The responsibility of Obstacle is to select a random position and set it up as another way for a cycle to lose a game.

    Attributes:
        None.
    """
    def __init__(self):
        super().__init__()
        self.set_text("-")
        self.set_color(constants.WHITE)
        position = Point(0, 0)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)

        
