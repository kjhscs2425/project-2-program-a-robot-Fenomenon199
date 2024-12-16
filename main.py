# Import the robot control commands from the library
from simulator import robot
import time

left, right = robot.sonars()
spin = input("Do you want to spin right or left? ")
seconds= float( input("How many seconds would you run for? "))
if spin == "right":
    robot.motors(-1, 1, seconds)
elif spin == "left":
    robot.motors(1, -1, seconds)


go = input("Do you want to go forward or backward? ")
seconds= float( input("How many seconds would you run for? "))
if go== "forward":
   robot.motors(1, 1, seconds)
elif go==  "backward": 
    robot.motors(-1, -1, seconds)

robot.exit()