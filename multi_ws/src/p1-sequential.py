#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist



rospy.init_node('p1sequential', anonymous=False)

twist = Twist()
rate = rospy.Rate(5)


#node robot_name/mobile_base/commands/velocity -> type: geometry_msgs/Twist
pub_r1 = rospy.Publisher('robot1/mobile_base/commands/velocity', Twist, queue_size=1)
pub_r2 = rospy.Publisher('robot2/mobile_base/commands/velocity', Twist, queue_size=1)
pub_r3 = rospy.Publisher('robot3/mobile_base/commands/velocity', Twist, queue_size=1)
pub_r4 = rospy.Publisher('robot4/mobile_base/commands/velocity', Twist, queue_size=1)

while(True):
    cont = 0
    while(cont < 10):
        twist.angular.z = 0.6283
        pub_r1.publish(twist)
        cont+=1
        rate.sleep()
    
    cont = 0
    while(cont < 10):
        twist.angular.z = 0.6283
        pub_r2.publish(twist)
        cont+=1
        rate.sleep()
    
    cont = 0
    while(cont < 10):
        twist.angular.z = 0.6283
        pub_r3.publish(twist)
        cont+=1
        rate.sleep()
    
    cont = 0
    while(cont < 10):
        twist.angular.z = 0.6283
        pub_r4.publish(twist)
        cont+=1
        rate.sleep()
    




