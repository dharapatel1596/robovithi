#!/usr/bin/env python
# license removed for brevity
import rospy
import sys
import time
from src.rosImg2CvImg import rosImg2CvImg
from std_msgs.msg import String
from sensor_msgs.msg import Image
from robovithi.msg import RCV

class rbvithi:

  def __init__(self):
    rospy.init_node('talker', anonymous=True)
    self.pub = rospy.Publisher('receive',RCV,queue_size=10)
    self.sub = rospy.Subscriber('chatter', RCV, self.callback,queue_size=10)
    
  def callback(self,data):
    x = rosImg2CvImg()
    if data.operation != "":
    	x.ros2cv(data)
    self.pub.publish(data)

def main(args):
    try:
       ic = rbvithi()
       rospy.spin()
    except KeyboardInterrupt:
       print("Shutting down")

if __name__ == '__main__':
       main(sys.argv)
