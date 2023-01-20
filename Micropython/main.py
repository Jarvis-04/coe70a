#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Local Imports of Fuction Module Library
import RobotBody
import Movement
import Detection
import Lift
import Solution

from Movement import forwardMovement

# Start Code Here!

# Creating A Elementary Robot
robotParam = RobotBody.createParam()
robotParam["comp"] = "elementary"
robotParam["ev3"] = EV3Brick()
robotParam["left_wheel"] = Motor(Port.B, Direction.COUNTERCLOCKWISE)
robotParam["right_wheel"] = Motor(Port.C, Direction.COUNTERCLOCKWISE)
robotParam["light_1"] = ColorSensor(Port.S1)
robotParam["light_2"] = ColorSensor(Port.S2)
robotParam["color_1"] = ColorSensor(Port.S4)
robotParam["motor_2"] = Motor(Port.D, Direction.COUNTERCLOCKWISE)
robotParam["motor_1"] = Motor(Port.A)
robotParam["driveBase"] = DriveBase(Motor(Port.B, Direction.COUNTERCLOCKWISE), Motor(Port.C, Direction.COUNTERCLOCKWISE), wheel_diameter=56, axle_track=184.0)
robot = RobotBody.createRobot(robotParam)

# Detection.lineFollowUntilBlock(robot, 1000, 150)

# Detection.PIDlineFollowerUntilBlock(robot, 1000, 100, "LEFT")

# Lift.elevatorReset(robot)
# for x in range(1,5):
#     Lift.elevatorDrop(robot,x)
#     sleep(1)
#     Lift.elevatorReset(robot)

# Detection.lineFollowUntilBlock(robot, 3000, 100)
# while (1):
#     print(robot.color_1.rgb()[2])
#     wait(100)
# Detection.lineFollowUntilBlock(robot, 3000, 100)
# Detection.PIDlineFollowerUntilBlock(robot, 3000, 100, "LEFT")

solution = Solution.robotSolutions(robot)
Solution.robotSolutions.elementarySolution(solution)


