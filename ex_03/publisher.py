#!/usr/bin/env python


## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import random
import rospy
from std_msgs.msg import Int16

def talker():
    pub = rospy.Publisher('chatter', Int16, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	tmp = random.randint(1,11)
        rospy.loginfo(tmp)
        pub.publish(tmp)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

