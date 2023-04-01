#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from RobotBody import WROrobot
import Movement
import Detection
import Lift
from time import sleep

class robotSolutions:
    # Define constants here

    def __init__(self, testRobot:WROrobot):
        self.testRobot = testRobot

    def elementarySolution(self):
        #1
        Detection.stopOnLine(self.testRobot, 100)
        Movement.forwardMovement(self.testRobot, 65)
        Movement.turnOnSpot(self.testRobot, -45)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Movement.PIDlineFollower(self.testRobot, 180, 100, "RIGHT")
        Movement.setSpeed(self.testRobot, 100)
        dropNum = Detection.push(self.testRobot, 80)
        Movement.setSpeed(self.testRobot, 100)

        Movement.backwardMovement(self.testRobot, 50)
        Movement.turnUntilLine(self.testRobot, "RIGHT")
        Lift.dropOff(self.testRobot, dropNum)
        Movement.PIDlineFollower(self.testRobot, 380, 100, "LEFT")
        #2
        Movement.setSpeed(self.testRobot, 100)
        dropNum = Detection.push(self.testRobot, 130)
        Movement.setSpeed(self.testRobot, 100)

        Movement.backwardMovement(self.testRobot, 50)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Lift.dropOff(self.testRobot, dropNum)
        #3
        Movement.forwardMovement(self.testRobot, 100)
        Movement.turnOnSpot(self.testRobot, 100)
        Movement.forwardMovement(self.testRobot, 280)
        Movement.turnUntilLine(self.testRobot, "RIGHT")
        Movement.PIDlineFollower(self.testRobot, 420, 30, "RIGHT")
        Detection.stopOnLine(self.testRobot, 100)
        Movement.forwardMovement(self.testRobot, 65)
        Movement.turnOnSpot(self.testRobot, -45)
        Movement.turnUntilLine(self.testRobot,"LEFT")
        Movement.turnOnSpot(self.testRobot, 15)
        Movement.setSpeed(self.testRobot, 100)
        dropNum = Detection.push(self.testRobot, 190)
        Movement.setSpeed(self.testRobot, 100)

        Movement.backwardMovement(self.testRobot, 80)
        Movement.turnUntilLine(self.testRobot, "RIGHT")
        Lift.dropOff(self.testRobot, dropNum)
        Movement.forwardMovement(self.testRobot, 10)
        Movement.turnOnSpot(self.testRobot, -90)
        #4
        Movement.arcTurn(self.testRobot, 411, 146, 200, "LEFT", 4020)
        Movement.forwardMovement(self.testRobot, 160)
        Movement.PIDlineFollower(self.testRobot, 180, 30, "RIGHT")
        Detection.stopOnLine(self.testRobot, 100)
        Movement.forwardMovement(self.testRobot, 65)
        Movement.turnOnSpot(self.testRobot, -45)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Movement.turnOnSpot(self.testRobot, 15)
        Movement.setSpeed(self.testRobot, 100)
        dropNum = Detection.push(self.testRobot, 190)
        Movement.setSpeed(self.testRobot, 100)

        Movement.backwardMovement(self.testRobot, 80)
        Movement.turnUntilLine(self.testRobot, "RIGHT")
        Lift.dropOff(self.testRobot, dropNum)
        #5
        Movement.turnOnSpot(self.testRobot, -15)
        Movement.forwardMovement(self.testRobot, 100)
        Movement.turnOnSpot(self.testRobot, 85)
        Movement.PIDlineFollower(self.testRobot, 740, 30, "LEFT")
        Detection.stopOnLine(self.testRobot, 100)
        Movement.forwardMovement(self.testRobot, 65)
        Movement.turnOnSpot(self.testRobot, 45)
        Movement.turnUntilLine(self.testRobot, "RIGHT")
        Movement.PIDlineFollower(self.testRobot, 140, 100, "LEFT")
        dropNum = Detection.push(self.testRobot, 100)

        Movement.backwardMovement(self.testRobot, 50)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Lift.dropOff(self.testRobot, dropNum)
        Movement.PIDlineFollower(self.testRobot, 340, 100, "LEFT")
        #6
        Movement.setSpeed(self.testRobot, 100)
        dropNum = Detection.push(self.testRobot, 130)
        Movement.setSpeed(self.testRobot, 100)

        Movement.backwardMovement(self.testRobot, 50)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Lift.dropOff(self.testRobot, dropNum)
        #END
        Movement.PIDlineFollower(self.testRobot, 220, 100, "RIGHT")
        Movement.turnOnSpot(self.testRobot, -90)
        Movement.forwardMovement(self.testRobot, 100)

    def elementarySolution2016(self):
        blockNumber = 1
        Movement.setSpeed(robot = self.testRobot, speed = 100)
        Lift.elevatorReset(self.testRobot)
        Movement.dualSensorPIDlineFollower(self.testRobot, 350, self.testRobot.DRIVE_SPEED)
        Movement.turnOnSpot(self.testRobot, -35)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Movement.dualSensorPIDlineFollower(self.testRobot, 300, self.testRobot.DRIVE_SPEED)
        Detection.lineFollowUntilLineIntersection(self.testRobot, 500, self.testRobot.DRIVE_SPEED)
        Movement.forwardMovement(self.testRobot, 100)
        Movement.turnOnSpot(self.testRobot, -85)
        Movement.turnUntilLine(self.testRobot, "RIGHT")
        Detection.lineFollowUntilBlock(self.testRobot, 300, self.testRobot.DRIVE_SPEED)
        # do block detect and replace here
        if Detection.detectBlockColor(self.testRobot) == Color.RED:
            # Picking red block
            Movement.backwardMovement(self.testRobot, 120)
            Lift.clawGrab(self.testRobot, "release")
            Movement.forwardMovement(self.testRobot, 110)
            Lift.clawGrab(self.testRobot, "pick")
            Movement.forwardMovement(self.testRobot, 120)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Movement.dualSensorPIDlineFollower(self.testRobot, 130, self.testRobot.DRIVE_SPEED)
            # Placing blue block
            Lift.elevatorDrop(self.testRobot, blockNumber)
            blockNumber = blockNumber + 1
            Lift.elevatorReset(self.testRobot)
        else:
            Movement.forwardMovement(self.testRobot, 120)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
        Detection.lineFollowUntilBlock(self.testRobot, 3000, self.testRobot.DRIVE_SPEED)
        #  do block detect and replce here
        if Detection.detectBlockColor(self.testRobot) == Color.RED:
            # Picking red block
            Movement.backwardMovement(self.testRobot, 120)
            Lift.clawGrab(self.testRobot, "release")
            Movement.forwardMovement(self.testRobot, 110)
            Lift.clawGrab(self.testRobot, "pick")
            Movement.forwardMovement(self.testRobot, 120)
            Movement.turnOnSpot(self.testRobot, 90)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Movement.dualSensorPIDlineFollower(self.testRobot, 130, self.testRobot.DRIVE_SPEED)
            # Placing blue block
            Lift.elevatorDrop(self.testRobot, blockNumber)
            blockNumber = blockNumber + 1
            Lift.elevatorReset(self.testRobot)
        else :
            Movement.forwardMovement(self.testRobot, 120)
            Movement.turnOnSpot(self.testRobot, 90)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
        Detection.lineFollowUntilBlock(self.testRobot, 3000, self.testRobot.DRIVE_SPEED)
        #  do block detect and replace here
        if Detection.detectBlockColor(self.testRobot) == Color.RED:
            # Picking red block
            Movement.backwardMovement(self.testRobot, 120)
            Lift.clawGrab(self.testRobot, "release")
            Movement.forwardMovement(self.testRobot, 110)
            Lift.clawGrab(self.testRobot, "pick")
            Movement.forwardMovement(self.testRobot, 90)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Movement.dualSensorPIDlineFollower(self.testRobot, 130, self.testRobot.DRIVE_SPEED)
            # Placing blue block
            Lift.elevatorDrop(self.testRobot, blockNumber)
            blockNumber = blockNumber + 1
            Lift.elevatorReset(self.testRobot)
        else:
            Movement.forwardMovement(self.testRobot, 90)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
        Detection.lineFollowUntilBlock(self.testRobot, 3000, self.testRobot.DRIVE_SPEED)
        # do block detect and replace here
        if Detection.detectBlockColor(self.testRobot) == Color.RED:
            # Picking red block
            Movement.backwardMovement(self.testRobot, 120)
            Lift.clawGrab(self.testRobot, "release")
            Movement.forwardMovement(self.testRobot, 110)
            Lift.clawGrab(self.testRobot, "pick")
            Movement.forwardMovement(self.testRobot, 120)
            Movement.turnOnSpot(self.testRobot, 140)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Movement.dualSensorPIDlineFollower(self.testRobot, 130, self.testRobot.DRIVE_SPEED)
            # Placing blue block
            Lift.elevatorDrop(self.testRobot, blockNumber)
            blockNumber = blockNumber + 1
            Lift.elevatorReset(self.testRobot)
        else :
            Movement.forwardMovement(self.testRobot, 120)
            Movement.turnOnSpot(self.testRobot, 140)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
        Detection.lineFollowUntilBlock(self.testRobot, 3000, self.testRobot.DRIVE_SPEED)
        # do block detect and replace here
        if Detection.detectBlockColor(self.testRobot) == Color.RED:
            # Picking red block
            Movement.backwardMovement(self.testRobot, 120)
            Lift.clawGrab(self.testRobot, "release")
            Movement.forwardMovement(self.testRobot, 110)
            Lift.clawGrab(self.testRobot, "pick")
            Movement.forwardMovement(self.testRobot, 130)
            Movement.turnOnSpot(self.testRobot, 35)
            Movement.forwardMovement(self.testRobot, 120)
            # Placing blue block
            Lift.elevatorDrop(self.testRobot, blockNumber)
            blockNumber = blockNumber + 1
            Lift.elevatorReset(self.testRobot)
        else:
            Movement.forwardMovement(self.testRobot, 120)
            Movement.turnOnSpot(self.testRobot, 35)

        Detection.stopOnLine(self.testRobot, self.testRobot.DRIVE_SPEED)
        Movement.forwardMovement(self.testRobot, 80)
        Detection.stopOnLine(self.testRobot, self.testRobot.DRIVE_SPEED)
        Movement.forwardMovement(self.testRobot, 80)
        Detection.stopOnLine(self.testRobot, self.testRobot.DRIVE_SPEED)
        Lift.clawGrab(self.testRobot, "release")
        Movement.forwardMovement(self.testRobot, 75)
        Movement.backwardMovement(self.testRobot, 300)
        Lift.clawGrab(self.testRobot, "pick")

        # Return to Red Zone (hard coded rn)
        Movement.turnOnSpot(self.testRobot, 160)
        Movement.forwardMovement(self.testRobot, 450)
        sleep(1)
        Detection.stopOnLine(self.testRobot, self.testRobot.DRIVE_SPEED)
        sleep(1)
        Movement.forwardMovement(self.testRobot, 100)
        Detection.lineFollowUntilLineIntersection(self.testRobot, 500, self.testRobot.DRIVE_SPEED)
        Movement.turnOnSpot(self.testRobot, -65)
        Movement.forwardMovement(self.testRobot, 250)

    def juniorSolution(self):
        Detection.stopOnLine(self.testRobot, 100)
        c = Detection.colorStore(self.testRobot)

        Movement.setSpeed(self.testRobot, 200)
        Movement.forwardMovement(self.testRobot, 100)
        Movement.turnOnSpot(self.testRobot, -90)
        Movement.forwardMovement(self.testRobot, 400)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Movement.PIDlineFollower(self.testRobot, 100, 200,"LEFT")
        Detection.lineFollowUntilIntersection(self.testRobot, 300, 200)

        Detection.panelPickup(self.testRobot, 10000, 100)
        Movement.forwardMovement(self.testRobot, 130)
        Movement.turnOnSpot(self.testRobot, -170)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Detection.lineFollowUntilIntersection(self.testRobot, 500, 100)
        Movement.dualSensorPIDlineFollower(self.testRobot, 1630, 200)

        Movement.turnOnSpot(self.testRobot, 90)
        Movement.forwardMovement(self.testRobot, 100)
        Lift.clawGrab(self.testRobot, "release")
        Movement.backwardMovement(self.testRobot, 100)
        Lift.clawGrab(self.testRobot, "pick")
        Movement.turnUntilLine(self.testRobot, "RIGHT")
        Movement.PIDlineFollower(self.testRobot, 150, 150,"RIGHT")
        Detection.lineFollowUntilIntersection(self.testRobot, 1670, 200)

        Movement.setSpeed(self.testRobot, 100)
        Detection.lineFollowerScanTreeAndPickup(self.testRobot, 10000, 100)
        Movement.setSpeed(self.testRobot, 200)
        Detection.treeDropOffSpotLocator(self.testRobot)
        Movement.forwardMovement(self.testRobot, 100)
        Movement.turnOnSpot(self.testRobot, -170)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Movement.dualSensorPIDlineFollower(self.testRobot, 200, 100)
        Detection.lineFollowUntilIntersection(self.testRobot, 1300, 100)
        treeDropOff(self.testRobot)

        Movement.setSpeed(self.testRobot, 100)
        Detection.lineFollowerScanTreeAndPickup(self.testRobot, 10000, 100)
        Movement.setSpeed(self.testRobot, 200)
        Detection.treeDropOffSpotLocator(self.testRobot)
        Movement.turnOnSpot(self.testRobot, -170)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Movement.dualSensorPIDlineFollower(self.testRobot, 270, 100)
        Detection.lineFollowUntilIntersection(self.testRobot, 1300, 100)
        treeDropOff(self.testRobot)

        Movement.dualSensorPIDlineFollower(self.testRobot, 660, 200)
        Movement.turnOnSpot(self.testRobot, 80)
        Movement.forwardMovement(self.testRobot, 350)

    def juniorSolution2016(self):
        Movement.turnOnSpot(self.testRobot, 80)

    def seniorSolution(self):
        ## Starting in green area
        Lift.initTwoPartClaw(self.testRobot)
        Lift.twoPartLift(self.testRobot, 500, 0.65, 0.0, 0)
        Movement.setSpeed(self.testRobot, 200)
        Movement.forwardMovement(self.testRobot, 200)
        Detection.lineFollowUntilIntersection(self.testRobot, 1000, 200)
        Movement.turnOnSpot(self.testRobot, 90)
        Detection.lineFollowUntilIntersection(self.testRobot, 1000, 200)
        Movement.forwardMovement(self.testRobot, 100)
        Movement.turnOnSpot(self.testRobot, 35)
        Movement.turnUntilLine(self.testRobot, "RIGHT")

        ## Starting on the first branch traversing through all the branches
        ## First create a turbine base array to store all the turbine bases collected
        ## Then create a technology decider array which corresponds to the turbine bases so we know which color turbine needs to be picked up

        turbineBaseArray = []
        technologyDeciderArray = []
        Movement.setSpeed(self.testRobot, 100)
        tBtD = Movement.branchTraversal(self.testRobot, 100)
        Movement.setSpeed(self.testRobot, 200)
        turbineBaseArray.append(tBtD[0])
        technologyDeciderArray.append(tBtD[1])
        Movement.turnOnSpot(self.testRobot, -120)
        Lift.twoPartLift(self.testRobot, 500, 0.35, 1, 0)
        Movement.forwardMovement(self.testRobot, 160)
        Lift.twoPartLift(self.testRobot, 500, 0.65, 0.0, 0)
        Movement.turnUntilLine(self.testRobot, "RIGHT")
        Movement.PIDlineFollower(self.testRobot, 150, 200, "LEFT")
        Movement.setSpeed(self.testRobot, 100)
        tBtD = Movement.branchTraversal(self.testRobot, 100)
        Movement.setSpeed(self.testRobot, 200)
        turbineBaseArray.append(tBtD[0])
        technologyDeciderArray.append(tBtD[1])
        Movement.turnOnSpot(self.testRobot, 130)
        Lift.twoPartLift(self.testRobot, 500, 0.35, 1, 0)
        Movement.forwardMovement(self.testRobot, 160)
        Lift.twoPartLift(self.testRobot, 500, 0.65, 0.0, 0)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Movement.PIDlineFollower(self.testRobot, 150, 200, "RIGHT")
        Movement.setSpeed(self.testRobot, 100)
        tBtD = Movement.branchTraversal(self.testRobot, 100)
        Movement.setSpeed(self.testRobot, 200)
        turbineBaseArray.append(tBtD[0])
        technologyDeciderArray.append(tBtD[1])
        Movement.turnOnSpot(self.testRobot, -130)
        Lift.twoPartLift(self.testRobot, 500, 0.35, 1, 0)
        Movement.forwardMovement(self.testRobot, 160)
        Lift.twoPartLift(self.testRobot, 500, 0.65, 0.0, 0)

        temp = turbineBaseArray[0]
        turbineBaseArray[0] = turbineBaseArray[2]
        turbineBaseArray[2] = temp

        temp = technologyDeciderArray[0]
        technologyDeciderArray[0] = technologyDeciderArray[2]
        technologyDeciderArray[2] = temp

        ## After robot finishes at 3rd branch
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Movement.dualSensorPIDlineFollower(self.testRobot, 300, 200)
        Detection.lineFollowUntilIntersection(self.testRobot, 1000, 200)
        Movement.forwardMovement(self.testRobot, 100)
        Movement.turnOnSpot(self.testRobot, 75)
        Movement.turnUntilLine(self.testRobot, "RIGHT")

        ## At first line of turbines
        Movement.setSpeed(self.testRobot, 100)
        updatedTechnologyDeciderArray = Detection.collectTurbinesOntoBase(self.testRobot, technologyDeciderArray, 100)
        Movement.setSpeed(self.testRobot, 200)

        ## Robot is now at the start of the first line of turbines facing North
        Movement.forwardMovement(self.testRobot, 100)
        Movement.turnOnSpot(self.testRobot, 45)
        Movement.turnUntilLine(self.testRobot, "RIGHT")
        Detection.lineFollowUntilIntersection(self.testRobot, 300, 100)
        Movement.forwardMovement(self.testRobot, 100)
        for each in updatedTechnologyDeciderArray:
            if each != None:
                Movement.turnOnSpot(self.testRobot, 75)
                Movement.turnUntilLine(self.testRobot, "RIGHT")
                Movement.setSpeed(self.testRobot, 100)
                Detection.collectTurbinesOntoBase(self.testRobot, updatedTechnologyDeciderArray, 100)
                Movement.setSpeed(self.testRobot, 200)
                Movement.forwardMovement(self.testRobot, 100)
                Movement.turnOnSpot(self.testRobot, -45)
                Movement.turnUntilLine(self.testRobot, "LEFT")
                Detection.lineFollowUntilIntersection(self.testRobot, 500, 200)
                Movement.dualSensorPIDlineFollower(self.testRobot, 300, 200)
                Movement.turnOnSpot(self.testRobot, 160)
                Movement.turnUntilLine(self.testRobot, "RIGHT")
                Movement.dualSensorPIDlineFollower(self.testRobot, 500, 200)
                break


        ##Last Portion of Senior Competition
        nodePath = Movement.findConstructionPath(self.testRobot, turbineBaseArray)
        Lift.twoPartLift(self.testRobot, 500, 0.65, 0, 0)
        basesLeft = 3
        beginningNode = Movement.startNodeFinder(self.testRobot, nodePath)
        if (beginningNode == 1):
            direction = "counterclockwise"
        if (beginningNode == 4):
            direction = "clockwise"
        direction = Movement.nodeTraversal(self.testRobot, beginningNode, nodePath[0], direction)
        Movement.setSpeed(self.testRobot, 100)
        Lift.nodeConstruction(self.testRobot, direction, turbineBaseArray[0], basesLeft)
        basesLeft = basesLeft - 1
        Movement.setSpeed(self.testRobot, 200)
        direction = Movement.nodeTraversal(self.testRobot, nodePath[0], nodePath[1], direction)
        Movement.setSpeed(self.testRobot, 100)
        Lift.nodeConstruction(self.testRobot, direction, turbineBaseArray[1], basesLeft)
        basesLeft = basesLeft - 1
        Movement.setSpeed(self.testRobot, 200)
        direction = Movement.nodeTraversal(self.testRobot, nodePath[1], nodePath[2], direction)
        Movement.setSpeed(self.testRobot, 100)
        Lift.nodeConstruction(self.testRobot, direction, turbineBaseArray[2], basesLeft)
        basesLeft = basesLeft - 1
        Movement.setSpeed(self.testRobot, 200)

        #Have Robot travel to the fourth node if it is not already there
        direction = Movement.nodeTraversal(self.testRobot, nodePath[2], 4, direction)

        #Drive back to green start area
        if(direction == "counterclockwise"):
            Movement.setSpeed(self.testRobot, 200)
            Movement.forwardMovement(self.testRobot, 300)
            Movement.turnOnSpot(self.testRobot, 45)
            Detection.lineFollowUntilIntersection(self.testRobot, 1000, 100)
            Movement.forwardMovement(self.testRobot, 130)
            Movement.turnOnSpot(self.testRobot, 70)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Detection.lineFollowUntilColorIntersection(self.testRobot, 1000, 100)
            Movement.forwardMovement(self.testRobot, 185)

        if(direction == "clockwise"):
            Movement.setSpeed(self.testRobot, 200)
            Movement.backwardMovement(self.testRobot, 150)
            Movement.turnOnSpot(self.testRobot, -135)
            Detection.lineFollowUntilIntersection(self.testRobot, 1000, 100)
            Movement.forwardMovement(self.testRobot, 130)
            Movement.turnOnSpot(self.testRobot, 70)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Detection.lineFollowUntilColorIntersection(self.testRobot, 1000, 100)
            Movement.forwardMovement(self.testRobot, 185)

    def treeDropOff(self):

        if(self.testRobot.currentRightDropOff == Color.WHITE and self.testRobot.currentLeftDropOff == Color.WHITE):
            #Complete
            Movement.dualSensorPIDlineFollower(self.testRobot, 690, 200)
            Movement.turnOnSpot(self.testRobot, -90)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 2)
            Movement.setSpeed(self.testRobot, 200)
            Movement.backwardMovement(self.testRobot, 80)
            Lift.clawGrab(self.testRobot, "pick")
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 70)
            Movement.turnUntilLine(self.testRobot, "LEFT")
            Movement.PIDlineFollower(self.testRobot, 100, 150, "LEFT")
            Detection.lineFollowUntilIntersection(self.testRobot, 1500, 200)
            self.testRobot.currentRightTree = None
            self.testRobot.currentRightDropOff = None
            self.testRobot.currentLeftTree = None
            self.testRobot.currentLeftDropOff = None

        if(self.testRobot.currentRightDropOff == Color.WHITE and self.testRobot.currentLeftDropOff == Color.RED):

            Movement.PIDlineFollower(self.testRobot, 550, 200, "RIGHT")
            Movement.turnOnSpot(self.testRobot, -120)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 1)
            Movement.setSpeed(self.testRobot, 200)
            self.testRobot.currentRightTree = None
            self.testRobot.currentRightDropOff = None

            Movement.backwardMovement(self.testRobot, 111)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Movement.PIDlineFollower(self.testRobot, 320, 200, "LEFT")
            Movement.turnOnSpot(self.testRobot, 90)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 2)
            Movement.setSpeed(self.testRobot, 200)
            self.testRobot.currentLeftTree = None
            self.testRobot.currentLeftDropOff = None

            #Returning
            Movement.backwardMovement(self.testRobot, 80)
            Lift.clawGrab(self.testRobot, "pick")
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 30)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Movement.PIDlineFollower(self.testRobot, 150, 200, "RIGHT")
            Detection.lineFollowUntilIntersection(self.testRobot, 1500, 200)

        if(self.testRobot.currentRightDropOff == Color.WHITE and self.testRobot.currentLeftDropOff == Color.BLUE):
            #Completed
            Movement.dualSensorPIDlineFollower(self.testRobot, 550, 200)
            Movement.turnOnSpot(self.testRobot, -90)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 1)
            Movement.setSpeed(self.testRobot, 200)
            self.testRobot.currentRightTree = None
            self.testRobot.currentRightDropOff = None

            Movement.backwardMovement(self.testRobot, 80)
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 50)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Movement.PIDlineFollower(self.testRobot, 250, 200, "RIGHT")
            Movement.dualSensorPIDlineFollower(self.testRobot, 450, 200)
            Movement.dualSensorPIDlineFollower(self.testRobot, 200, 200)
            Movement.turnOnSpot(self.testRobot, -90)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 2)
            Movement.setSpeed(self.testRobot, 200)
            self.testRobot.currentLeftTree = None
            self.testRobot.currentLeftDropOff = None

            #Returning
            Movement.backwardMovement(self.testRobot, 80)
            Lift.clawGrab(self.testRobot, "pick")
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 30)
            Movement.turnUntilLine(self.testRobot, "LEFT")
            Movement.PIDlineFollower(self.testRobot, 150, 200, "LEFT")
            Detection.lineFollowUntilIntersection(self.testRobot, 1500, 200)

        if(self.testRobot.currentRightDropOff == Color.RED and self.testRobot.currentLeftDropOff == Color.WHITE):

            Movement.PIDlineFollower(self.testRobot, 786, 200, "RIGHT")
            Movement.turnOnSpot(self.testRobot, 90)
            Movement.forwardMovement(self.testRobot, 80)
            Lift.treeDropOff(self.testRobot, 1)
            self.testRobot.currentRightTree = None
            self.testRobot.currentRightDropOff = None

            Movement.backwardMovement(self.testRobot, 111)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Movement.PIDlineFollower(self.testRobot, 200, 200, "RIGHT")
            Movement.turnOnSpot(self.testRobot, 90)
            Movement.forwardMovement(self.testRobot, 80)
            Lift.treeDropOff(self.testRobot, 2)
            self.testRobot.currentLeftTree = None
            self.testRobot.currentLeftDropOff = None

        if(self.testRobot.currentRightDropOff == Color.RED and self.testRobot.currentLeftDropOff == Color.RED):
            #Complete
            Movement.dualSensorPIDlineFollower(self.testRobot, 1000, 200)
            Movement.turnOnSpot(self.testRobot, 90)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 2)
            Movement.setSpeed(self.testRobot, 200)
            Movement.backwardMovement(self.testRobot, 80)
            Lift.clawGrab(self.testRobot, "pick")
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 70)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Movement.PIDlineFollower(self.testRobot, 100, 150, "RIGHT")
            Movement.dualSensorPIDlineFollower(self.testRobot, 500, 200)
            Detection.lineFollowUntilIntersection(self.testRobot, 1500, 200)


            self.testRobot.currentRightTree = None
            self.testRobot.currentRightDropOff = None
            self.testRobot.currentLeftTree = None
            self.testRobot.currentLeftDropOff = None


        if(self.testRobot.currentRightDropOff == Color.RED and self.testRobot.currentLeftDropOff == Color.BLUE):
            Movement.dualSensorPIDlineFollower(self.testRobot, 780, 200)
            Movement.turnOnSpot(self.testRobot, 90)
            Movement.forwardMovement(self.testRobot, 80)
            Lift.treeDropOff(self.testRobot, 1)
            self.testRobot.currentRightTree = None
            self.testRobot.currentRightDropOff = None

            Movement.backwardMovement(self.testRobot, 20)
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 30)
            Movement.turnUntilLine(self.testRobot, "LEFT")
            Movement.PIDlineFollower(self.testRobot, 320, 200, "LEFT")
            Movement.turnOnSpot(self.testRobot, -90)
            Movement.forwardMovement(self.testRobot, 80)
            Lift.treeDropOff(self.testRobot, 2)
            self.testRobot.currentLeftTree = None
            self.testRobot.currentLeftDropOff = None

            Movement.backwardMovement(self.testRobot, 20)
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 30)
            Movement.turnUntilLine(self.testRobot, "LEFT")
            Detection.lineFollowUntilIntersection(self.testRobot, 1500, 200)

        if(self.testRobot.currentRightDropOff == Color.BLUE and self.testRobot.currentLeftDropOff == Color.WHITE):
            #Completed
            Movement.dualSensorPIDlineFollower(self.testRobot, 1162, 200)
            Movement.turnOnSpot(self.testRobot, -90)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 1)
            Movement.setSpeed(self.testRobot, 200)
            self.testRobot.currentRightTree = None
            self.testRobot.currentRightDropOff = None

            Movement.backwardMovement(self.testRobot, 80)
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 50)
            Movement.turnUntilLine(self.testRobot, "LEFT")
            Movement.dualSensorPIDlineFollower(self.testRobot, 572, 200)
            Movement.turnOnSpot(self.testRobot, 90)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 2)
            Movement.setSpeed(self.testRobot, 200)
            self.testRobot.currentLeftTree = None
            self.testRobot.currentLeftDropOff = None

            #Returning
            Movement.backwardMovement(self.testRobot, 80)
            Lift.clawGrab(self.testRobot, "pick")
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 30)
            Movement.turnUntilLine(self.testRobot, "LEFT")
            Movement.PIDlineFollower(self.testRobot, 150, 200, "LEFT")
            Detection.lineFollowUntilIntersection(self.testRobot, 1500, 200)

        if(self.testRobot.currentRightDropOff == Color.BLUE and self.testRobot.currentLeftDropOff == Color.RED):
            #Completed
            Movement.dualSensorPIDlineFollower(self.testRobot, 1162, 200)
            Movement.turnOnSpot(self.testRobot, -90)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 1)
            Movement.setSpeed(self.testRobot, 200)
            self.testRobot.currentRightTree = None
            self.testRobot.currentRightDropOff = None

            Movement.backwardMovement(self.testRobot, 80)
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 50)
            Movement.turnUntilLine(self.testRobot, "LEFT")
            Movement.PIDlineFollower(self.testRobot, 286, 200, "LEFT")
            Movement.turnOnSpot(self.testRobot, -90)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 2)
            Movement.setSpeed(self.testRobot, 200)
            self.testRobot.currentLeftTree = None
            self.testRobot.currentLeftDropOff = None

            #Returning
            Movement.backwardMovement(self.testRobot, 80)
            Lift.clawGrab(self.testRobot, "pick")
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 30)
            Movement.turnUntilLine(self.testRobot, "RIGHT")
            Movement.PIDlineFollower(self.testRobot, 150, 200, "LEFT")
            Detection.lineFollowUntilIntersection(self.testRobot, 1500, 200)

        if(self.testRobot.currentRightDropOff == Color.BLUE and self.testRobot.currentLeftDropOff == Color.BLUE):
            #Complete
            Movement.dualSensorPIDlineFollower(self.testRobot, 1072, 200)
            Movement.turnOnSpot(self.testRobot, -90)
            Movement.forwardMovement(self.testRobot, 80)
            Movement.setSpeed(self.testRobot, 100)
            Lift.treeDropOff(self.testRobot, 2)
            Movement.setSpeed(self.testRobot, 200)
            Movement.backwardMovement(self.testRobot, 80)
            Lift.clawGrab(self.testRobot, "pick")
            Detection.driveUntilLine(self.testRobot, -150)
            Movement.forwardMovement(self.testRobot, 70)
            Movement.turnUntilLine(self.testRobot, "LEFT")
            Movement.PIDlineFollower(self.testRobot, 100, 150, "LEFT")
            Detection.lineFollowUntilIntersection(self.testRobot, 1500, 200)
            self.testRobot.currentRightTree = None
            self.testRobot.currentRightDropOff = None
            self.testRobot.currentLeftTree = None
            self.testRobot.currentLeftDropOff = None

    def seniorSolution2016(self):
        # Initialize and get to first container
        Lift.seniorClaw2016(self.testRobot, "init")
        Movement.setSpeed(robot = self.testRobot, speed = 150)
        Detection.stopOnLine(robot = self.testRobot, speed = self.testRobot.DRIVE_SPEED)
        Movement.forwardMovement(self.testRobot, 100)
        Movement.turnUntilLine(self.testRobot, "LEFT")
        Movement.turnOnSpot(self.testRobot, 10)
        Detection.lineFollowUntilTurn(self.testRobot, 300, self.testRobot.DRIVE_SPEED, "right")
        # First Container
        Movement.turnOnSpot(self.testRobot, -100)
        Lift.seniorClaw2016(self.testRobot, "open")
        Movement.backwardMovement(self.testRobot, 95)
        Lift.seniorClaw2016(self.testRobot, "lift")
        # check block color and correct if nessesary
        wait(1000)
        # currentContainerColor = Color.RED # Hardcoded due to messed up order
        currentRGB = Detection.getBlockReflection2016(self.testRobot, "container")
        currentContainerColor = Detection.detectBlockReflection2016(self.testRobot, "container")
        print(currentRGB)
        print(currentContainerColor)
        if (currentContainerColor == Color.GREEN):
            Lift.seniorClaw2016(self.testRobot, "drop")
            Lift.seniorClaw2016(self.testRobot, "open")
            sleep(1)
            Movement.forwardMovement(self.testRobot, 90)
            Lift.seniorClaw2016(self.testRobot, "close")
            sleep(1)
            Movement.nodeTraversal2016(self.testRobot, Color.GREEN, Color.RED)
        else:
            carryingBlock = 1
            Movement.forwardMovement(self.testRobot, 90)
            sleep(1)
            print("stop me")
            wait(10000)
            Movement.nodeTraversal2016(self.testRobot, Color.GREEN, currentContainerColor)
        # Second Container
        Lift.seniorClaw2016(self.testRobot, "drop")
        Lift.seniorClaw2016(self.testRobot, "open")
        Movement.backwardMovement(self.testRobot, 90)
        Lift.seniorClaw2016(self.testRobot, "lift")
        if (carryingBlock == 1):
            Movement.backwardMovement(self.testRobot, 80)
            Movement.forwardMovement(self.testRobot, 80)
        # check block color and correct if nessesary
        wait(1000)
        prevContainerColor = currentContainerColor
        currentRGB = Detection.getBlockReflection2016(self.testRobot, "container")
        currentContainerColor = Detection.detectBlockReflection2016(self.testRobot, "container")
        print(currentRGB)
        print(currentContainerColor)
        if (currentContainerColor == prevContainerColor):
            Lift.seniorClaw2016(self.testRobot, "drop")
            Lift.seniorClaw2016(self.testRobot, "open")
            sleep(1)
            Movement.forwardMovement(self.testRobot, 90)
            Lift.seniorClaw2016(self.testRobot, "close")
            sleep(1)
            Movement.nodeTraversal2016(self.testRobot, Color.RED, Color.BLUE)
        else:
            carryingBlock = 1
            Movement.forwardMovement(self.testRobot, 90)
            sleep(1)
            Movement.nodeTraversal2016(self.testRobot, prevContainerColor, currentContainerColor)
        # Third Container
        # Movement.turnOnSpot(self.testRobot, 10) # THIS IS TO ADJUST FOR TRAVERSAL FROM YELLOW TO BLUE, nodeTraversal may need to be adjusted
        Movement.forwardMovement(self.testRobot, 10) # SAME AS ABOVE
        Lift.seniorClaw2016(self.testRobot, "drop")
        Lift.seniorClaw2016(self.testRobot, "open")
        Movement.backwardMovement(self.testRobot, 90)
        Lift.seniorClaw2016(self.testRobot, "lift")
        if (carryingBlock == 1):
            Movement.backwardMovement(self.testRobot, 80)
            Movement.forwardMovement(self.testRobot, 80)
        # check block color and correct if nessesary
        wait(1000)
        prevContainerColor = currentContainerColor
        currentContainerColor = Detection.detectBlockReflection2016(self.testRobot, "container")
        currentRGB = Detection.getBlockReflection2016(self.testRobot, "container")
        currentContainerColor = Detection.detectBlockReflection2016(self.testRobot, "container")
        print(currentRGB)
        print(currentContainerColor)
        if (currentContainerColor == prevContainerColor):
            Lift.seniorClaw2016(self.testRobot, "drop")
            Lift.seniorClaw2016(self.testRobot, "open")
            sleep(1)
            Movement.forwardMovement(self.testRobot, 140)
            Lift.seniorClaw2016(self.testRobot, "close")
            sleep(1)
            Movement.nodeTraversal2016(self.testRobot, Color.RED, Color.BLUE)
        else:
            carryingBlock = 1
            Movement.forwardMovement(self.testRobot, 140)
            sleep(1)
            Movement.nodeTraversal2016(self.testRobot, prevContainerColor, currentContainerColor)
        # Fourth Container
        Movement.turnOnSpot(self.testRobot, -10) # THIS IS TO ADJUST FOR TRAVERSAL FROM BLUE TO RED, nodeTraversal may need to be adjusted
        Movement.forwardMovement(self.testRobot, 15) # SAME AS ABOVE
        Lift.seniorClaw2016(self.testRobot, "drop")
        Lift.seniorClaw2016(self.testRobot, "open")
        Movement.backwardMovement(self.testRobot, 90)
        Lift.seniorClaw2016(self.testRobot, "lift")
        if (carryingBlock == 1):
            Movement.backwardMovement(self.testRobot, 80)
            Movement.forwardMovement(self.testRobot, 80)
        # check block color and correct if nessesary
        wait(1000)
        prevContainerColor = currentContainerColor
        currentRGB = Detection.getBlockReflection2016(self.testRobot, "container")
        currentContainerColor = Detection.detectBlockReflection2016(self.testRobot, "container")
        print(currentRGB)
        print(currentContainerColor)
        currentContainerColor = Detection.detectBlockReflection2016(self.testRobot, "container")
        if (currentContainerColor == prevContainerColor):
            Lift.seniorClaw2016(self.testRobot, "drop")
            Lift.seniorClaw2016(self.testRobot, "open")
            sleep(1)
            Movement.forwardMovement(self.testRobot, 90)
            Lift.seniorClaw2016(self.testRobot, "close")
            Movement.nodeTraversal2016(self.testRobot, Color.RED, Color.BLUE)
        else:
            carryingBlock = 1
            Movement.forwardMovement(self.testRobot, 90)
            Movement.nodeTraversal2016(self.testRobot, prevContainerColor, currentContainerColor)