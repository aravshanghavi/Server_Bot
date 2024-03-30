#!/usr/bin/env python3
import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Pose2D
import socket

global wheel_base
def callback(data):
    msg=Twist()
    linear_vel = msg.linear.x
    angular_vel = msg.angular.z
    #left wheels
    wheel_front_left = linear_vel + wheel_base*angular_vel
    wheel_back_left = linear_vel + wheel_base*angular_vel
    #right wheels
    wheel_front_right = linear_vel - wheel_base*angular_vel
    wheel_back_right = linear_vel - wheel_base*angular_vel

def main():
    global wheel_base
    wheel_base = 0.483
    pub = rospy.Publisher('/vel_wheel', Twist, queue_size=100)
    rospy.Subscriber('/cmd_vel', Twist, callback)
    rospy.spin()

if __name__=='__main__':
    main()
