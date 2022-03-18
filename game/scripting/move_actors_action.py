from game.scripting.action import Action
from game.shared.point import Point
PACE = 5    #  How fast the snake will move - move once every 5 cycles
GROWTH = 5 #  How fast the snake will grow - grow once every 25 cycles


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
        self.pace = PACE
        self.speed = self.pace
        self.growth = GROWTH
        self.growth_speed = self.growth

    def execute (self, cast, script):
        """Executes the move actors action.

        Move all actors based on velocity of the actor

        Speed is based on the PACE set at beginning, but can be adjusted on the keyboard
        Growth indicates how fast the tail will grow.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        lscore = cast.get_first_actor("lscore")
        rscore = cast.get_first_actor("rscore")
        lcycle = cast.get_first_actor("lcycle")
        rcycle = cast.get_first_actor("rcycle")
        all_actors = cast.get_all_actors()
        self.speed -= 1
        if self.speed == 0:
            self.speed = self.pace
            for actor in all_actors:
                actor.move_next()
        self.growth_speed -= 1
        if self.growth_speed == 0:
            self.growth_speed = self.growth
            if not rcycle.is_game_over:
                rscore.add_points(1)
            rcycle.grow_tail(1)
            if not lcycle.is_game_over:
                lscore.add_points(1)
            lcycle.grow_tail(1)    

    def set_speed (self, speed):
        self.pace = speed
        self.growth = speed
        
