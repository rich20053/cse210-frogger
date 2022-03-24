import constants
from game.casting.helper import Helper
from game.shared.point import Point


class Turtle(Helper):
    """
    Try not to run into this item.
    
    The responsibility of Obstacle is to select a random position and set it up as another way for a cycle to lose a game.

    Attributes:
        None.
    """
    def __init__(self, x, y, length, velocity):
        super().__init__(length)
        self.set_text("O")
        self.set_color(constants.GREEN)
        position = Point(x,y)
        newpos = position.scale(constants.CELL_SIZE)
        self.set_position(newpos)
        self._prepare_body(x,y, velocity)

        
