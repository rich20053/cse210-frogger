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
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_segment_collision(self, cast):
        """Identifies when two actors come into contact with each other and handle it appropriately.
           If it is a hazzard, the frog dies, if it is a helper, the frog rides safely
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cars = cast.get_actors("cars")
        trucks = cast.get_actors("trucks")
        frog = cast.get_first_actor("frog")
        frog.set_off_log_or_turtle()
        logs = cast.get_actors("logs")
        turtles = cast.get_actors("turtles")
        
        # Test for car collision
        for car in cars:
            carsegs = car.get_segments()
            first_x = carsegs[0].get_position().get_x()
            last_x = carsegs[1].get_position().get_x()
            if (frog.get_position().get_x()+20 >= first_x and
                frog.get_position().get_x()-20 <= last_x and
                frog.get_position().get_y() + 1 == carsegs[0].get_position().get_y()):
                    self._is_game_over = True
                    frog.set_text("*")
        
        # Test for truck collision
        for truck in trucks:
            trucksegs = truck.get_segments()
            first_x = trucksegs[0].get_position().get_x()
            last_x = trucksegs[3].get_position().get_x()
            if (frog.get_position().get_x()+20 >= first_x and
                frog.get_position().get_x()-20 <= last_x and
                frog.get_position().get_y() + 1 == trucksegs[0].get_position().get_y()):
                    self._is_game_over = True
                    frog.set_text("*")
        
        # If the frog is in the top half of the screen, the frog dies if not in contact (collision) with a Helper
        if (frog.get_position().get_y() + 1 < 7 * constants.CELL_SIZE and
            frog.get_position().get_y() + 1 > 1 * constants.CELL_SIZE):
            self._is_game_over = True

            # Frog in contact with a Log
            for log in logs:
                logsegs = log.get_segments()
                first_x = logsegs[0].get_position().get_x()
                last_x = logsegs[len(logsegs)-1].get_position().get_x()
                if (frog.get_position().get_x()+20 >= first_x and
                    frog.get_position().get_x()-20 <= last_x and
                    frog.get_position().get_y() + 1 == logsegs[0].get_position().get_y()):
                        self._is_game_over = False
                        frog.set_velocity(logsegs[0].get_velocity())
                        frog.set_on_log_or_turtle()

            # Frog in contact with a turtle
            for turtle in turtles:
                turtlesegs = turtle.get_segments()
                first_x = turtlesegs[0].get_position().get_x()
                last_x = turtlesegs[len(turtlesegs)-1].get_position().get_x()
                if (frog.get_position().get_x()+20 >= first_x and
                    frog.get_position().get_x()-20 <= last_x and
                    frog.get_position().get_y() + 1 == turtlesegs[0].get_position().get_y()):
                        self._is_game_over = False
                        frog.set_velocity(turtlesegs[0].get_velocity())
                        frog.set_on_log_or_turtle()
                    

            if (self._is_game_over == True):
                frog.set_text("*")
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message if the frog dies.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            x = int(constants.MAX_X / 2)
            y = 7 * constants.CELL_SIZE
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)
            lines = cast.get_actors("lines")
            for line in lines:
                cast.remove_actor("lines", line)
            score = cast.get_first_actor("score")
            score.game_over()
            frog = cast.get_first_actor("frog")
            frog.set_game_over()
