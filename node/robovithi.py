#!/usr/bin/env python
# license removed for brevity
import rospy
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Image

class image_converter:

  def __init__(self):
    rospy.init_node('talker', anonymous=True)
    self.pub = rospy.Publisher('receive',Image,queue_size=10)
    self.sub = rospy.Subscriber('chatter', Image, self.callback,queue_size=10)
    
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
