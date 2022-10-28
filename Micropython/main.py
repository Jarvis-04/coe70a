#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

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
robotParam["motor_2"] = Motor(Port.D)
robotParam["motor_1"] = Motor(Port.A)
robotParam["driveBase"] = DriveBase(Motor(Port.B, Direction.COUNTERCLOCKWISE), Motor(Port.C, Direction.COUNTERCLOCKWISE), wheel_diameter=69.85, axle_track=195.0)
robot = RobotBody.createRobot(robotParam)

solution = Solution.robotSolutions(robot)
Solution.robotSolutions.elementarySolution(solution)

