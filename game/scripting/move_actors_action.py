from game.scripting.action import Action
from game.shared.point import Point
PACE = 6   #  How fast the snake will move - move once every 5 cycles
FROGPACE = 5 #  How fast the snake will grow - grow once every 25 cycles


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """
    def __init__(self):
        """
        contructor sets the initial speed of moving
        """
        self._pace = PACE
        self._speed = self._pace
        self._frogpace = FROGPACE
        self._frogspeed = self._frogpace
        
    def execute (self, cast, script):
        """Executes the move actors action.

        Move all actors based on velocity of the actor

        Speed is based on the PACE set at beginning, but can be adjusted on the keyboard
        Growth indicates how fast the tail will grow.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        frog = cast.get_first_actor("frog")
        score = cast.get_first_actor("score")
        score.add_points(frog.get_score())
        self._speed -= 1
        if self._speed == 0:
            self._speed = self._pace
            cars = cast.get_actors("cars")
            for car in cars:
                car.move_next()
            trucks = cast.get_actors("trucks")
            for truck in trucks:
                truck.move_next()
            turtles = cast.get_actors("turtles")
            for turtle in turtles:
                turtle.move_next()
            logs = cast.get_actors("logs")
            for log in logs:
                log.move_next()
            frog.move_next()
        

    def set_speed (self, speed):
        self.pace = speed
        self.growth = speed

        
