from wpilib import *
from wpilib.command import *
from commandbased import *
from robot import *

class DriveTime(Command):

    def __init__(self, power, time):
        super().__init__('Drive Time')
        self.startTime = Timer.getFPGATimestamp()
        self.power = power
        self.time = time

    def initialize(self):
        pass

    def execute(self):
        Robot.drive.setPower(self.power)

    def isFinished(self):
        return (Timer.getFPGATimestamp() - self.startTime) > self.time

    def end(self):
        Robot.drive.setPower(0)
