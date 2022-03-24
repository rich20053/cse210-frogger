from itertools import cycle
from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        frog = cast.get_first_actor("frog")
        score = cast.get_first_actor("score")
        lines = cast.get_actors("lines")
        cars = cast.get_actors("cars")
        trucks = cast.get_actors("trucks")
        turtles = cast.get_actors("turtles")
        logs = cast.get_actors("logs")
        messages = cast.get_actors("messages")
            



        self._video_service.clear_buffer()
        self._video_service.draw_actor(frog)
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(lines)
        for car in cars:
            csegments = car.get_segments()
            self._video_service.draw_actors(csegments)
        for truck in trucks:
            csegments = truck.get_segments()
            self._video_service.draw_actors(csegments)
        for turtle in turtles:
            csegments = turtle.get_segments()
            self._video_service.draw_actors(csegments)
        for log in logs:
            csegments = log.get_segments()
            self._video_service.draw_actors(csegments)

        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
