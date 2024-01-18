# HAMR_Manipulation
**This repo only contains main contribution of my work, other minor contribution and open-source ROS program (such as navigation package from ROS official) are not included, so directly download this repo and run it will not work**

## Background
We've studied the AMR (autonomous mobile robot) with robotic arm products that available in the market, most of them are heavy and only capable for light-weight manipulation. 
![marketing](image/marketing_small.png)
## Objective Goal
the goal of this research is to integrate robotic arm and a omni-wheel chassis that provides with hight payload, high accuracy and high speed, I call it HAMR (High payload Autonomous Mobile Robot)


## Setup
### Hardware
1. KUKA KR70 R2100 robotic arm (maximum payload: 80kg; maximum speed: 2m/s)
2. Adlee 3700W brushless motor *4 (with reduction gears)
3. Advantech ARK-1250L (i5-1145G7E, DDR4 16GB)
4. Pepper fuch ODM30M-R2000 LiDAR
5. Pepper fuch IMU360D-F99 IMU
6. ICP-DAS GW-7238D J1939-Modbus TCP gateway
![vehicle](image/vehicle_small.png)

### Software
1. ROS1 Noetic (base on [Adlink ros_menu](https://github.com/Adlink-ROS/ros_menu))
2. C++ 9.0.4
3. Python 3.8.10
4. Hector SLAM (for map building)
![map_building](image/map_building_small.png)

### Prerequest
1. All hardware work normal (power, signal and wire connection)
2. Use CAD file to build TF broadcaster to get the coordinate trnasformation in ROS

![tf_broadcaster](image/vehicle_tf_small.png)

## Folder function 
1. config: Config file for rviz.
2. amr_urdf: HAMR 3D model with movable joint/axis. Normally will not use this model to save computation power.
3. dal_tf: Coordinate transform broadcaster. Open this before open LiDAR and SLAM.
4. fromTopictoCSV: Save value from ROS Topic to CSV for post-processing.
5. imu360: Self-made P+F IMU360-F99 IMU driver for ROS. Works with ICP-DAS J1939 gateway.
6. kuka_control: Receive command from ROS topic and transmit to KUKA controller by TCP.
7. motor_control: Receive velocity from ROS topic and do the inverse kinematic; Send the velocity command to brushless motor driver.

 