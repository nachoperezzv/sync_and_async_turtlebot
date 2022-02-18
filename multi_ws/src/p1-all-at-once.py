#!/usr/bin/env python

import rospy
from re import sub
from os import read
from array import array 
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Pose, Point, Vector3



rospy.init_node('p1-all-at-once', anonymous=False)

#node robot_name/mobile_base/commands/velocity -> type: geometry_msgs/Twist
pub_r1 = rospy.Publisher('robot1/mobile_base/commands/velocity', Twist, queue_size=1)
pub_r2 = rospy.Publisher('robot2/mobile_base/commands/velocity', Twist, queue_size=1)
pub_r3 = rospy.Publisher('robot3/mobile_base/commands/velocity', Twist, queue_size=1)
pub_r4 = rospy.Publisher('robot4/mobile_base/commands/velocity', Twist, queue_size=1)

twist = Twist()
twist.angular.z = 0.6283

while(True):
    pub_r1.publish(twist)
    pub_r2.publish(twist)
    pub_r3.publish(twist)
    pub_r4.publish(twist)
