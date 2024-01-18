#!/usr/bin/env python3
#In terminal: rosbag play --clock <rosbag name> .bag 

import rospy
import numpy as np
import pandas as pd
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
folder = "/home/dal/data/KF_standarlized/0629/"
# filename = 'M1'
'''
@author: Small Brian
@date: 20230627
@brief: This is a program to extract data from ROS topic and save it to CSV file when ctrl+c to exit this program.
@commit: Use relative time in ROS instead of absolute time. Add pandas dataframe index name.
0. Change the arraysize & trigger to 99999
1. Python3 /run this program
2. Open another termianl and run "rosbag play <bag files>.bag"
3. Use index to get the IMU data size
4. Change array size and trigger to IMU data size
5. Run step 1 & 2, get the IMU data csv
'''
class save_data():
    def __init__(self):
        # self.filename = input("Input file name: ")
        self.isStart = False
        self.imuang_x = list()
        self.start()
    def start(self):
        rospy.init_node('Topic_to_CSV', anonymous=True)
        print("Start extracting informaion.")
        self.record = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                                 0, 0, 0, 0, 0, 0, 0], ])
        print("Initla shape: ", np.shape(self.record))
        rospy.Subscriber('/handsfree/imu', Imu, self.get_IMU_data)
        rospy.spin()     
    def get_IMU_data(self, data):
        
        self.imuang_x.append(data.angular_velocity.z)



    def save_to_csv(self):
        print("Start saving data to csv.")
        df = pd.DataFrame(self.record)
        df.columns = ['time', 'cmd_vel', 'imuacc_x', 'imuacc_y', 'imuacc_z',  'imuang_x', 'imuang_y', 'imuang_z', 'imuori_x',
                       'imuori_y', 'imuori_z', 'imuori_w', 'odompos_x', 'odompos_y', 'odompos_z', 'odomori_x', 'odomori_y', 
                       'odomori_z', 'odomori_w']
        df.to_csv(folder + self.filename + '_withAngle.csv')
        print("Done! Save file to: ", folder + self.filename + "_withAngle.csv")
    def __del__(self):
        print("Destructor called.")
        # self.save_to_csv()
        average_omega= sum(self.imuang_x)/len(self.imuang_x)
        print("Average angular velocity: ", average_omega)
        #std
        std_omega = np.std(self.imuang_x)
        print("Std range: ", std_omega)
        #variance
        var_omega = np.var(self.imuang_x)
        print("Var range: ", var_omega)
if __name__ == '__main__':
    print("Start rostopic to csv.")
    save_data()