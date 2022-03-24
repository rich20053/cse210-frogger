import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the player.
    
    The responsibility of ControlActorsAction is to get the direction and move the palyer's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, 0)
        self._new_game = False

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        frog = cast.get_first_actor("frog")
        velocity = self._keyboard_service.get_direction()
        if (frog.is_on_log_or_turtle()):
            if ((velocity.get_y() != 0) or (velocity.get_x() != 0)):
                frog.set_velocity(velocity)
        else:
            frog.set_velocity(velocity)
    

        '''
        # Signal new game
        if self._keyboard_service.is_key_down('n'):
            collision = script.get_first_action("check")
            collision.start_new_game()
            all_messages = cast.get_actors("messages")
            for message in all_messages:
                cast.remove_actor("messages", message)
            score = cast.get_first_actor("score")
            cast.remove_actor("score", score)
            cast.add_actor("score", Score())
            
            self._new_game = False'''
            
