#!/usr/bin/env python
# license removed for brevity
import rospy
import sys
import time
from src.RosImg2CvImg import RosImg2CvImg
from std_msgs.msg import String
from sensor_msgs.msg import Image
from robovithi.msg import RCV

class Rbvithi:

  def __init__(self):
    rospy.init_node('talker', anonymous=True)
    self.pub = rospy.Publisher('receive',RCV,queue_size=10)
    self.sub = rospy.Subscriber('chatter', RCV, self.callback,queue_size=10)
    
  def callback(self,data):
    x = RosImg2CvImg()
    if data.operation != "":
    	x.ros2cv(data)
    self.pub.publish(data)

def main():
    try:
       Rbvithi()
       rospy.spin()
    except KeyboardInterrupt:
       print("Shutting down")

if __name__ == '__main__':
       main()
