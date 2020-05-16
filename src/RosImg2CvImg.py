#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class RosImg2CvImg:

  def ros2cv(self,data):
    self.bridge = CvBridge()
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data.image,"bgr8")
      cv2.imshow("Image window", cv_image)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
    except CvBridgeError as e:
      print(e)




