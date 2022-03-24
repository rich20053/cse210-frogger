import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Frog(Actor):
    """
    Try not to run into this item.
    
    The responsibility of Obstacle is to select a random position and set it up as another way for a cycle to lose a game.

    Attributes:
        None.
    """
    def __init__(self):
        super().__init__()
        self.set_text("#")
        self.set_color(constants.GREEN)
        position = Point(int(constants.COLUMNS / 2), 14)
        newpos = position.scale(constants.CELL_SIZE)
        self.set_position(newpos)
        self._score = 0
        self._on_log_or_turtle = False
        self._is_game_over = False

    def move_next(self):
        """Moves the frog to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.

        """
        if (self._is_game_over):
            return
        x = (self._position.get_x() + self._velocity.get_x())
        if (x > constants.MAX_X - 41):
            x = constants.MAX_X - 41
        if (x < 0):
            x = 0
        y = (self._position.get_y() + self._velocity.get_y()) 
        if (y > constants.MAX_Y - 41):
            y = constants.MAX_Y - 41
        if (y < 0):
            y = constants.MAX_Y - 41
            self.add_score(1)

        self._position = Point(x, y)
    
    def add_score(self, score):
        self._score += score

    def get_score(self):
        tmp_score = self._score
        self._score = 0
        return(tmp_score)

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
    '''    
    def set_velocity_and_move(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        old_velocity = self._velocity.get_y()
        self._velocity = velocity
        new_velocity = self._velocity.get_y()
        #if (old_velocity != new_velocity):
        #    self.move_next()'''
    
    def set_on_log_or_turtle(self):
        self._on_log_or_turtle = True

    def set_off_log_or_turtle(self):
        self._on_log_or_turtle = False

    def is_on_log_or_turtle(self):
        return(self._on_log_or_turtle)
        
    def set_game_over(self):
        self._is_game_over = True
        

       
        
