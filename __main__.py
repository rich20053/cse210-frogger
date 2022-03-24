import constants
from game.casting.boundary import Boundary

from game.casting.cast import Cast
from game.casting.car import Car
from game.casting.redcar import RedCar
from game.casting.score import Score
from game.casting.truck import Truck
from game.casting.frog import Frog
from game.casting.log import Log
from game.casting.turtle import Turtle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("frog", Frog())
    cast.add_actor("score", Score())

    # create hazzards
    # lane 1
    for i in range (3):
        lane1car = Car((i+1)*7, constants.LANE_1, constants.CAR_LENGTH,Point(-3, 0))
        cast.add_actor("cars", lane1car)

    # lane 2
    for i in range (3):
        lane2car = RedCar((i+1)*7, constants.LANE_2, constants.CAR_LENGTH,Point(5, 0))
        lane2car.set_color(constants.RED)
        cast.add_actor("cars", lane2car)

    # lane 3
    for i in range (3):
        lane3car = Car((i+1)*7+25, constants.LANE_3, constants.CAR_LENGTH,Point(-8, 0))
        cast.add_actor("cars", lane3car)

    # lane 4
    for i in range (3):
        lane4car = RedCar((i+1)*7, constants.LANE_4, constants.CAR_LENGTH,Point(10, 0))
        lane4car.set_color(constants.RED)
        cast.add_actor("cars", lane4car)

    # lane 5
    for i in range (3):
        lane5truck = Truck((i+1)*7-5, constants.LANE_5, constants.TRUCK_LENGTH,Point(-15, 0))
        cast.add_actor("trucks", lane5truck)

    # lane 6
    for i in range (3):
        lane6turtle = Turtle((i+1)*7-5, constants.LANE_6, constants.LG_TURTLE_LENGTH,Point(-10, 0))
        cast.add_actor("turtles", lane6turtle)

    # lane 7
    for i in range (3):
        lane7log = Log((i+1)*7-5, constants.LANE_7, constants.SM_LOG_LENGTH,Point(3, 0))
        cast.add_actor("logs", lane7log)

    # lane 8
    for i in range (2):
        lane8log = Log((i+1)*11-5, constants.LANE_8, constants.LG_LOG_LENGTH,Point(12, 0))
        cast.add_actor("logs", lane8log)

    # lane 9
    for i in range (3):
        lane9turtle = Turtle((i+1)*7-5, constants.LANE_9, constants.SM_TURTLE_LENGTH,Point(-5, 0))
        cast.add_actor("turtles", lane9turtle)

    # lane 10
    for i in range (3):
        lane10log = Log((i+1)*7-5, constants.LANE_10, constants.MD_LOG_LENGTH,Point(9, 0))
        cast.add_actor("logs", lane10log)

    # create boundaries

    for i in range (constants.COLUMNS):
        topline = Boundary()
        linepoint = Point(i+1, 1)
        newpos = linepoint.scale(constants.CELL_SIZE)        
        topline.set_position(newpos)
        topline.set_text("-")
        cast.add_actor("lines", topline)
        midline = Boundary()
        linepoint = Point(i+1, 7)
        newpos = linepoint.scale(constants.CELL_SIZE)        
        midline.set_position(newpos)
        midline.set_text("=")
        cast.add_actor("lines", midline)
        lowline = Boundary()
        linepoint = Point(i+1, 13)
        newpos = linepoint.scale(constants.CELL_SIZE)        
        lowline.set_position(newpos)
        lowline.set_text("-")
        cast.add_actor("lines", lowline)
        
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("check", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()