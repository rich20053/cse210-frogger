import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Boundary(Actor):
    """
    The boudary objects appear on the screen to show where the frog is safe.
    
    The frog cannot die when sitting on a boundary

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

        
