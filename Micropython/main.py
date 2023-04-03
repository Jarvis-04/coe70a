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
robotParam["driveBase"] = DriveBase(Motor(Port.B, Direction.COUNTERCLOCKWISE), Motor(Port.C, Direction.COUNTERCLOCKWISE), wheel_diameter=55, axle_track=135.0)
robot = RobotBody.createRobot(robotParam)


# while(1):
#     print(robot.color_2.color())
#     wait(500)
# Lift.seniorClaw2016(robot, "init")
# Lift.seniorClaw2016(robot, "lift")
# print(robot.color_2.color())
# wait(100000)
# Lift.seniorClaw2016(robot, "init")
# Movement.setSpeed(robot, speed = 200)
# Movement.nodeTraversal2016(robot, Color.GREEN, Color.RED)

# Lift.seniorClaw2016(robot, "init")
# Lift.seniorClaw2016(robot, "open")
# Lift.seniorClaw2016(robot, "lift")
# print(Detection.detectBlockReflection2016(robot, "container"))

# solution = Solution.robotSolutions(robot)
# Solution.robotSolutions.seniorSolution2016(solution)
# Movement.robotStop(robot)

# colorDict = {Color.GREEN:None, Color.RED:None, Color.BLUE:None, Color.YELLOW:None}
# currentColor = Detection.detectBlockReflection2016(robot, "tank")
# colorDict[currentColor] = 0
# print(currentColor)
# print(colorDict)
Movement.turnUntilLineOneSensor2016(robot, "RIGHT")
Detection.PIDlineFollowerUntilBlock2016(robot, 1000, 100, "LEFT")
Movement.forwardMovement(robot, 20)
Lift.setHolderPosition(robot, colorDict[currentColor] + 2, "turn")
Lift.seniorClaw2016(robot, "press")
Lift.seniorClaw2016(robot, "depress")
# Movement.forwardMovement(robot, 20)
# Movement.turnUntilLineOneSensor2016(robot, "LEFT")
# Detection.PIDlineFollowerUntilBlock2016(robot, 1000, 100, "LEFT")
# x = 1
# while(x == 1):
#     print(Detection.getBlockReflection2016(robot, "tank"))
#     print(Detection.detectTankColor2016(robot, "tank"))
# print("test")

# Movement.setSpeed(robot, 200)
# Movement.nodeTraversal2016(robot, "yellow", "blue")
# Movement.backwardMovements(robot, 300)
# wait(3000)
# Movement.nodeTraversal2016(robot, "yellow", "green")

# Lift.seniorClaw2016(robot, "lift")
# x = 1
# while (x == 1):
#     currentContainerColor = Detection.detectBlockReflection2016(robot, "container")
#     currentRGB = Detection.getBlockReflection2016(robot, "container")
#     print(currentContainerColor)
#     print(currentRGB)
# if (currentContainerColor == Color.GREEN):
#     Lift.seniorClaw2016(robot, "drop")
#     Lift.seniorClaw2016(robot, "open")
#     Movement.forwardMovement(robot, 90)
#     Lift.seniorClaw2016(robot, "close")
