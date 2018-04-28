import wpilib
from wpilib.command import Command, Scheduler
from commandbased import *
from subsystems import drive
from commands import driveTime


class Robot(CommandBasedRobot):

    drive = drive.Drive()

    def robotInit(self):
        pass

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        autoCommand = driveTime.DriveTime(-1, 5)
        autoCommand.start()

    def autonomousPeriodic(self):
        Scheduler.getInstance().run()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        Scheduler.getInstance().run()

    def testInit(self):
        pass

    def testPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(Robot, physics_enabled=True)

