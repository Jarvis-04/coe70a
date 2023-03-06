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

# Start Code Here!

# Creating A Elementary Robot
# robotParam = RobotBody.createParam()
# robotParam["comp"] = "elementary"
# robotParam["ev3"] = EV3Brick()
# robotParam["left_wheel"] = Motor(Port.B, Direction.COUNTERCLOCKWISE)
# robotParam["right_wheel"] = Motor(Port.C, Direction.COUNTERCLOCKWISE)
# robotParam["light_1"] = ColorSensor(Port.S1)
# robotParam["light_2"] = ColorSensor(Port.S2)
# robotParam["color_1"] = ColorSensor(Port.S4)
# robotParam["motor_2"] = Motor(Port.D, Direction.COUNTERCLOCKWISE)
# robotParam["motor_1"] = Motor(Port.A)
# robotParam["driveBase"] = DriveBase(Motor(Port.B, Direction.COUNTERCLOCKWISE), Motor(Port.C, Direction.COUNTERCLOCKWISE), wheel_diameter=56, axle_track=184.0)
# robot = RobotBody.createRobot(robotParam)

# solution = Solution.robotSolutions(robot)
# Solution.robotSolutions.elementarySolution(solution)


# Creating A Senior Robot
robotParam = RobotBody.createParam()
robotParam["comp"] = "senior"
robotParam["ev3"] = EV3Brick()
robotParam["left_wheel"] = Motor(Port.B)
robotParam["right_wheel"] = Motor(Port.C)
robotParam["light_1"] = ColorSensor(Port.S3)
robotParam["light_2"] = ColorSensor(Port.S1)
robotParam["color_1"] = ColorSensor(Port.S2)
robotParam["color_2"] = ColorSensor(Port.S4)
robotParam["motor_1"] = Motor(Port.A)
robotParam["motor_2"] = Motor(Port.D)
robotParam["driveBase"] = DriveBase(Motor(Port.B, Direction.COUNTERCLOCKWISE), Motor(Port.C, Direction.COUNTERCLOCKWISE), wheel_diameter=50, axle_track=184.0)
robot = RobotBody.createRobot(robotParam)

solution = Solution.robotSolutions(robot)
Solution.robotSolutions.seniorSolution2016(solution)

# Movement.setSpeed(robot, 200)
# Movement.nodeTraversal2016(robot, "yellow", "blue")
# Movement.backwardMovements(robot, 300)
# wait(3000)
# Movement.nodeTraversal2016(robot, "yellow", "green")

# Lift.seniorClaw2016(robot, "lift")
# currentContainerColor = Detection.detectBlockColor2016(robot, "container")
# print(currentContainerColor)
# if (currentContainerColor == Color.GREEN):
#     Lift.seniorClaw2016(robot, "drop")
#     Lift.seniorClaw2016(robot, "open")
#     Movement.forwardMovement(robot, 90)
#     Lift.seniorClaw2016(robot, "close")
