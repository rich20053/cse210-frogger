import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._game_is_over = False
        self._points = 0
        self.add_points(0)
        self.set_text("Score: 0")
        self.set_color(constants.WHITE)
        position = Point(0, 0)
        self.set_position(position)
  
    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        if (not self._game_is_over):
            self._points += points
            self.set_text(f"Score: {self._points}")

    def game_over(self):
        self._game_is_over = True