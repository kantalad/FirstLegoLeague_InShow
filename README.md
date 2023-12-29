
# LEGO First League Micropython

Welcome to the exciting world of LEGO First League programming! This file will guide you through using Micropython on your EV3 to control your robot and conquer the missions for this year's challenge.

Learn more about LEGO FFL here:  https://www.firstinspires.org/robotics/fll

## Missions:

This libraray was designed to inspire teams and make the leap into coding easier.  The missions are setup to work with the In Show season.

The missions and threads for this project are not complete.  There are some fully working missions but the majority are pseudo code with no plans to finish.

## Getting Started:

Hardware: Make sure you have your EV3, motors, sensors, and other accessories assembled.

Software: Download the LEGO Education Python editor or use another Micropython environment compatible with EV3. This project is setup for Visual Studio Code.

Connect your hub to the software via Bluetooth or USB cable.

## MyRobot.py File:

Under Modules you will find the MyRobot.py file.  You will need to adjust this file for your robot's configuration.  You will also see the avilable commands for your robot.

This file is currently setup for a robot with four motors.  Two are for driving, a motor is on the front and another on the back.

There are two light sensors used for line following.

There is a gyroscope which helps guild the robot and ensures accurate turns.

A touch sensor is located at the front for the drive unitl bump commands.

## main.py

This is the start file.   This file will initialize the brick and setup the menu system.

Be sure to add the threads in the order you wish to run your missions.

## Missions and Threads

Missions and threads are separated.

Mission files assume the robot is at a specific location knows how to accomplish the task from that spot.

Thread files are what sends the robot to the desired location.  For example: You will use a thread to move the robot to a particular location, then run the mission. Once the mission is over, you can continue the thread to move the robot to the next location and then run that mission.

The idea is to break down code into smaller, easier to program, tasks.

## Programming Tips:

Use clear and concise code with proper indentation and comments.

Break down complex tasks into smaller, reusable functions.

Utilize sensors (color, ultrasonic, etc.) to make autonomous decisions based on the mission requirements.

Test your code thoroughly by running the program and observing your robot's behavior.

Remember to modify and adapt the provided code to match your specific robot design and mission goals.

## Resources:

LEGO EV3 Prime Micropython Documentation: https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3/

LEGO First League Resources: https://www.firstinspires.org/robotics/fll/game-and-season

Online tutorials:

https://pybricks.com/ev3-micropython/

## Have Fun!

Have fun exploring the possibilities of Micropython and programming your robot to excel in the LEGO First League challenge!

Remember: You're encouraged to modify and improve the provided code to make your robot unique and efficient. Feel free to experiment, collaborate with your team, and most importantly, have fun mastering the exciting world of robotics!

Good luck!
