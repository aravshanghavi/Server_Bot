#!/usr/bin/env python3
import rospy
import tf
from nav_msgs.msg import Odometry

def callback(msg):

    br = tf.TransformBroadcaster()
    br.sendTransform((msg.pose.pose.position.x, msg.pose.pose.position.y, 0), (msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w), rospy.Time.now(), "base_footprint", "odom")

def main():
    rospy.init_node('odom_to_base_link_broadcaster')
    rospy.Subscriber("/odom", Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    main()