#!/usr/bin/python3

import MotorBridge
from time import sleep

# stepper motor stuff...enjoy!

motor = MotorBridge.MotorBridgeCape()
motor.StepperMotorAInit()

class morph:
    def StepperMotorATest():
        arch = int(input("Please type your favorite number! "))
        if arch == 0:
            sleep(2)
        elif arch <= 24:
            motor.StepperMotorAMove(2500, 1000)
            sleep(3)
            motor.StepperMotorAMove(-2500, 1000)
            sleep(3)
        elif arch >= 26:
            motor.StepperMotorAMove(7500, 1000)
            sleep(10)
            motor.StepperMotorAMove(-7500, 1000)
            sleep(10)
        elif arch == 76:
            motor.StepperMotorAMove(1000, 1000)
            sleep(2)
            motor.StepperMotorAMove(-1000, 1000)
            sleep(2)
        elif arch == 1000:
            sleep(4)
            print("Congrats on being you!", arch)
        else:
            print("I like baba boom!")

if __name__=="__main__":
    try:
        while True:
            morph.StepperMotorATest()
    except KeyboardInterrupt:
        print("You have ended your entering of favorite numbers... ")
