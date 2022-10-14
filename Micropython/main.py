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

from Movement import forwardMovement

# Start Code Here!

# Creating A Elementary Robot
robotParam = RobotBody.createParam()
robotParam["comp"] = "elementary"
robotParam["ev3"] = EV3Brick()
robotParam["left_wheel"] = Motor(Port.B)
robotParam["right_wheel"] = Motor(Port.C)
robotParam["driveBase"] = DriveBase(Motor(Port.B), Motor(Port.C), wheel_diameter=69.85, axle_track=133.35)
robot = RobotBody.createRobot(robotParam)

# Setting Linear Speed to 100 millimeters per second
Movement.setSpeed(robot = robot, speed = 100)

# Moving Forward for 100 millimeters

Movement.forwardMovement(robot = robot, distanceToTravel = 200)

hook_Motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
print(hook_Motor.angle())
hook_Motor.run_angle(100, -90)
hook_Motor.run_angle(100, 90)
wait(2000)