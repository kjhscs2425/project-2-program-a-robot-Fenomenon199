# Import the robot control commands from the library
from simulator import robot
import time

spin = input("Do you want to spin right or left? ")
seconds= float( input("How many seconds would you run for? "))
if spin == "right":
    robot.motors(-1, 1, seconds)
elif spin == "left":
    robot.motors(1, -1, seconds)


go = input("Do you want to go forward or backward? ")
seconds= float( input("How many seconds would you run for? "))
if go== "forward":
    while True:
        left, right = robot.sonars()
        robot.motors(1, 1, 0.01)
        print(left, right)
        if left < 75 or right < 75:
            break
elif go==  "backward": 
    while True:
        left, right = robot.sonars()    
        robot.motors(-1, -1, 0.1)
        if left > 375 or right > 375:
            break