# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       bentdm197                                                    #
# 	Created:      12/16/2024, 12:51:35 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()
controller_1 = Controller()

#---------------------------#
#   green motor - 18 : 01   #
#   red motor   - 36 : 01   #
#   blue motor  - 06 : 01   #
#                           #
#   90 = 18 DEGREES         #
# --------------------------#  

#-----------#
# pin > 70% #
#-----------#

#Setup motor robot
left_motor_1 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
left_motor_2 = Motor(Ports.PORT17, GearSetting.RATIO_18_1, True)
right_motor_1 = Motor(Ports.PORT15, GearSetting.RATIO_18_1, False)
right_motor_2 = Motor(Ports.PORT16, GearSetting.RATIO_18_1, False)

intake_motor = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
elevator_motor = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
mobile_goal_motor = Motor(Ports.PORT12, GearSetting.RATIO_36_1, True)
arm_motor = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)
wall_stake_motor_1 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
wall_stake_motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)

left_drive_smart_stopped = 0
right_drive_smart_stopped = 0
left_drive_smart_speed = 0
right_drive_smart_speed = 0

# group motor
group_left = MotorGroup(left_motor_1, left_motor_2)
group_right = MotorGroup(right_motor_1, right_motor_2)  
wall_stake_motor = MotorGroup(wall_stake_motor_1, wall_stake_motor_2)
  
# drive train
robot = DriveTrain(group_left, group_right, wheelTravel = 260, wheelBase = 340, trackWidth = 100, units = MM)

# Set velocity & torque
group_right.set_velocity(60, PERCENT)
group_left.set_velocity(60, PERCENT)

robot.set_turn_velocity(60, PERCENT)

elevator_motor.set_velocity(70, PERCENT)
elevator_motor.set_max_torque(100, PERCENT)

arm_motor.set_velocity(100, PERCENT)
wall_stake_motor.set_velocity(100, PERCENT)

intake_motor.set_max_torque(60, PERCENT)
intake_motor.set_velocity(100, PERCENT)

mobile_goal_motor.set_max_torque(100, PERCENT)
mobile_goal_motor.set_velocity(100, PERCENT)

# wait for rotation sensor to fully initialize
# wait(30, MSEC)

# def pre_autonomous():

def autonomous():
    # left side
    elevator_motor.spin_for(FORWARD, 670, MSEC)

    # go to take mobile goal
    robot.drive_for(FORWARD, 250, MM)
    # robot.drive_for(FORWARD, 250, MM)


    robot.turn_for(RIGHT, 19, DEGREES)

    # take mobile goal
    group_left.set_velocity(40, PERCENT)
    group_right.set_velocity(40, PERCENT)
    mobile_goal_motor.spin(FORWARD, 100, PERCENT)
    robot.drive_for(REVERSE, 490, MM)
    mobile_goal_motor.spin(REVERSE)
    mobile_goal_motor.set_stopping(HOLD)
    group_left.set_velocity(60, PERCENT)
    group_right.set_velocity(60, PERCENT)
    wait(400, MSEC)

    # take 1st ring
    robot.turn_for(LEFT, 15.5, DEGREES)

    intake_motor.spin(FORWARD)
    elevator_motor.spin(FORWARD, 70, PERCENT)
    robot.drive_for(FORWARD, 510, MM,60, PERCENT)
    wait(400, MSEC)

    # go to 2nd ring in front of wall stake 
    robot.turn_for(LEFT, 8.5, DEGREES)
    wait(100, MSEC)
    robot.drive_for(FORWARD, 540, MM, 60, PERCENT)
    wait(100, MSEC)
    group_right.spin_for(FORWARD, 320, DEGREES)

    wait(500, MSEC)

    robot.drive(FORWARD)
    wait(900, MSEC)
    robot.drive_for(REVERSE, 310, MM)
    wait(200, MSEC)
    #take the other 3 rings
    robot.turn_for(LEFT, 15, DEGREES, 60, PERCENT)
    robot.drive_for(FORWARD, 950, MM, 60, PERCENT)
    wait(600, MSEC)

    robot.drive_for(FORWARD, 270, MM, 60, PERCENT)
    wait(200, MSEC)

    robot.drive_for(REVERSE, 100, MM, 50, PERCENT)
    wait(500, MSEC)

    #######2 SCENARIOS (group right or turn right)
    #1 METHOD
    group_right.spin_for(REVERSE, 580, DEGREES)

    wait(100, MSEC)
    robot.drive(FORWARD)
    wait(1400, MSEC)

    robot.drive_for(REVERSE, 150, MM, 50, PERCENT)
    wait(500, MSEC)
    robot.turn_for(RIGHT, 22, DEGREES)
    mobile_goal_motor.set_stopping(COAST)
    mobile_goal_motor.spin_for(FORWARD, 1000, MSEC) 
    wait(300, MSEC)
    robot.drive_for(FORWARD, 100, MM, 60, PERCENT)

    robot.drive(REVERSE)  
    wait(900, MSEC)

    robot.drive_for(FORWARD, 200, MM, 70, PERCENT)
    robot.turn_for(RIGHT, 17, DEGREES)
    wait(100, MSEC)
    robot.drive(REVERSE)
    wait(700, MSEC)
    robot.drive_for(FORWARD, 1430, MM, 50, PERCENT)
    ####RECALIBRATE WITH WALL
    robot.turn_for(LEFT, 19, DEGREES)
    robot.drive(REVERSE, 50, PERCENT)
    wait(1100, MSEC)
    robot.drive_for(FORWARD, 320, MM, 50, PERCENT)  
##########################RIGHT SIDEEE
    wait(100, MSEC)
    robot.turn_for(LEFT, 18.5, DEGREES)
    group_left.set_velocity(30, PERCENT)
    group_right.set_velocity(30, PERCENT)
    mobile_goal_motor.spin(FORWARD, 100, PERCENT)
    mobile_goal_motor.set_stopping(HOLD)
    robot.drive_for(REVERSE, 200, MM)
    mobile_goal_motor.set_stopping(COAST)
    mobile_goal_motor.spin(REVERSE)
    mobile_goal_motor.set_stopping(HOLD)
    robot.drive_for(REVERSE, 100, MM, 50, PERCENT)
    # take mobile goal
    group_left.set_velocity(60, PERCENT)
    group_right.set_velocity(60, PERCENT)
    wait(400, MSEC)

    # take 1st ring
    robot.turn_for(RIGHT, 16, DEGREES)
    intake_motor.spin(FORWARD)
    elevator_motor.spin(FORWARD, 70, PERCENT)
    robot.drive_for(FORWARD, 510, MM,60, PERCENT)
    wait(500, MSEC)

    # go to 2nd ring in front of wall stake 
    robot.turn_for(RIGHT, 8.5, DEGREES)
    wait(100, MSEC)
    robot.drive_for(FORWARD, 540, MM, 60, PERCENT)
    wait(100, MSEC)
    group_left.spin_for(FORWARD, 280, DEGREES)

    wait(500, MSEC)

    robot.drive(FORWARD)
    wait(800, MSEC)
    robot.drive_for(REVERSE, 310, MM)
    wait(200, MSEC)
    #take the other 3 rings
    robot.turn_for(RIGHT, 15, DEGREES, 60, PERCENT)
    robot.drive_for(FORWARD, 950, MM, 60, PERCENT)
    wait(600, MSEC)

    robot.drive_for(FORWARD, 280, MM, 60, PERCENT)
    wait(200, MSEC)

    robot.drive_for(REVERSE, 90, MM, 50, PERCENT)
    wait(500, MSEC)

    #######2 SCENARIOS (group right or turn right)
    #1 METHOD
    group_left.spin_for(REVERSE, 560, DEGREES)

    wait(100, MSEC)
    robot.drive(FORWARD)
    wait(700, MSEC)

    robot.drive_for(REVERSE, 150, MM, 50, PERCENT)
    wait(500, MSEC)
    robot.turn_for(LEFT, 22, DEGREES)
    mobile_goal_motor.set_stopping(COAST)
    mobile_goal_motor.spin_for(FORWARD, 1000, MSEC) 
    wait(300, MSEC)
    robot.drive_for(FORWARD, 100, MM, 60, PERCENT)

    robot.drive(REVERSE)  
    wait(900, MSEC)

    robot.drive_for(FORWARD, 200, MM, 70, PERCENT)
    robot.turn_for(LEFT, 17, DEGREES)
    wait(100, MSEC)
    robot.drive(REVERSE)
    wait(700, MSEC)



    

def user_control():
    brain.screen.clear_screen()
    global left_drive_smart_stopped, right_drive_smart_stopped
        
# create competition instance
# comp = Competition(user_control, autonomous)

# pre_autonomous()
user_control()
autonomous()
       
        
