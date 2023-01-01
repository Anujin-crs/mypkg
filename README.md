# mypkg

Assignment project for "Robot system" class which includes ROS2 program commands and test file.
This package contains the program that shows us spiral movement of turtle in 2D turtlesim program. 

![test](https://github.com/Anujin-crs/mypkg/actions/workflows/test.yml/badge.svg)

# Commands

talker node publishes data and the listener subscribes to the topic so it can receive that data.

## Topic
From talker node we publish linear velocity and angular velocity data of the turtle, which listener subscribes.
With the help of turtlesim application of ROS, we can see the spiral movement of turtle.

## Command usage 
Run each command on different interface

### turtlesim interface
to run turtlesim application:
```bash
$ ros2 run turtlesim turtlesim_node
```

### talker.py
Input example:
```bash
$ ros2 run mypkg talker 1.0 2.0 -0.2  # parameters
```
Output example:
```bash
[INFO] [1672401244.887741100] [talker_publisher_spiral]: Sending - Linear Velocity : 1.000000, Angular Velocity : 2.000000
[INFO] [1672401245.376044300] [talker_publisher_spiral]: Sending - Linear Velocity : 1.000000, Angular Velocity : 1.800000
[INFO] [1672401245.874582800] [talker_publisher_spiral]: Sending - Linear Velocity : 1.000000, Angular Velocity : 1.600000
[INFO] [1672401246.376259800] [talker_publisher_spiral]: Sending - Linear Velocity : 1.000000, Angular Velocity : 1.400000
```

### listener.py
Input example:
```bash
$ ros2 run mypkg listener
```
Output example:
```bash
[INFO] [1672401268.392911200] [listener_subscriber_spiral]: Recieved - Linear Velocity : 1.000000, Angular Velocity : -7.400000
[INFO] [1672401268.878995900] [listener_subscriber_spiral]: Recieved - Linear Velocity : 1.000000, Angular Velocity : -7.600000
[INFO] [1672401269.378982800] [listener_subscriber_spiral]: Recieved - Linear Velocity : 1.000000, Angular Velocity : -7.800000
[INFO] [1672401269.878526400] [listener_subscriber_spiral]: Recieved - Linear Velocity : 1.000000, Angular Velocity : -8.000000
```

## Required software
* Python 3.10
* ROS2
* Turtlesim

## Test environment
* Ubuntu 22.04
* Python 3.10
* ROS2 Humble

## Contributing
* Please feel free to contribute. Any kind of discussion is welcome.

## License
* This software package is licensed for redistribution and use under the BSD-3-Clause License.
* The code for this package is my own work with the permission of Professor Ryuichi Ueda of Chiba Institute of Technology, and some of the ideas are from @BotBuilder youtube channel
* © 2022 Anujin-crs

#### Citation
* ["Robot System" lesson slides of Professor Ryuichi Ueda](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* [Youtube channel @BotBuilder](https://www.youtube.com/@botbuilder3492)
 
  
