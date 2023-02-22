 # * MotorBridge.py
 # * This is a library for BBG/BBB motor bridge cape
 # * Copyright (c) 2015 seeed technology inc.
 # * Author      : Jiankai Li
 # * Create Time:  Nov 2015
 # * Change Log : Jan. 2023 by Seth w/ help from #beagle on IRC and vsx-examples for gpiod in python3...
 # *
 # * The MIT License (MIT)
 # *
 # * Permission is hereby granted, free of charge, to any person obtaining a copy
 # * of this software and associated documentation files (the "Software"), to deal
 # * in the Software without restriction, including without limitation the rights
 # * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # * copies of the Software, and to permit persons to whom the Software is
 # * furnished to do so, subject to the following conditions:
 # *
 # * The above copyright notice and this permission notice shall be included in
 # * all copies or substantial portions of the Software.
 # *
 # * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # * THE SOFTWARE.
 # */
# FileName : MotorBridge.py
# by Jiankai.li

from smbus2 import SMBus
from time import sleep
#import pathlib
import gpiod

CHIP = 'gpiochip1'
LINE_OFFSET = [17]

chip = gpiod.Chip(CHIP)

lines = chip.get_lines(LINE_OFFSET)
lines.request(consumer=' ', type=gpiod.LINE_REQ_DIR_OUT)

lines.set_values([0])

bus = SMBus('/dev/i2c-2')

ReadMode  = 0
WriteMode = 1
DeAddr    = 0X4B
ConfigValid =  0x3a6fb67c
DelayTime = 0.005

# TB_WORKMODE

TB_SHORT_BREAK  = 0
TB_CW           = 1
TB_CCW          = 2
TB_STOP         = 3
TB_WORKMODE_NUM = 4


# TB_PORTMODE

TB_DCM          = 0
TB_SPM          = 1
TB_PORTMODE_NUM = 2


# SVM_PORT

SVM1            = 0
SVM2            = 1
SVM3            = 2
SVM4            = 3
SVM5            = 4
SVM6            = 5
SVM_PORT_NUM    = 6

# SVM_STATE

SVM_DISABLE     = 0
SVM_ENABLE      = 1
SVM_STATE_NUM   = 2

# IO_MODE

IO_IN           = 0
IO_OUT          = 1
IO_MODE_NUM     = 2

# IO_PUPD

IO_PU           = 0
IO_PD           = 1
IO_NP           = 2
IO_PUPD_NUM     = 3

# IO_PPOD

IO_PP           = 0
IO_OD           = 1
IO_PPOD_NUM     = 2

# IO_STATE

IO_LOW          = 0
IO_HIGH         = 1
IO_STATE_NUM    = 2

# IO_PORT

IO1             = 0
IO2             = 1
IO3             = 2
IO4             = 3
IO5             = 4
IO6             = 5
IO_NUM          = 6


# PARAM_REG

CONFIG_VALID        = 0
CONFIG_TB_PWM_FREQ  = CONFIG_VALID + 4

I2C_ADDRESS         = CONFIG_TB_PWM_FREQ + 4

TB_1A_MODE          = I2C_ADDRESS + 1
TB_1A_DIR           = TB_1A_MODE + 1
TB_1A_DUTY          = TB_1A_DIR + 1
TB_1A_SPM_SPEED     = TB_1A_DUTY + 2
TB_1A_SPM_STEP      = TB_1A_SPM_SPEED + 4

TB_1B_MODE          = TB_1A_SPM_STEP + 4
TB_1B_DIR           = TB_1B_MODE + 1
TB_1B_DUTY          = TB_1B_DIR + 1
TB_1B_SPM_SPEED     = TB_1B_DUTY + 2
TB_1B_SPM_STEP      = TB_1B_SPM_SPEED + 4

TB_2A_MODE          = TB_1B_SPM_STEP + 4
TB_2A_DIR           = TB_2A_MODE + 1
TB_2A_DUTY          = TB_2A_DIR + 1
TB_2A_SPM_SPEED     = TB_2A_DUTY + 2
TB_2A_SPM_STEP      = TB_2A_SPM_SPEED + 4

TB_2B_MODE          = TB_2A_SPM_STEP + 4
TB_2B_DIR           = TB_2B_MODE + 1
TB_2B_DUTY          = TB_2B_DIR + 1
TB_2B_SPM_SPEED     = TB_2B_DUTY + 2
TB_2B_SPM_STEP      = TB_2B_SPM_SPEED + 4

SVM1_STATE          = TB_2B_SPM_STEP + 4
SVM1_FREQ           = SVM1_STATE + 1
SVM1_ANGLE          = SVM1_FREQ + 2

SVM2_STATE          = SVM1_ANGLE + 2
SVM2_FREQ           = SVM2_STATE + 1
SVM2_ANGLE          = SVM2_FREQ + 2

SVM3_STATE          = SVM2_ANGLE + 2
SVM3_FREQ           = SVM3_STATE + 1
SVM3_ANGLE          = SVM3_FREQ + 2

SVM4_STATE          = SVM3_ANGLE + 2
SVM4_FREQ           = SVM4_STATE + 1
SVM4_ANGLE          = SVM4_FREQ + 2

SVM5_STATE          = SVM4_ANGLE + 2
SVM5_FREQ           = SVM5_STATE + 1
SVM5_ANGLE          = SVM5_FREQ + 2

SVM6_STATE          = SVM5_ANGLE + 2
SVM6_FREQ           = SVM6_STATE + 1
SVM6_ANGLE          = SVM6_FREQ + 2

IO1_STATE           = SVM6_ANGLE + 2
IO1_MODE            = IO1_STATE + 1
IO1_PUPD            = IO1_MODE + 1
IO1_PPOD            = IO1_PUPD + 1

IO2_STATE           = IO1_PPOD + 1
IO2_MODE            = IO2_STATE + 1
IO2_PUPD            = IO2_MODE + 1
IO2_PPOD            = IO2_PUPD + 1

IO3_STATE           = IO2_PPOD + 1
IO3_MODE            = IO3_STATE + 1
IO3_PUPD            = IO3_MODE + 1
IO3_PPOD            = IO3_PUPD + 1

IO4_STATE           = IO3_PPOD + 1
IO4_MODE            = IO4_STATE + 1
IO4_PUPD            = IO4_MODE + 1
IO4_PPOD            = IO4_PUPD + 1

IO5_STATE           = IO4_PPOD + 1
IO5_MODE            = IO5_STATE + 1
IO5_PUPD            = IO5_MODE + 1
IO5_PPOD            = IO5_PUPD + 1

IO6_STATE           = IO5_PPOD + 1
IO6_MODE            = IO6_STATE + 1
IO6_PUPD            = IO6_MODE + 1
IO6_PPOD            = IO6_PUPD + 1

PARAM_REG_NUM = IO6_PPOD + 1

def WriteByte(Reg,Value):
    data = [0 for i in range(2)]
    data[0] = Reg
    data[1] = Value
    bus.write_i2c_block_data(0x4b, 1, data)

def WriteHalfWord(Reg,Value):
    data = [0 for i in range(3)]
    data[0] = Reg
    data[1] = Value & 0xff
    data[2] = (Value>>8) & 0xff
    bus.write_i2c_block_data(0x4b, 1, data)

def WriteOneWord(Reg,Value):
    data = [0 for i in range(5)]
    data[0] = Reg
    data[1] = Value & 0xff
    data[2] = (Value>>8) & 0xff
    data[3] = (Value>>16) & 0xff
    data[4] = (Value>>24) & 0xff
    bus.write_i2c_block_data(0x4b, 1, data)

def SetDefault():
    WriteOneWord(CONFIG_VALID, 0x00000000)

class MotorBridgeCape:
    def __init__(self):
        lines.set_values([1])
        sleep(1)

    # init stepper motor A
    def StepperMotorAInit(self):
        WriteByte(TB_1A_MODE, TB_SPM) #Stepper
        sleep(DelayTime)
        WriteHalfWord(TB_1A_DUTY, 1000)    # voltage
        sleep(DelayTime)

    # MoveSteps > 0 CW
    # MoveSteps < 0 CCW
    # StepDelayTime : delay time for every step. uint us
    def StepperMotorAMove(self, MoveSteps, StepDelayTime):
        if MoveSteps > 0:
            WriteByte(TB_1A_DIR, TB_CW)   #CW
        else:
            WriteByte(TB_1A_DIR, TB_CCW)   #CW
            MoveSteps = -MoveSteps
        sleep(DelayTime)
        WriteOneWord(TB_1A_SPM_SPEED, StepDelayTime)  # unit us
        sleep(DelayTime)
        WriteOneWord(TB_1A_SPM_STEP, MoveSteps)
        sleep(DelayTime)

    # init stepper motor B
    def StepperMotorBInit(self):
        WriteByte(TB_2A_MODE, TB_SPM) #Stepper
        sleep(DelayTime)
        WriteHalfWord(TB_2A_DUTY, 1000)    # voltage
        sleep(DelayTime)

    # MoveSteps > 0 CW
    # MoveSteps < 0 CCW
    # StepDelayTime : delay time for every step. uint us
    def StepperMotorBMove(self, MoveSteps, StepDelayTime):
        if MoveSteps > 0:
            WriteByte(TB_2A_DIR, TB_CW)   #CW
        else:
            WriteByte(TB_2A_DIR, TB_CCW)   #CW
            MoveSteps = -MoveSteps
        sleep(DelayTime)
        WriteOneWord(TB_2A_SPM_SPEED, StepDelayTime)  # unit us
        sleep(DelayTime)
        WriteOneWord(TB_2A_SPM_STEP, MoveSteps)
        sleep(DelayTime)

    # Init DC Motor
    def DCMotorInit(self,MotorName, Frequency):
    # Init the DC Frequency
        WriteOneWord(CONFIG_TB_PWM_FREQ, Frequency)
        sleep(DelayTime)

    # Set the port as DC Motor
        if MotorName == 1 or MotorName == 2:
            WriteByte(TB_1A_MODE, TB_DCM)
            sleep(DelayTime)
            WriteByte(TB_1A_DIR, TB_STOP)
            sleep(DelayTime)
            WriteByte(TB_1B_MODE, TB_DCM)
            sleep(DelayTime)
            WriteByte(TB_1B_DIR, TB_STOP)
            sleep(DelayTime)
        if MotorName == 3 or MotorName == 4:
            WriteByte(TB_2A_MODE, TB_DCM)
            sleep(DelayTime)
            WriteByte(TB_2A_DIR, TB_STOP)
            sleep(DelayTime)
            WriteByte(TB_2B_MODE, TB_DCM)
            sleep(DelayTime)
            WriteByte(TB_2B_DIR, TB_STOP)
            sleep(DelayTime)

    # Drive the DC Motor
    # Direction 1 CW | 2 CCW
    # PWNDuty  0 ~ 100
    def DCMotorMove(self, MotorName, Direction, PWMDuty):
        if MotorName == 1:
            WriteByte(TB_1B_DIR, Direction)
            sleep(DelayTime)
            WriteOneWord(TB_1B_DUTY, PWMDuty*10)
            sleep(DelayTime)

        if MotorName == 2:
            WriteByte(TB_1A_DIR, Direction)
            sleep(DelayTime)
            WriteOneWord(TB_1A_DUTY, PWMDuty*10)
            sleep(DelayTime)

        if MotorName == 3:
            WriteByte(TB_2B_DIR, Direction)
            sleep(DelayTime)
            WriteOneWord(TB_2B_DUTY, PWMDuty*10)
            sleep(DelayTime)

        if MotorName == 4:
            WriteByte(TB_2A_DIR, Direction)
            sleep(DelayTime)
            WriteOneWord(TB_2A_DUTY, PWMDuty*10)
            sleep(DelayTime)

    # Stop the DC motor
    def DCMotorStop(self, MotorName):
        if MotorName == 1:
            WriteByte(TB_1B_DIR, TB_STOP)
        if MotorName == 2:
            WriteByte(TB_1A_DIR, TB_STOP)
        if MotorName == 3:
            WriteByte(TB_2B_DIR, TB_STOP)
        if MotorName == 4:
            WriteByte(TB_2A_DIR, TB_STOP)
        sleep(DelayTime)

    # init the Servo
    def ServoInit(self, ServoName, Frequency):
        if ServoName == 1:
            WriteHalfWord(SVM1_FREQ, Frequency)
            sleep(DelayTime)
            WriteByte(SVM1_STATE, SVM_ENABLE)
            sleep(DelayTime)

        if ServoName == 2:
            WriteHalfWord(SVM2_FREQ, Frequency)
            sleep(DelayTime)
            WriteByte(SVM2_STATE, SVM_ENABLE)
            sleep(DelayTime)
        if ServoName == 3:
            WriteHalfWord(SVM3_FREQ, Frequency)
            sleep(DelayTime)
            WriteByte(SVM3_STATE, SVM_ENABLE)
            sleep(DelayTime)

        if ServoName == 4:
            WriteHalfWord(SVM4_FREQ, Frequency)
            sleep(DelayTime)
            WriteByte(SVM4_STATE, SVM_ENABLE)
            sleep(DelayTime)
        if ServoName == 5:
            WriteHalfWord(SVM5_FREQ, Frequency)
            sleep(DelayTime)
            WriteByte(SVM5_STATE, SVM_ENABLE)
            sleep(DelayTime)

        if ServoName == 6:
            WriteHalfWord(SVM6_FREQ, Frequency)
            sleep(DelayTime)
            WriteByte(SVM6_STATE, SVM_ENABLE)
            sleep(DelayTime)

    def ServoMoveAngle(self, ServoName, Angle):
        if ServoName == 1:
            WriteHalfWord(SVM1_ANGLE, Angle)
            sleep(DelayTime)

        if ServoName == 2:
            WriteHalfWord(SVM2_ANGLE, Angle)
            sleep(DelayTime)

        if ServoName == 3:
            WriteHalfWord(SVM3_ANGLE, Angle)
            sleep(DelayTime)

        if ServoName == 4:
            WriteHalfWord(SVM4_ANGLE, Angle)
            sleep(DelayTime)

        if ServoName == 5:
            WriteHalfWord(SVM5_ANGLE, Angle)
            sleep(DelayTime)

        if ServoName == 6:
            WriteHalfWord(SVM6_ANGLE, Angle)
            sleep(DelayTime)

#def myloop():

    #time.sleep(1)
    #motor.StepperMotorBMove(-1000,1000) # 20 steppers  1000us every step
    #time.sleep(1)
    #motor.StepperMotorBMove(1000,1000)  # 20 steppers  1000us every step

if __name__=="__main__":
    print("Hello!")

    #motor = MotorBridgeCape()
    #motor.StepperMotorBInit()
    #motor.StepperMotorBMove(1000,1000) # 20 steppers  1000us every step
    #myloop()

