# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       bentdm197                                                    #
# 	Created:      12/19/2024, 2:07:57 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()
controller_1 = Controller()

#-------------------------------#
#   green motor - 18 : 01       #
#   red motor   - 36 : 01       #
#   blue motor  - 06 : 01       #
# ------------------------------#  


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

group_left = MotorGroup(left_motor_1, left_motor_2)
group_right = MotorGroup(right_motor_1, right_motor_2)  
wall_stake_motor = MotorGroup(wall_stake_motor_1, wall_stake_motor_2) 

robot = DriveTrain(group_left, group_right, wheelTravel = 260, wheelBase = 340, trackWidth = 100, units = MM)

# Set velocity & torque
group_right.set_velocity(100, PERCENT)
group_left.set_velocity(100, PERCENT)

intake_motor.set_velocity(100, PERCENT)
intake_motor.set_max_torque(100, PERCENT)

mobile_goal_motor.set_velocity(100, PERCENT)
mobile_goal_motor.set_max_torque(100, PERCENT)

elevator_motor.set_velocity(90, PERCENT)
arm_motor.set_velocity(100, PERCENT)
wall_stake_motor.set_velocity(100, PERCENT)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

# def pre_autonomous()

def autonomous():
    # # def Red Cong():
    #     robot.drive_for(REVERSE,260,MM,40,PERCENT)
    #     mobile_goal_motor.spin(FORWARD)
    #     group_left.spin_for(REVERSE,145,DEGREES)
    #     wait(200, MSEC)
    #     robot.drive_for(REVERSE,170,MM,20,PERCENT)
    #     wait(200,MSEC)
    #     mobile_goal_motor.spin(REVERSE)
    #     elevator_motor.spin_for(FORWARD,2,SECONDS)
    #     robot.turn_for(LEFT,10,DEGREES)
    #     robot.drive_for(FORWARD,230,MM,40,PERCENT)
    #     elevator_motor.spin(FORWARD)                
    #     intake_motor.spin(FORWARD)
    #     robot.drive_for(FORWARD,150,MM,20,PERCENT)
    #     wait(200,MSEC)
    #     intake_motor.stop()
    #     robot.turn_for(LEFT,27,DEGREES)
    #     robot.drive_for(FORWARD,600,MM,60,PERCENT)      
    #     elevator_motor.stop()

        

    # # def Red Tru():
    #     robot.drive_for(REVERSE,260,MM,40,PERCENT)
    #     mobile_goal_motor.spin(FORWARD)
    #     group_right.spin_for(REVERSE,145,DEGREES)
    #     wait(0.5,SECONDS)
    #     robot.drive_for(REVERSE,170,MM,20,PERCENT)
    #     wait(0.2,SECONDS)
    #     mobile_goal_motor.spin(REVERSE)
    #     wait(0.5,SECONDS)
    #     elevator_motor.spin_for(FORWARD,2,SECONDS)
    #     robot.turn_for(RIGHT,10,DEGREES)
    #     robot.drive_for(FORWARD,210,MM,20,PERCENT)
    #     wait(0.2,SECONDS)
    #     elevator_motor.spin(FORWARD)
    #     intake_motor.spin(FORWARD)
    #     robot.drive_for(FORWARD,130,MM,20,PERCENT)
    #     wait(0.5,SECONDS)
    #     intake_motor.stop()
    #     robot.turn_for(RIGHT,27,DEGREES)
    #     robot.drive_for(FORWARD,600,MM,50,PERCENT)      
    #     elevator_motor.stop()



    # # Def Blue Cong():
    #     robot.drive_for(REVERSE,260,MM,30,PERCENT)
    #     mobile_goal_motor.spin(FORWARD)
    #     group_left.spin_for(REVERSE,145,DEGREES)
    #     robot.drive_for(REVERSE,180,MM,25,PERCENT)
    #     wait(0.2,SECONDS)
    #     mobile_goal_motor.spin(REVERSE)
    #     elevator_motor.spin_for(FORWARD,2,SECONDS)
    #     wait(0.5,SECONDS)
    #     robot.turn_for(LEFT,10,DEGREES)
    #     robot.drive_for(FORWARD,210,MM,40,PERCENT)
    #     wait(0.2,SECONDS)
    #     elevator_motor.spin(FORWARD)
    #     intake_motor.spin(FORWARD)
    #     robot.drive_for(FORWARD,130,MM,20,PERCENT)
    #     wait(0.2,SECONDS)
    #     intake_motor.stop()
    #     robot.turn_for(LEFT,27,DEGREES)
    #     robot.drive_for(FORWARD,600,MM,50,PERCENT)      
    #     elevator_motor.stop()



    # #Def blue_tru():
        return
        robot.drive_for(REVERSE,280,MM,40,PERCENT)
        mobile_goal_motor.spin(FORWARD)
        group_right.spin_for(REVERSE,150,DEGREES)
        wait(0.3,SECONDS)
        robot.drive_for(REVERSE,170,MM,20,PERCENT)
        wait(0.2,SECONDS)
        mobile_goal_motor.spin(REVERSE)
        wait(0.2,SECONDS)
        elevator_motor.spin_for(FORWARD,1,SECONDS, 80, PERCENT)
        # robot.drive_for(REVERSE, 200, MM, 40, PERCENT)
        wait(0.1, SECONDS)
        # robot.turn_for(RIGHT,21,DEGREES)
        robot.turn_for(RIGHT,25,DEGREES)

        robot.drive_for(FORWARD,500,MM,50,PERCENT)
        wait(0.1, SECONDS)
        intake_motor.spin(FORWARD)
        elevator_motor.spin(FORWARD,80, PERCENT)  

        # wait(0.1, SECONDS)
        # intake_motor.spin(FORWARD)
        # elevator_motor.spin(FORWARD,80, PERCENT)
        # group_right.spin_for(FORWARD, 260, DEGREES)
        # robot.drive_for(FORWARD,300, MM, 40, PERCENT)

        # wait(0.1 ,SECONDS)
        # group_left.spin_for(FORWARD, 200, DEGREES)

        # wait(0.5, SECONDS)
        # group_left.spin_for(REVERSE, 200, DEGREES)
        # robot.drive_for(REVERSE, 130, MM, 40, PERCENT)
        # # wait(0.1, SECONDS)
        # # robot.turn_for(LEFT, 8, DEGREES)     
        # # robot.drive_for(FORWARD, 300, MM, 40, PERCENT)
        
  
def user_control():
    brain.screen.clear_screen()
    global left_drive_smart_stopped, right_drive_smart_stopped

    while True:
        # elevator
            # button L2
        if controller_1.buttonL2.pressing():
            elevator_motor.spin(FORWARD)

            # button L1
        elif controller_1.buttonL1.pressing():
            elevator_motor.spin(REVERSE)

            # button Release
        else:
            elevator_motor.stop()

        # mobile goal
            # button B
        if controller_1.buttonB.pressing():
            mobile_goal_motor.set_max_torque(100, PERCENT)
            mobile_goal_motor.spin(FORWARD)
            mobile_goal_motor.set_stopping(HOLD)

            # button X
        if controller_1.buttonX.pressing():
            mobile_goal_motor.set_max_torque(100, PERCENT)
            mobile_goal_motor.spin(REVERSE)
            mobile_goal_motor.set_stopping(HOLD)

            # button Right 
        if controller_1.buttonRight.pressing():
            mobile_goal_motor.set_stopping(COAST)
            mobile_goal_motor.stop()

        # wall stake
            # button Up
        if controller_1.buttonUp.pressing():
            wall_stake_motor.set_max_torque(100, PERCENT)
            wall_stake_motor.set_velocity(100, PERCENT)
            wall_stake_motor.spin(REVERSE)
            
            # button Down
        if controller_1.buttonDown.pressing():
            wall_stake_motor.set_velocity(60, PERCENT)
            wall_stake_motor.set_stopping(COAST)
            wall_stake_motor.spin_for(FORWARD, 300, MSEC)
            wall_stake_motor.stop()

        # intake
            # button R2
        if controller_1.buttonR2.pressing():
            intake_motor.set_stopping(COAST)
            intake_motor.spin(REVERSE)

            # button R1
        elif controller_1.buttonR1.pressing():
            intake_motor.set_stopping(COAST)
            intake_motor.spin(FORWARD)
            
            # button Release
        else:
            intake_motor.stop() 

        # arm
            # button Y 
        if controller_1.buttonY.pressing():
            arm_motor.set_max_torque(100, PERCENT)
            arm_motor.spin(FORWARD)
            arm_motor.set_stopping(HOLD)
            # button A 
        if controller_1.buttonA.pressing():
            arm_motor.spin_for(REVERSE, 200, MSEC)
            arm_motor.set_stopping(COAST)
            arm_motor.stop()

        #joystick
        rotate = 60*math.sin(0.007*controller_1.axis3.position())
        if controller_1.axis3.position() < -85:
            forward_left = -100
        elif controller_1.axis3.position() < -55:
            forward_left = -100
        else:
            forward_left = controller_1.axis3.position()

        left_drive_smart_speed = forward_left

        rotate = 60*math.sin(0.007*controller_1.axis2.position())
        if controller_1.axis2.position() < -85:
            forward_right = -100
        elif controller_1.axis2.position() < -85:
            forward_right = -100
        else:
            forward_right = controller_1.axis2.position()
        right_drive_smart_speed = forward_right

 
        if left_drive_smart_speed < 10 and left_drive_smart_speed > -10:
            if left_drive_smart_stopped:
                group_left.stop()
                left_drive_smart_stopped = 0
        else:
            left_drive_smart_stopped = 1

        if right_drive_smart_speed < 10 and right_drive_smart_speed > -10:
            if right_drive_smart_stopped:
                group_right.stop()
                right_drive_smart_stopped = 0
        else:
            right_drive_smart_stopped = 1


        if left_drive_smart_stopped:
            group_left.set_velocity(left_drive_smart_speed, PERCENT)
            group_left.spin(FORWARD)
        if right_drive_smart_stopped:
            group_right.set_velocity(right_drive_smart_speed, PERCENT)
            group_right.spin(FORWARD)
        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)

# pre_autonomous()
# user_control()
# autonomous()


        
