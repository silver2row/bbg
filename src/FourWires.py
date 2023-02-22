#!/usr/bin/python3

import MotorBridge
from time import sleep

motor = MotorBridge.MotorBridgeCape()
motor.StepperMotorAInit()

def StepperMotorATest():
    motor.StepperMotorAMove(1000, 1000) # 1000 steppers  1000us every step
    sleep(5)
    motor.StepperMotorAMove(-1000, 1000) #1000 steppers  1000us every step
    sleep(5)
