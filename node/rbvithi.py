#!/usr/bin/env python
# license removed for brevity
import rospy
import sys
import time
from std_msgs.msg import String
from sensor_msgs.msg import Image
from robovithi.msg import RCV

class image_converter:

  def __init__(self):
    rospy.init_node('talker', anonymous=True)
    self.pub = rospy.Publisher('receive',RCV,queue_size=10)
    self.sub = rospy.Subscriber('chatter', RCV, self.callback,queue_size=10)
    
  def callback(self,data):
    self.pub.publish(data)

def main(args):
    try:
       ic = image_converter()
       rospy.spin()
    except KeyboardInterrupt:
       print("Shutting down")

if __name__ == '__main__':
       main(sys.argv)
