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
        self._ldirection = Point(0, -constants.CELL_SIZE)
        self._rdirection = Point(0, -constants.CELL_SIZE)
        self._new_game = False
        self._last_ldirection = 'w'
        self._last_rdirection = 'i'

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # Left cycle (red)
        # Prepare to increment score for every turn.
        lscore = cast.get_first_actor("lscore")
        # left
        if self._keyboard_service.is_key_down('a'):
            self._ldirection = Point(-constants.CELL_SIZE, 0)
            if self._last_ldirection != 'a':
                self._last_ldirection = 'a'
                lscore.add_points(1)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._ldirection = Point(constants.CELL_SIZE, 0)
            if self._last_ldirection != 'd':
                self._last_ldirection = 'd'
                lscore.add_points(1)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._ldirection = Point(0, -constants.CELL_SIZE)
            if self._last_ldirection != 'w':
                self._last_ldirection = 'w'
                lscore.add_points(1)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._ldirection = Point(0, constants.CELL_SIZE)
            if self._last_ldirection != 's':
                self._last_ldirection = 's'
                lscore.add_points(1)
        
        lcycle = cast.get_first_actor("lcycle")
        lcycle.turn_head(self._ldirection)

        # Right cycle (green)
        # Prepare to increment score for every turn.
        rscore = cast.get_first_actor("rscore")
        # left
        if self._keyboard_service.is_key_down('j'):
            self._rdirection = Point(-constants.CELL_SIZE, 0)
            if self._last_ldirection != 'j':
                self._last_ldirection = 'j'
                rscore.add_points(1)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._rdirection = Point(constants.CELL_SIZE, 0)
            if self._last_ldirection != 'l':
                self._last_ldirection = 'l'
                rscore.add_points(1)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._rdirection = Point(0, -constants.CELL_SIZE)
            if self._last_ldirection != 'i':
                self._last_ldirection = 'i'
                rscore.add_points(1)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._rdirection = Point(0, constants.CELL_SIZE)
            if self._last_ldirection != 'k':
                self._last_ldirection = 'k'
                rscore.add_points(1)
        
        rcycle = cast.get_first_actor("rcycle")
        rcycle.turn_head(self._rdirection)

        # Change cycle speed
        if self._keyboard_service.is_key_down('1'):
            speedchange = script.get_first_action("update")
            speedchange.set_speed(9)

        if self._keyboard_service.is_key_down('2'):
            speedchange = script.get_first_action("update")
            speedchange.set_speed(7)

        if self._keyboard_service.is_key_down('3'):
            speedchange = script.get_first_action("update")
            speedchange.set_speed(5)

        if self._keyboard_service.is_key_down('4'):
            speedchange = script.get_first_action("update")
            speedchange.set_speed(3)

        if self._keyboard_service.is_key_down('5'):
            speedchange = script.get_first_action("update")
            speedchange.set_speed(1)

        # Signal new game
        if self._keyboard_service.is_key_down('n'):
            collision = script.get_first_action("check")
            collision.start_new_game()
            all_messages = cast.get_actors("messages")
            for message in all_messages:
                cast.remove_actor("messages", message)
            rcycle.__init__()
            lcycle.__init__()
            lscore = cast.get_first_actor("lscore")
            lscore.__init__()
            rscore = cast.get_first_actor("rscore")
            rscore.__init__()
            all_obstacles = cast.get_actors("obstacles")
            for obstacle in all_obstacles:
                obstacle.__init__()
            all_prizes = cast.get_actors("prizes")
            for prize in all_prizes:
                prize.__init__()
            self._ldirection = Point(0, -constants.CELL_SIZE)
            self._rdirection = Point(0, -constants.CELL_SIZE)
            self._new_game = False
            self._last_ldirection = 'w'
            self._last_rdirection = 'i'
