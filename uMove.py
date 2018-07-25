import MotorBridge
import time

MotorName        = 1
MotorName        = 2
ClockWise        = 1
CounterClockWise = 2
PwmDuty          = 90
Frequency        = 1000

if __name__=="__main__":
    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 51):
        motor.DCMotorMove(1, 1, 90)
        motor.DCMotorMove(2, 1, 90)
        print "I got your biscuit, now!"

#Making a U-Shape in the lawn
#Left motor on chassis goes while the right motor ccw
    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 3):
        motor.DCMotorMove(1, 1, 90)
        motor.DCMotorMove(2, 2, 90)
        print "I love Jim's TURN!"

#All Flanks...Straight Ahead!        
    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 51):
        motor.DCMotorMove(1, 1, 90)
        motor.DCMotorMove(2, 1, 90)
        print "Give in to temptation!"
        
#Make another U-Turn but this time, motors go in the opposite direction!
    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 3):
        motor.DCMotorMove(1, 2, 90)
        motor.DCMotorMove(2, 1, 90)
        
#Straight Ahead
    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 51):
        motor.DCMotorMove(1, 1, 90)
        motor.DCMotorMove(2, 1, 90)
        print "Tacos are not all around here!"
        
    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 3):
        motor.DCMotorMove(1, 1, 90)
        motor.DCMotorMove(2, 2, 90)
    
    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 51):
        motor.DCMotorMove(1, 1, 90)
        motor.DCMotorMove(2, 1, 90)    
    
    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 3):
        motor.DCMotorMove(1, 2, 90)
        motor.DCMotorMove(2, 1, 90)
    
    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 51):
        motor.DCMotorMove(1, 1, 90)
        motor.DCMotorMove(2, 1, 90)

    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 3):
        motor.DCMotorMove(1, 1, 90)
        motor.DCMotorMove(2, 2, 90)

    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 51):
        motor.DCMotorMove(1, 1, 90)
        motor.DCMotorMove(2, 1, 90)        

    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 3):
        motor.DCMotorMove(1, 2, 90)
        motor.DCMotorMove(2, 1, 90)
        
    motor = MotorBridge.MotorBridgeCape()
    motor.DCMotorInit(1, 1000)
    motor.DCMotorInit(2, 1000)
    for i in range(1, 51):
        motor.DCMotorMove(1, 1, 90)
        motor.DCMotorMove(2, 1, 90)
        print "Major Malfunction!"
        print "Minor Infraction!"
