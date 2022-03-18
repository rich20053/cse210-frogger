import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the their trail, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_lgame_over = False
        self._is_rgame_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_rgame_over and not self._is_lgame_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the palyer collides with one of segments of other player.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        obstacles = cast.get_actors("obstacles")
        prizes = cast.get_actors("prizes")
        lcycle = cast.get_first_actor("lcycle")
        lhead = lcycle.get_segments()[0]
        lsegments = lcycle.get_segments()[1:]
        lscore = cast.get_first_actor("lscore")
        rscore = cast.get_first_actor("rscore")
        
        for segment in lsegments:
            if lhead.get_position().equals(segment.get_position()):
                self._is_lgame_over = True
        
        rcycle = cast.get_first_actor("rcycle")
        rhead = rcycle.get_segments()[0]
        rsegments = rcycle.get_segments()[1:]
        
        for segment in rsegments:
            if rhead.get_position().equals(segment.get_position()):
                self._is_rgame_over = True

        for segment in rsegments:
            if lhead.get_position().equals(segment.get_position()):
                self._is_lgame_over = True

        for segment in lsegments:
            if rhead.get_position().equals(segment.get_position()):
                self._is_rgame_over = True

        if rhead.get_position().equals(lhead.get_position()):
                self._is_rgame_over = True
                self._is_lgame_over = True

        for obstacle in obstacles:
            if rhead.get_position().equals(obstacle.get_position()):
                self._is_rgame_over = True
            if lhead.get_position().equals(obstacle.get_position()):
                self._is_lgame_over = True
        
        for prize in prizes:
            if rhead.get_position().equals(prize.get_position()):
                rscore.add_points(25)
                cast.remove_actor("prizes",prize)
            if lhead.get_position().equals(prize.get_position()):
                lscore.add_points(25)
                cast.remove_actor("prizes",prize)
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message if a player collides with their opponent's trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_rgame_over:
            rcycle = cast.get_first_actor("rcycle")
            rsegments = rcycle.get_segments()
            rcycle.set_game_over()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!  Press 'n' to begin a new game.")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in rsegments:
                segment.set_color(constants.WHITE)

        if self._is_lgame_over:
            lcycle = cast.get_first_actor("lcycle")
            lsegments = lcycle.get_segments()
            lcycle.set_game_over()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!  Press 'n' to begin a new game.")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in lsegments:
                segment.set_color(constants.WHITE)
    
    def start_new_game(self):
        """Resets 'game over' to restart the game.
        
        Args:
            none.
        """
        self._is_lgame_over = False
        self._is_rgame_over = False
    

