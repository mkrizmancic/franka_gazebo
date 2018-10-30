#!/usr/bin/env python
"""
A simple script that translates desired gripper width to command for
JointGroupPositionController.
"""
import rospy
from std_msgs.msg import Float64MultiArray, MultiArrayDimension, Float64


def callback(data):
    pub = rospy.Publisher('/franka/gripper_position_controller/command',
                          Float64MultiArray, queue_size=1)

    msg = Float64MultiArray()
    msg.layout.dim = [MultiArrayDimension('', 2, 1)]
    msg.data = [data.data / 2, data.data / 2]

    pub.publish(msg)


if __name__ == '__main__':
    rospy.init_node('gripper_publisher')
    rospy.Subscriber("/franka/gripper_width", Float64, callback, queue_size=1)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
