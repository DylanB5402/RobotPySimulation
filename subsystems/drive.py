import wpilib
from ctre import *
from wpilib.command.subsystem import Subsystem
from robotpy_ext.common_drivers import navx

class Drive(Subsystem):

    def __init__(self):
        super().__init__('Drive')
        self.left_motor = TalonSRX(0)
        self.right_motor = TalonSRX(1)
        self.navX = navx.AHRS.create_spi()

        self.left_motor.setInverted(True)
        self.left_motor.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Absolute)
        self.left_motor.setSensorPhase(True)

        self.right_motor.setInverted(False)
        self.right_motor.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Absolute)
        self.right_motor.setSensorPhase(False)

    def setPower(self, power):
        self.right_motor.set(ControlMode.PercentOutput, power)
        self.left_motor.set(ControlMode.PercentOutput, power)

    def getRightPosition(self):
        return self.left_motor.getSelectedSensorPosition()

    def getRightPosition(self):
        return self.right_motor.getSelectedSensorPosition()

    def getYaw(self):
        return self.navX.getYaw()

